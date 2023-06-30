#!/usr/bin/env python

import requests
import re
from urllib.parse import urlparse


target_url = "http://192.168.187.134/mutillidae/"


def extract_links_from(url):
    response = requests.get(url)
    parsed_url = urlparse(url)
    domain = parsed_url.netloc

    links = re.findall('(?:href=")(.*?)"', response.content.decode('utf-8'))
    external_links = []
    for link in links:
        if link.startswith('http') and domain not in link:
            external_links.append(link)
    return external_links


external_links = extract_links_from(target_url)

for link in external_links:
    print(link)