import os
import requests
import yaml
import sys

class ApiData():
    
    def __init__(self, endpoint, querydict):
        self.endpoint = endpoint
        self.querydict = querydict
        self.key = sys.argv[1:][0]
        self.limit=50
        self.url = "https://api-v3.igdb.com/" + endpoint
        self.headers = {'user-key': self.key}

    def get_api_data(self):
        """
        Sends API request to IGDB. 
        If response is equal to limit of 50, sends another until complete list is retrieved.
        """
        response = requests.request("POST", self.url, headers=self.headers, params=self.querydict)
        response_list = yaml.load(response.text)
        while len(yaml.load(response.text)) is self.limit:
            self.querydict['offset'] += self.limit
            response = requests.request("POST", self.url, headers=self.headers, params=self.querydict)
            response_list += yaml.load(response.text)
        return response_list