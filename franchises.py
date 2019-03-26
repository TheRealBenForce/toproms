import api_data
import yaml
import games
import processor

class Franchises():

    def __init__(self, platform_id):
        self.platform_id = platform_id
        return


    def get_largest_franchise_ids(self):
        """ Uses the list of games to find the highest occuring franchise IDs"""
        franchise_ids_list = []
        p = processor.Processor()
        g = games.Games(self.platform_id)
        game_list = g.get_top_game_list()
        for game in game_list:
            if 'franchise' in game.keys():
                franchise_ids_list.append(game['franchise'])
        sorted_list = sorted(set(franchise_ids_list), key=lambda x: -franchise_ids_list.count(x))
        return sorted_list

    def refresh_franchise_list(self):
        """
        Get's a new franchise list using IGDB API based on the most represented
        franchises in the games lists.
        """
        ids = map(str, self.get_largest_franchise_ids())
        franchise_list = []
        while len(ids) > 0:
            first_ten_string = ','.join(ids[:10]) # api filter limit
            where = "where id = ({}); ".format(first_ten_string)
            fields = "fields id,name; "
            payload = fields + where
            franchise_list.append(api_data.ApiData("franchises", payload).get_api_data())
            ids = ids[10:]
        return franchise_list

    #def get_franchise_list(self):
    #    """ Loads the entire franchise list as a yaml file """
    #    with open("./yamls/franchise_list.yml", 'r') as data:
    #        y = yaml.load(data)
    #    return y

