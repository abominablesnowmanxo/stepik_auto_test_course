import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

URL = 'http://suninjuly.github.io/registration2.html'

try:
    driver = webdriver.Chrome()
    driver.get(URL)

    first_name = driver.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
    first_name.send_keys('Ivan')
    last_name = driver.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
    last_name.send_keys('Petrov')
    email = driver.find_element(By.XPATH, "//input[@placeholder='Input your email']")
    email.send_keys('mail@mail.com')

    button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()
    time.sleep(1)

    welcome_text_el = driver.find_element(By.TAG_NAME, 'h1')
    welcome_text = welcome_text_el.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    driver.quit()
