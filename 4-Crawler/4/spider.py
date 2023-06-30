#!/usr/bin/env python

import requests
import re


target_url = "http://192.168.187.134/mutillidae/"


def extract_links_from(url):
    response = requests.get(url)
    return re.findall('(?:href=")(.*?)"', response.content.decode('utf-8'))

href_links = extract_links_from(target_url)

for link in href_links:
    print(link)



