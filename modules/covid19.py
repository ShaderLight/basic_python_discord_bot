import asyncio
from datetime import datetime
import json
import logging
from time import sleep
import random
import os

import aiohttp
import aiofiles
from bs4 import BeautifulSoup
import requests

BASEDIR = os.path.abspath(os.path.dirname(__file__))
BASEDIR = os.path.dirname(BASEDIR)

if not os.path.isdir(os.path.join(BASEDIR, 'databases')):
    os.makedirs(os.path.join(BASEDIR, 'databases'))


class Stats(object):
    def __init__(self, cases, deaths, recovered):
        self.cases = cases
        self.deaths = deaths
        self.recovered = recovered


class Covid_data:
    def __init__(self):
        self.base_url = 'https://worldometers.info/coronavirus/'
        self.last_updated = None
        
        # No need to use aiofiles because this gets executed at the 
        # very beggining, before bot connects to discord's websockets
        try:
            with open('databases/covid.json', 'r') as f:
                logging.debug('Found existing covid.json')
        except FileNotFoundError:
            with open('databases/covid.json', 'w') as f:
                logging.debug('No covid.json found, creating one')
                json.dump({'updated' : 'never'}, f, indent = 4)


    async def get_world_data(self, session):
        async with session.get(self.base_url) as response:
            assert response.status == 200
            content = await response.text()

        soup = BeautifulSoup(content, 'html.parser')
        data_container = soup.find('div', {'class':'content-inner'})
        
        counters = data_container.find_all('div', {'class':'maincounter-number'})
        
        cases = counters[0].text.replace('\n', '').replace(' ', '')
        deaths = counters[1].text.replace('\n', '').replace(' ', '')
        recovered = counters[2].text.replace('\n', '').replace(' ', '')

        response = Stats(cases, deaths, recovered)

        return response
    

    async def get_poland_data(self, session):
        url = self.base_url + 'country/poland/'

        async with session.get(url) as response:
            assert response.status == 200
            content = await response.text()

        soup = BeautifulSoup(content, 'html.parser')
        data_container = soup.find('div', {'class':'content-inner'})
        
        counters = data_container.find_all('div', {'class':'maincounter-number'})
        
        cases = counters[0].text.replace('\n', '').replace(' ', '')
        deaths = counters[1].text.replace('\n', '').replace(' ', '')
        recovered = counters[2].text.replace('\n', '').replace(' ', '')

        response = Stats(cases, deaths, recovered)

        return response
    

    async def save_data(self, world, poland):
        data_dict = {}

        current_date = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")


        data_dict['updated'] = current_date

        world_dict = {'cases': world.cases, 'deaths' : world.deaths, 'recovered' : world.recovered}
        poland_dict = {'cases': poland.cases, 'deaths' : poland.deaths, 'recovered' : poland.recovered}

        data_dict['world'] = world_dict
        data_dict['poland'] = poland_dict

        json_string = json.dumps(data_dict, indent = 4)

        async with aiofiles.open('databases/covid.json', mode='w') as f:
            await f.write(json_string)
    

    async def when_last_update(self):
        async with aiofiles.open('databases/covid.json', mode='r') as f:
            content = await f.read()
        
        data = json.loads(content)
        
        last_updated = data['updated']

        if last_updated == 'never':
            return 'never'

        datetime_last_updated = datetime.strptime(last_updated, "%d/%m/%Y, %H:%M:%S")

        return datetime_last_updated


    async def update(self):
        logging.debug('Updating covid data')
        user_agent = random.choice(['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582'])
        async with aiohttp.ClientSession(headers={'User-Agent':user_agent}) as session:

            world_data = await self.get_world_data(session)
            await asyncio.sleep(random.randrange(10, 20)/10)
            poland_data = await self.get_poland_data(session)


        await self.save_data(world_data, poland_data)
        
        logging.debug('Updated covid data')


    async def read_data(self):
        async with aiofiles.open('databases/covid.json', mode='r') as f:
            content = await f.read()
        
        data = json.loads(content)

        w_data = data['world']
        p_data = data['poland']

        world = Stats(w_data['cases'], w_data['deaths'], w_data['recovered'])
        poland = Stats(p_data['cases'], p_data['deaths'], p_data['recovered'])

        response = {'world' : world, 'poland' : poland}

        return response