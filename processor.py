import re
import csv
import games
import roms
from console_args import CONSOLE_ARGS
from fuzzywuzzy import fuzz
import logging

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
        logging.info('Beginning to create a new list of files to copy.')
        total = 0
        for i in self.config_data:
            g = games.Games(i['platformID'])
            top_list = sorted(g.get_top_game_list())
            r = roms.Roms(i['platformID'])
            current_list = sorted(r.get_rom_file_list())
            best_list = []
            logging.info('PROCESSING: {}'.format(g.get_console_name()))
            for t in top_list:
                try:
                    file, short_name, score = self.find_highest(t, current_list)
                    if score > 80:
                        logging.info('MATCHED: {} | {} | high score {}'.format(t['name'], file, str(score)))
                        best_list.append(file)
                        total += 1
                    else:
                        logging.warning('SKIPPED DUE TO SCORE: {} | {} | high score {}'.format(t['name'], file, str(score)))
                except Exception as e:
                    logging.exception(str(e))
                    pass
            r.make_new_rom_set(best_list)
        return


    def trim_filename(self, filename):
        """ Attempts to trim extension and things in parans and brackets """
        no_ext = filename[:-4]
        result = re.sub("[\(\[].*?[\)\]]", "", no_ext)
        return result.strip()


    def find_highest(self, game, file_list):
        """ returns the filename, simple name, and score from a list that best matches a search game """
        top_score = 0
        top_short_name = None
        top_file = None
        for f in file_list:
            short_name = self.trim_filename(f)
            score = fuzz.token_set_ratio(game, short_name)
            if score > top_score:
                top_score = score
                top_file = f
                top_short_name = short_name
        return top_file, top_short_name, top_score