import api_data
import yaml
import games
import processor
import platforms
import logging

class Franchises():

    def __init__(self, platform_id):
        self.platform_id = platform_id
        self.platform_abbrev = platforms.Platforms().get_platform_abbrev(platform_id)
        self.platform_name = platforms.Platforms().get_platform_name(platform_id)
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
        logging.info('Identified {} franchises for {} platform'.format(len(sorted_list), self.platform_name))
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
            franchise_list.append(api_data.ApiData("franchises", payload).get_api_data()[0])
            ids = ids[10:]
        return franchise_list

    def get_franchise_list(self):
        """ Loads the entire franchise list as a yaml file """
        with open("./yamls/franchise_lists/" + self.platform_abbrev + ".yml", 'r') as data:
            y = yaml.load(data)
        franchise_list = [d['name'] for d in y]
        print(franchise_list)
        return franchise_list

