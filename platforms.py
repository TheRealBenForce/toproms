import api_data
import yaml

class Platforms():
    
    def __init__(self):
        return
    
    def refresh_platform_list(self):
        """
        Get's a new platform list using IGDB API
        """
        querydict = {
            "fields":"id,abbreviation,name,generation",
            "limit":50,
            "order":"name",
            "offset": 0
        }
        platform_list = api_data.ApiData("platforms", querydict).get_api_data()
        # get rid of systems with no appreviation.
        trimmed_list = []
        for d in platform_list:
            if 'abbreviation' in d:
                trimmed_list.append(d)
        print(trimmed_list)
        return trimmed_list
        
    def get_platform_list(self):
        """ Loads the entire platform list as a yaml file """
        with open("./yamls/platform_list.yml", 'r') as data:
            y = yaml.load(data)
        return y
        
