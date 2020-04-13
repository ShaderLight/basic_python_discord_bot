import json



class LanguageNotSupportedError(Exception):
    """Raised when passed language is not recognised"""


class Language:
    def __init__(self, lang_set):
        self.lang_set = lang_set.upper()

        self.update(self.lang_set)



    def read_localisation_file(self):
        
        if self.lang_set == 'EN':
            with open('locale/en_US.json', 'r') as f:
                language_dict = json.load(f)
    
        elif self.lang_set == 'PL':
            with open('locale/pl_PL.json', 'r') as f:
                language_dict = json.load(f)
        
        return language_dict


    def load_strings(self, language_dict):

        self.help = language_dict['help']
        self.language = language_dict['language']
        self.urban = language_dict['urban']
        self.urbanlist = language_dict['urbanlist']
        self.s_anime = language_dict['s_anime']
        self.s_manga = language_dict['s_manga']
        self.s_animelist = language_dict['s_animelist']
        self.s_mangalist = language_dict['s_mangalist']
        self.s_character = language_dict['s_character']
        self.s_characterlist = language_dict['s_characterlist']
        self.s_user = language_dict['s_user']
        self.s_userlist = language_dict['s_userlist']
        self.covid = language_dict['covid']


    def save_settings(self):

        with open('settings.json', 'r') as f:
            settings = json.load(f)
        
        settings['language'] = self.lang_set

        with open('settings.json', 'w') as f:
            json.dump(settings, f, indent=4)

    
    def update(self, desired_language):
        self.lang_set = desired_language.upper()

        if self.lang_set not in ['EN','PL']:
            raise LanguageNotSupportedError

        language_dict = self.read_localisation_file()

        self.load_strings(language_dict)

        self.save_settings()



    
        
        