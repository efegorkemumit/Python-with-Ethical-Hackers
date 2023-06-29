#!/usr/bin/env python

import requests

def request(url):
    try:
        return requests.get("http://"+url)
    except requests.exceptions.ConnectionError:
        pass


target_url = "google.com"

with open("/home/kali/Desktop/lync_subdomains.txt", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = word + "." + target_url
        response = request(test_url)
        if response:
            print("[+] Discovered subdomain ---->>>> " +test_url)
