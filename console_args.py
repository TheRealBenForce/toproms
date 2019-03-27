"""
Parsing of command line arguments.

No other functionality should be added to this module.
The typically usage is:

>>> from console_args import CONSOLE_ARGS 

https://stackoverflow.com/questions/41322486/access-argparse-variables-from-external-module
"""

import argparse

def _parse_arguments():
    parser = argparse.ArgumentParser(description='Makes a mini romset of the most popular roms from a larger rom set.')
    parser.add_argument('configFile',
                        default ='./config.csv',
                        nargs='?',
                        type=str,
                        help='the file that maps your platforms to directories')
    parser.add_argument('-a, --apikey',
                        type=str,
                        dest='apikey',
                        help='An optional api key for IGDB. Can be used to refresh platform and game lists.')
    parser.add_argument('-f --franchise',
                        dest='include_franchise',
                        action='store_true',
                        help="""If flag as set, will attempt to match all games within a franchise when at least
                        'one game is in the top ranked games."""
                        )
    return parser.parse_args()

CONSOLE_ARGS =  _parse_arguments()

# optional: delete function after use to prevent calling from other place
del _parse_arguments