import sys
import yaml
import platforms
import games
import argparse
import processor
#import roms
from console_args import CONSOLE_ARGS


def main():
    if CONSOLE_ARGS.apikey:
        refresh_all()
    p = processor.Processor()
    p.make_top_list()
    return


def write_file(filename, data):
    with open(filename, 'w') as outfile:
        yaml.safe_dump(data, outfile, default_flow_style=False)    
    return


def refresh_all():
    print("Detected API key, refreshing rom lists")
    platforms_obj = platforms.Platforms()
    platform_list = platforms_obj.refresh_platform_list()
    write_file('./yamls/platform_list.yml', platform_list)
    for p in platform_list:
        games_obj = games.Games(p['id'])
        filename  = './yamls/game_lists/' + games_obj.get_console_name() + '.yml'
        write_file(filename, games_obj.refresh_game_list())


if __name__ == '__main__':
    main()