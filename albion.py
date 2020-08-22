import asyncio
import requests
import aiofiles
import logging
import json


class AlbionDataBrowser:
    def __init__(self):
        self.supported_languages = ['PL-PL', 'EN-US']
        self.desired_cities = ['Thetford', 'Martlock', 'Lymhurst', 'Fort Sterling', 'Caerleon', 'Bridgewatch', 'Black Market']
        logging.debug('Initialising Albion database')
        
        with open('albion.json', mode='r', encoding='utf-8') as f:
            content = json.load(f)
        
        self.filter_data(content)

        logging.info('Initialised Albion database')


    def filter_data(self, content):
        self.database = []

        skip_entry = False
        for dictionary in content:
            item_dict = {}
            for language in self.supported_languages:
                try:
                    for key, value in dictionary['LocalizedNames'].items():
                        if language == key:
                            item_dict[language + '_name'] = value
                except AttributeError:
                    skip_entry = True
                    break

                try:
                    for key, value in dictionary['LocalizedDescriptions'].items():
                        if language == key:
                            item_dict[language + '_description'] = value
                except AttributeError:
                    for language in self.supported_languages:
                        item_dict[language + '_description'] = None

            if skip_entry:
                skip_entry = False
                continue
                    
            item_dict['ID'] = dictionary['UniqueName']

            logging.debug('AlbionDataBrowser - Loaded ID - ' + item_dict['ID'])

            self.database.append(item_dict)


    def find_by_name(self, name):
        name = name.lower()

        found = False
        for entry in self.database:
            for language in self.supported_languages:
                value = entry[language + '_name']

                if name == value.lower():
                    found = True
                    break

                if found:
                    break

            if found:
                item_name = entry[language + '_name']
                item_desc = entry[language + '_description']
                item_id = entry['ID']
                break
        try:
            output = {'description': item_desc, 'id': item_id, 'name': item_name}
        except UnboundLocalError:
            output = None
        print(output)
        return output


    def get_item_prices_by_id(self, item_id, quality=1):
        BASE_URL = 'https://www.albion-online-data.com/api/v2/stats/Prices/'
        
        url = BASE_URL + item_id + '?qualities=' + str(quality)

        print(url)
        r = requests.get(url)
        print(r.status_code)
        assert r.status_code == 200
        
        data = json.loads(r.content)

        return data




