import json

import aiofiles


class LanguageNotSupportedError(Exception):
    """Raised when passed language is not recognised"""


class Language:
    def __init__(self, lang_set):
        self.lang_set = lang_set.upper()



    async def read_localisation_file(self):
        
        if self.lang_set == 'EN':
            async with aiofiles.open('locale/en_US.json', mode='r') as f:
                content = await f.read()
                language_dict = json.loads(content)
    
        elif self.lang_set == 'PL':
            async with aiofiles.open('locale/pl_PL.json', mode='r') as f:
                content = await f.read()
                language_dict = json.loads(content)
        
        return language_dict


    def load_strings(self, language_dict):

        self.help = language_dict['help']
        self.language = language_dict['language']
        self.urban = language_dict['urban']
        self.urbanlist = language_dict['urbanlist']
        self.s_anime = language_dict['shindenanime']
        self.s_manga = language_dict['shindenmanga']
        self.s_animelist = language_dict['shindenanimelist']
        self.s_mangalist = language_dict['shindenmangalist']
        self.s_character = language_dict['shindencharacter']
        self.s_characterlist = language_dict['shindencharacterlist']
        self.s_user = language_dict['shindenuser']
        self.s_userlist = language_dict['shindenuserlist']
        self.covid = language_dict['covid']


    async def save_settings(self):

        async with aiofiles.open('settings.json', 'r') as f:
            content = await f.read()

        settings = json.loads(content)
        settings['language'] = self.lang_set
        json_string = json.dumps(settings, indent=4)

        async with aiofiles.open('settings.json', 'w') as f:
            await f.write(json_string)

    
    async def update(self, desired_language):
        
        if desired_language not in ['EN','PL']:
            raise LanguageNotSupportedError
        
        self.lang_set = desired_language.upper()

        language_dict = await self.read_localisation_file()

        self.load_strings(language_dict)

        await self.save_settings()