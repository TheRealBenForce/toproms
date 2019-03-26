import re
import csv
import games
import roms
from console_args import CONSOLE_ARGS
from fuzzywuzzy import process
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
        ''' 
        Makes a new list of rom files based on most popular and what you have. 
        Then copies them to a new folder.
        '''
        logging.info('Beginning to create a new list of files to copy.')
        total = 0
        for i in self.config_data:
            g = games.Games(i['platformID'])
            r = roms.Roms(i['platformID'])
            top_list = sorted(g.get_top_game_list())
            file_list = sorted(r.get_rom_file_list())
            clean_file_list = map(lambda x: self.santize_string(x), file_list)
            best_list = []
            logging.info(u'PROCESSING: {}'.format(g.get_console_name()))
            for t in top_list:
                game = self.convert_to_romans(t['name'])
                try:
                    highest = process.extractOne(game, clean_file_list)
                    score = str(highest[1])
                    idx = clean_file_list.index(highest[0])
                    filename = file_list[idx]
                    if int(score) > 85:
                        logging.info(u'MATCHED: {} | {} | high score {}'.format(t['name'], filename, score))
                        best_list.append(filename)
                        total += 1
                    else:
                        logging.warning(u'SKIPPED DUE TO SCORE: {} | {} | high score {}'.format(t['name'], filename, score))
                except Exception as e:
                    logging.exception(str(e))
                    pass
            r.make_new_rom_set(best_list)
        return


    def trim_filename(self, string):
        ''' Attempts to trim extension and things in parans and brackets '''
        if string[-4:-3] == ".":
            string = string[:-4]
            string = re.sub('[\(\[].*?[\)\]]', '', string)
        return string.strip()


    #def remove_common_words(self, string):
    #    """ Removes most commond words from a string"""
    #    common = [
    #        "the", "be", "to", "of", "and", 
    #        "a", "in", "that", "have", "I", 
    #        "it", "for", "not", "on", "with", 
    #        "he", "as", "you", "do", "at"
    #        ]
    #    return string


    def convert_to_romans(self, string):
        ''' 
        Normalizes numbers by converting all to roman numerals.
        Assumes there won't be more than 20 games in a series to simplfy.
        Assumes there is always a space before the number and 
        zero or more non alpha character and zero or more
        non eol characters after like this example:
        Super Mega Fighter 4: Super Awesome Edition
        Super Mega Fighter 14: Super Awesome Edition
        Super Mega Fighter 4 - Super Awesome Edition
        Super Mega Fighter 4
        '''
        conversion = {
            '1':'I', '2':'II', '3':'III', '4':'IV', '5':'V', 
            '6':'VI', '7':'VII', '8':'VIII', '9':'IX', '10':'X',
            '11':'XI', '12':'XII', '13':'XIII', '14':'XIV', '15':'XV', 
            '16':'XVI', '17':'XVII', '18':'XVIII', '19':'XIX', '20':'XX'
            }
        pattern = r'(.)+(?P<num>\d)+(\W)*(.)*'
        if re.match(pattern, string):
            num = re.match(pattern, string).group('num')
            if num in conversion.keys():
                roman = conversion[num]
                string.replace(num, conversion[num])
        return string


    def santize_string(self, string):
        """Runs all sanitation methods against string"""
        string = self.trim_filename(string)
        string = self.convert_to_romans(string)
        return string