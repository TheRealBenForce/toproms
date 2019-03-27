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
        
        
    def get_platform_abbrev(self, platform_id):
        """ Pass in a platform id and get the platform abbreviation"""
        try:
            with open("./yamls/platform_list.yml", 'r') as data:
                y = yaml.load(data)
            for c in y:
                if str(c['id']) == str(platform_id):
                    return c['abbreviation']
        except Exception as e:
            logging.exception(str(e))
        return()


    def get_platform_name(self, platform_id):
        """ Pass in a platform id and get the platform name"""
        try:
            with open("./yamls/platform_list.yml", 'r') as data:
                y = yaml.load(data)
            for c in y:
                if str(c['id']) == str(platform_id):
                    return c['name']
        except Exception as e:
            logging.exception(str(e))
        return()
