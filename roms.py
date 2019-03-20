import processor
import os
import shutil

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
            print(str(e))
            raise
        return None


    def make_new_rom_set(self, rom_list):
        """ Copies roms from a list to a new folder """
        original_path = self.find_rom_list_folder() 
        new_path = original_path + " - Top Roms"
        try:
            os.mkdir(new_path)
        except OSError:
            pass
        except Exception as e:
            print(str(e))
        for file in rom_list:
            try:
                #print("Copying {} to {}".format(file, path))
                shutil.copy2(original_path + "/" + file, new_path + "/")
            except Exception as e:
                print(str(e))
                pass
        return