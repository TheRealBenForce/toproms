import api_data
import yaml

class Platforms():
    
    def __init__(self):
        return
    
    def refresh_platform_list(self):
        """
        Get's a new platform list using IGDB API
        """
        payload = "fields id,abbreviation,name,generation; sort name;"
        platform_list = api_data.ApiData("platforms", payload).get_api_data()
        # get rid of systems with no appreviation.
        trimmed_list = []
        for d in platform_list:
            if 'abbreviation' in d:
                trimmed_list.append(d)
        return trimmed_list
        
    def get_platform_list(self):
        """ Loads the entire platform list as a yaml file """
        with open("./yamls/platform_list.yml", 'r') as data:
            y = yaml.load(data)
        return y
        
