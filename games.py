import api_data
import yaml

class Games():
    
    def __init__(self, console_id):
        self.console_id = console_id
        self.game_list = self.refresh_game_list()
        self.console_name = self.get_console_name(console_id)
        return
    
    def refresh_game_list(self):
        """
        Get's a new game list using IGDB API
        """
        querydict = {
            "fields" : "id,name,rating,popularity,total_rating,total_rating_count",
            "limit" : 50,
            "order" : "popularity:desc",
            "offset" : 0,
            "filter[platforms][in]" : self.console_id
        }
        game_list = api_data.ApiData("games", querydict).get_api_data()
        return game_list
        
    def get_console_name(self, console_id):
        """ Pass in a console id and get the console name"""
        try:
            with open("./yamls/platform_list.yml", 'r') as data:
                y = yaml.load(data)
            for c in y:
                if c['id'] is console_id:
                    return c['abbreviation']
        except Exception as e:
            print(str(e))
