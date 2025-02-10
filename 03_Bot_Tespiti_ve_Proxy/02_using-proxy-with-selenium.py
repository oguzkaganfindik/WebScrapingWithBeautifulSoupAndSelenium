#########################################
# Using Proxy with Selenium
#########################################

import requests
from selenium import webdriver
from extension import proxies

url = 'https://www.ipaddress.my/'

proxy_username = 'JX2kX2Gf'
proxy_password = 'eWKNTTTF'
proxy_ip_address = '104.239.108.144'
proxy_port = '6379'

# username:password@ip_address:port
options = webdriver.ChromeOptions()
# options.add_argument(f'--proxy-server={proxy_ip_address}:{proxy_port}')

proxies_extension_path = proxies(proxy_username, proxy_password, proxy_ip_address, proxy_port)
options.add_extension(proxies_extension_path)
# selenium-wire

driver = webdriver.Chrome(options=options)
driver.get(url)

