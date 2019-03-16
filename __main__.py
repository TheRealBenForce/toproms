import sys
import yaml
import platforms
import games

def main():
    #platforms_obj = platforms.Platforms()
    #write_file('./yamls/platform_list.yml', platforms_obj.platform_list)
    
    
    games_obj = games.Games(18)
    filename  = './yamls/game_lists/' + games_obj.get_console_name(18) + '.yml'
    write_file(filename, games_obj.game_list)
    return

def write_file(filename, data):
    with open(filename, 'w') as outfile:
        yaml.safe_dump(data, outfile, default_flow_style=False)    
    return
    

if __name__ == '__main__':
    main()