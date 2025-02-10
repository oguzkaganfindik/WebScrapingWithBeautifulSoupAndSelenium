#########################################
# Finding Elements and Extracting Data
#########################################

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.example.com")
element = driver.find_element(By.XPATH, "//a")
element
element.text
element.get_attribute("innerHTML")
element.get_attribute("href")