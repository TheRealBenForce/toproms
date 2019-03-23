import sys
import yaml
import platforms
import games
import argparse
import processor
#import roms
import os
import logging.config
import yaml
from console_args import CONSOLE_ARGS


def main():
    setup_logging()
    if CONSOLE_ARGS.apikey:
        refresh_all()
    logging.info('Beginning rom processing')
    p = processor.Processor()
    p.make_top_list()
    return


def write_file(filename, data):
    with open(filename, 'w') as outfile:
        yaml.safe_dump(data, outfile, default_flow_style=False)    
    return


def refresh_all():
    logging.info('Detected API key, refreshing rom lists')
    platforms_obj = platforms.Platforms()
    platform_list = platforms_obj.refresh_platform_list()
    write_file('./yamls/platform_list.yml', platform_list)
    for p in platform_list:
        games_obj = games.Games(p['id'])
        filename  = './yamls/game_lists/' + games_obj.get_console_name() + '.yml'
        write_file(filename, games_obj.refresh_game_list())

def setup_logging(
    default_path='logging.yaml',
    default_level=logging.INFO,
    env_key='LOG_CFG'
):
    """Setup logging configuration"""
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

if __name__ == '__main__':
    main()