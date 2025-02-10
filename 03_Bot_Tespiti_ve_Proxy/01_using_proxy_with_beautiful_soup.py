#########################################
# Using Proxy with Beautiful Soup
#########################################

import requests
from bs4 import BeautifulSoup

url = 'https://www.ipaddress.my/'

headers = {
    "User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7",
    "Accept-Language":"en-US,en;q=0.5"
}
# proxies = {
#     #username:password@ip_address:port
#     "http": 'http://JX2kX2Gf:eWKNTTTF@216.19.205.244:6565',
#     "https":'http://JX2kX2Gf:eWKNTTTF@216.19.205.244:6565',
# }

# response = requests.get(url,  headers=headers, proxies=proxies)
response = requests.get(url,  headers=headers)
response.status_code

soup = BeautifulSoup(response.content, 'html.parser')
ip_address_element = soup.find("div", attrs={"class":"panel-body"}).find("li").find("span")
flag_element = soup.find("div", attrs={"class":"panel-body"}).find_all("li")[-1].find("img")
ip_address = ip_address_element.text
flag = flag_element["alt"]

print(ip_address)
print(flag)
