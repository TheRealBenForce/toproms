import re
import csv
import games
import roms
from console_args import CONSOLE_ARGS
from fuzzywuzzy import process

class Processor():
    def __init__(self):
        self.config_file = CONSOLE_ARGS.configFile
    
        config_list = []
        with open(self.config_file, 'rb') as f:
            reader = csv.reader(f)
            for row in reader:
                config_list.append({
                    'platformID' : row[0],
                    'folder' : row[1]
                })
            del config_list[0]
            self.config_data = config_list


    def make_top_list(self):
        """ Makes a new list of rom files based on most popular and what you have. """
        for i in self.config_data:
            g = games.Games(i['platformID'])
            top_list = sorted(g.get_top_game_list())
            r = roms.Roms(i['platformID'])
            current_list = sorted(r.get_rom_file_list())
            trimmed_list = []
            for r in current_list:
                trimmed_list.append(self.trim_filename(r))
            best_list = []
            print("PROCESSING: " + g.get_console_name())
            for t in top_list:
                try:
                    highest = process.extractOne(t['name'],trimmed_list)
                    if highest[1] > 85:
                        print(t['name'] + " <|> " + highest[0] + " <|> " + str(highest[1]))
                    else:
                        print("SKIPPING: " + t['name'] + " <|> " + highest[0] + " <|> " + str(highest[1]))
                except Exception as e:
                    print(str(e))
                    pass
        return
    
    def trim_filename(self, filename):
        """ Attempts to trim extension and things in parans and brackets """
        no_ext = filename[:-4]
        result = re.sub("[\(\[].*?[\)\]]", "", no_ext)
        return result.strip()
        
    #def match_top_game(self, top_game, game_list):
    #    """ takes a top game and finds the best match against a list"""
    #    best_match = None
    #    top_score = 0
    #    for g in game_list:
    #        pass
    #    return best_match