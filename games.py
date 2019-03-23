import api_data
import yaml
import logging


class Games():
    
    def __init__(self, platform_id):
        self.platform_id = platform_id
        return

    def refresh_game_list(self):
        """
        Get's a new game list using IGDB API. 
        Will collect for all platforms if there is no console id.
        """
        querydict = {
            "fields" : "id,name,popularity,rating,total_rating,total_rating_count",
            "limit" : 50,
            "order" : "total_rating:desc",
            "offset" : 0,
            "filter[total_rating_count][gt]":"4",
            "filter[platforms][in]" : self.platform_id
        }
        console_name = self.get_console_name()
        logging.info("Refreshing game list from IGDB for {}".format(console_name))
        game_list = api_data.ApiData("games", querydict).get_api_data()
        return game_list
        

    def get_console_name(self):
        """ Pass in a console id and get the console name"""
        try:
            with open("./yamls/platform_list.yml", 'r') as data:
                y = yaml.load(data)
            for c in y:
                if str(c['id']) == str(self.platform_id):
                    logging.info("Identified console as {}".format(c['name']))
                    return c['abbreviation']
        except Exception as e:
            logging.exception(str(e))
        return()
    
    def save_game_list(self, game_list):
        """ Exports a yaml file of the game list """
        filename  = './yamls/game_lists/' + self.get_console_name() + '.yml'
        with open(filename, 'w') as outfile:
            yaml.safe_dump(game_list, outfile, default_flow_style=False) 
        return

    def get_top_game_list(self):
        """ Loads the list of top games by looking up the abbreviation and reading that file name  """
        with open("./yamls/game_lists/" + self.get_console_name() +  ".yml", 'r') as data:
            y = yaml.load(data)
            return y
        return None
