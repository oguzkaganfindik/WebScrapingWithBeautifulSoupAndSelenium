#########################################
import time
from selenium import webdriver

# Initialize Driver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options)
driver.get("https://miuul.com/")
time.sleep(2)

#########################################
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.example.com")
driver.title
driver.current_url
driver.quit()

#########################################
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options)
driver.get("https://www.miuul.com")
driver.title
driver.current_url
driver.quit()

#########################################