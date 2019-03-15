import requests
import yaml
import os
import platforms


def main():
    platforms_obj = platforms.Platforms()
    write_file('platform_list.yml', platforms_obj.platform_list)
    return

def write_file(filename, data):
    with open(filename, 'w') as outfile:
        yaml.safe_dump(data, outfile, default_flow_style=False)    
    return
    

if __name__ == '__main__':
    main()