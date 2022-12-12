import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

URL_1 = 'https://suninjuly.github.io/simple_form_find_task.html'
URL_2 = 'https://suninjuly.github.io/find_link_text'
value = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    driver = webdriver.Chrome()
    driver.get(URL_2)
    link = driver.find_element(By.LINK_TEXT, value)
    link.click()

    first_name = driver.find_element(By.TAG_NAME, 'input')
    first_name.send_keys('Ivan')
    last_name = driver.find_element(By.NAME, 'last_name')
    last_name.send_keys('Petrov')
    city = driver.find_element(By.CLASS_NAME, 'city')
    city.send_keys('Smolensk')
    country = driver.find_element(By.ID, 'country')
    country.send_keys('Russia')
    button = driver.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

finally:
    time.sleep(10)
    driver.quit()

