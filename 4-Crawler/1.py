#!/usr/bin/env python

import requests

url = "www.sds22323google.com"
try:
    get_response = requests.get("http://"+url)
    print(get_response)
except requests.exceptions.ConnectionError:
    pass

