#!/usr/bin/env python3
import requests
from requests import get
from requests.exceptions import RequestException
import contextlib
from contextlib import closing
from bs4 import BeautifulSoup

# Set the URL you want to webscrape from
url = 'http://empireatx.com/shows/'

my_session = requests.session()
for_cookies = my_session.get("http://empireatx.com/shows/")
cookies = for_cookies.cookies
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'}
my_url = 'http://empireatx.com/shows/'

response = my_session.get(my_url, headers=headers, cookies=cookies)
print(response.status_code) 
soup = BeautifulSoup(response.text, "html.parser")

with open("output-empire.html", "w") as file:
   file.write(str(soup))

for j in soup.findAll("a"):
    jItem = j.find("h3", {"event-title"})
    if jItem is not None: 
        print(jItem.get_text())