#!/usr/bin/env python

import requests

def request(url):
    try:
        return requests.get("http://"+url)
    except requests.exceptions.ConnectionError:
        pass


target_url = "192.168.187.134/mutillidae/"


response = request(target_url)
print(response.content)