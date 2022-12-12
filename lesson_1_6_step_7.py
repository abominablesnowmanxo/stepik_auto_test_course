import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

URL = 'https://suninjuly.github.io/huge_form.html'

try:
    driver = webdriver.Chrome()
    driver.get(URL)
    elements = driver.find_elements(By.TAG_NAME, 'input')
    for element in elements:
        element.send_keys('Text')

    button = driver.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()


finally:
    time.sleep(10)
    driver.quit()
