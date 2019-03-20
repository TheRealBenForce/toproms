import processor
import os

class Roms():
    
    def __init__(self, platform_id):
        self.platform_id = platform_id
        return


    def get_rom_file_list(self):
        """ gets a list of files from folder passed in """
        path = './' + self.find_rom_list_folder()
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
            print(str(e))
            raise
        return None
        