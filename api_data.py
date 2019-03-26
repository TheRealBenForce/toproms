import os
import requests
import yaml
import sys
import logging
from console_args import CONSOLE_ARGS

class ApiData():
    
    def __init__(self, endpoint, search):
        self.endpoint = endpoint
        self.search = search
        self.key = CONSOLE_ARGS.apikey
        self.limit=50
        self.offset=0
        self.url = "https://api-v3.igdb.com/" + endpoint
        self.headers = {'user-key': self.key}
        self.payload = "{} limit {}; offset {};".format(self.search, self.limit, self.offset)

    def get_api_data(self):
        """
        Sends API request to IGDB. 
        If response is equal to limit of 50, sends another until complete list is retrieved
        or limit of 200 is reached.
        """
        try:
            response = requests.request("GET", self.url, headers=self.headers, data=self.payload)
            response_list = yaml.load(response.text)
            while len(yaml.load(response.text)) is self.limit and (self.offset + self.limit) <= 150:
                self.offset += self.limit
                self.payload = "{} limit {}; offset {};".format(self.search, self.limit, self.offset)
                response = requests.request("GET", self.url, headers=self.headers, data=self.payload)
                response_list += yaml.load(response.text)
        except Exception as e:
            logging.Exception("Exception with payload: " + self.payload)
            logging.Exception(str(e))
            raise
        return response_list