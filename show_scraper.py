#!/usr/bin/env python3
import requests
from requests import get
from requests.exceptions import RequestException
import contextlib
from contextlib import closing
from bs4 import BeautifulSoup

#one function for mohawk
#one function for barracuda
#one function for empire
#one for love goat
#one for hotel vegas

# Set the URL you want to webscrape from
url = 'https://www.mohawkaustin.com/'

# Connect to the URL
response = requests.get(url)
#print(response.text)
# Parse HTML and save to BeautifulSoup object
soup = BeautifulSoup(response.text, "html.parser")

for j in soup.findAll("article", {"list-view-item"}):
    print(j.find("article", {"artist-info"}).find("a").get_text())
    print(j.find("time", {"date-time"}).find("span", {"dates"}).get_text())
