import json
from urllib import request

class retriever:
    def __init__(self, url):
        self.url = url

    def retrieveJSON(self):
        response = request.urlopen(self.url)
        data = json.load(response) 
        return data
