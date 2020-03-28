import requests
from bs4 import BeautifulSoup

from datetime import datetime
import json
from time import sleep


class Stats(object):
    def __init__(self, cases, deaths, recovered):
        self.cases = cases
        self.deaths = deaths
        self.recovered = recovered


class Covid_data:
    def __init__(self):
        self.base_url = 'https://worldometers.info/coronavirus/'
        self.last_updated = None
        
        try:
            with open('covid.json', 'r') as f:
                pass
        except FileNotFoundError:
            with open('covid,json', 'w') as f:
                json.dump({'updated' : 'never'}, f, indent = 4)


    def get_world_data(self):
        r = requests.get(self.base_url)
        
        assert r.status_code == 200

        soup = BeautifulSoup(r.content, 'html.parser')
        data_container = soup.find('div', {'class':'content-inner'})
        
        counters = data_container.find_all('div', {'class':'maincounter-number'})
        
        cases = counters[0].text.replace('\n', '').replace(' ', '')
        deaths = counters[1].text.replace('\n', '').replace(' ', '')
        recovered = counters[2].text.replace('\n', '').replace(' ', '')

        response = Stats(cases, deaths, recovered)

        return response
    

    def get_poland_data(self):
        url = self.base_url + 'country/poland/'

        r = requests.get(url)
        
        assert r.status_code == 200

        soup = BeautifulSoup(r.content, 'html.parser')
        data_container = soup.find('div', {'class':'content-inner'})
        
        counters = data_container.find_all('div', {'class':'maincounter-number'})
        
        cases = counters[0].text.replace('\n', '').replace(' ', '')
        deaths = counters[1].text.replace('\n', '').replace(' ', '')
        recovered = counters[2].text.replace('\n', '').replace(' ', '')

        response = Stats(cases, deaths, recovered)

        return response
    

    def save_data(self, world, poland):
        data_dict = {}

        current_date = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")


        data_dict['updated'] = current_date

        world_dict = {'cases': world.cases, 'deaths' : world.deaths, 'recovered' : world.recovered}
        poland_dict = {'cases': poland.cases, 'deaths' : poland.deaths, 'recovered' : poland.recovered}

        data_dict['world'] = world_dict
        data_dict['poland'] = poland_dict

        with open('covid.json', 'w') as f:
            json.dump(data_dict, f, indent = 4)
    

    def when_last_update(self):
        with open('covid.json', 'r') as f:
            data = json.load(f)
        
        last_updated = data['updated']

        if last_updated == 'never':
            return 'never'

        datetime_last_updated = datetime.strptime(last_updated, "%d/%m/%Y, %H:%M:%S")

        return datetime_last_updated


    def update(self):
        world_data = self.get_world_data()
        sleep(0.5)
        poland_data = self.get_poland_data()

        self.save_data(world_data, poland_data)


    def read_data(self):
        with open('covid.json', 'r') as f:
            data = json.load(f)

        w_data = data['world']
        p_data = data['poland']

        world = Stats(w_data['cases'], w_data['deaths'], w_data['recovered'])
        poland = Stats(p_data['cases'], p_data['deaths'], p_data['recovered'])

        response = {'world' : world, 'poland' : poland}

        return response