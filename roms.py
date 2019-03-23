import processor
import os
import shutil
import logging


class Roms():
    
    def __init__(self, platform_id):
        self.platform_id = platform_id
        return


    def get_rom_file_list(self):
        """ gets a list of files from folder passed in """
        path = self.find_rom_list_folder()
        files = os.listdir(path)
        return files


    def find_rom_list_folder(self):
        """Gets the list of games to compare against file list."""
        try:
            p = processor.Processor()
            for c in p.config_data:
                if c['platformID'] == self.platform_id:
                    return c['folder']
        except Exception as e:
            logging.exception(str(e))
            raise
        return None


    def make_new_rom_set(self, rom_list):
        """ Copies roms from a list to a new folder """
        original_path = self.find_rom_list_folder() 
        new_path = self.determine_new_path(original_path)
        try:
            os.makedirs(new_path)
        except OSError as e:
            pass
        except Exception as e:
            logging.exception(str(e))
        for file in rom_list:
            try:
                if not os.path.exists(os.path.join(new_path, file)):
                    logging.info(u"Copying {} to {}".format(file, new_path))
                    shutil.copy2(original_path + "/" + file, new_path + "/")
                else:
                    logging.info(u"Skipping copy of {} to {}, file already exists".format(file, new_path))
            except Exception as e:
                logging.exception(str(e))
                pass
        return


    def determine_new_path(self, path):
        "Pass in a path and return a new path with 'toproms' branched one level down"
        substr = path.split("/")[-1][0]
        branch = "toproms/"
        idx = path.index(substr)
        path = path[:idx] + branch + path[idx:]
        return path