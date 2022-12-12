import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

URL = 'http://suninjuly.github.io/file_input.html'

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

try:
    driver = webdriver.Chrome()
    driver.get(URL)
    driver.find_element(By.NAME, 'firstname').send_keys('Andrew')
    driver.find_element(By.NAME, 'lastname').send_keys('Smith')
    driver.find_element(By.NAME, 'email').send_keys('mail@mail.com')
    driver.find_element(By.CSS_SELECTOR, '[type="file"]').send_keys(file_path)
    driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

finally:
    time.sleep(5)
    driver.quit()
