import requests
import re
from urllib.parse import urljoin

target_url = "http://192.168.187.134/mutillidae/"

visited_links = set()  # Set to store unique links
paths = set()  # Set to store discovered paths

def extract_links_from(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return re.findall('(?:href=")(.*?)"', response.text)
    except (requests.RequestException, UnicodeDecodeError):
        return []

def crawl(url):
    href_links = extract_links_from(url)
    for link in href_links:
        absolute_link = urljoin(url, link)
        if absolute_link.startswith(target_url):
            if absolute_link not in visited_links:
                visited_links.add(absolute_link)
                paths.add(absolute_link)
                print(absolute_link)
                crawl(absolute_link)

# Crawl the target URL
crawl(target_url)

# Print unique links
print("Unique Links:")
for link in visited_links:
    print(link)

# Print discovered paths
print("Discovered Paths:")
for path in paths:
    print(path)
