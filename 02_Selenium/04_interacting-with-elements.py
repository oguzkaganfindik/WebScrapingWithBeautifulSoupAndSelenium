####################################################
# Interacting with Elements
####################################################
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.miuul.com")
time.sleep(2)

btn_elements = driver.find_elements(By.XPATH, "//a[@id='login']")
btn = btn_elements[0]
btn.click()

inputs = driver.find_elements(By.XPATH, "//input[@name='arama']")
input = inputs[0]
input.send_keys("Machine Learning", Keys.ENTER)
# input.send_keys(Keys.ENTER)

####################################################

driver = webdriver.Chrome()
driver.get("https://www.google.com")
time.sleep(5)

inputs = driver.find_elements(By.XPATH, "//textarea[@name='q']")
input = inputs[0]
input.send_keys("Machine Learning", Keys.ENTER)

####################################################
# Fakat google bot olduğumuzu anladığından dolayı doğrulama istiyor.
# Bu durumu aşmak için:

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36")

driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com")
search_box = driver.find_element(By.XPATH, "//textarea[@name='q']")

search_box.send_keys("Machine Learning", Keys.ENTER)

time.sleep(10)

# driver.quit()

####################################################
