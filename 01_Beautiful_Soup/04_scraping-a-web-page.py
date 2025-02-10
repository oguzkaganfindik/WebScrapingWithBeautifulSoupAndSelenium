#######################################
# Scraping a Web Page
#######################################
# pip install requests

import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.example.com")
result.status_code
html = result.content
soup = BeautifulSoup(html, "html.parser")
soup.find("h1").text

#######################################

import requests
from bs4 import BeautifulSoup
result = requests.get("https://tr.m.wikipedia.org/wiki/Napolyon_Bonapart")
result.status_code
html = result.content
soup = BeautifulSoup(html, "html.parser")
title = soup.find("h1").text
content = soup.find("p").text
print(title)
print(content)

#######################################

import requests
from bs4 import BeautifulSoup
url = 'https://tr.m.wikipedia.org/wiki/Timur'
response = requests.get(url)
if response.status_code == 200:
    html = response.content
    soup = BeautifulSoup(html, "html.parser")
    print(soup.find("h1").text)
    print(soup.find("p").text)