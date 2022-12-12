import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = 'https://suninjuly.github.io/get_attribute.html'

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver = webdriver.Chrome()
    driver.get(URL)

    # x_element = driver.find_element(By.ID, 'input_value')
    # x = x_element.text
    treasure_element = driver.find_element(By.ID, 'treasure')
    x = treasure_element.get_attribute('valuex')
    y = calc(x)
    answer_field = driver.find_element(By.XPATH, "//input[@id='answer']")
    answer_field.send_keys(y)
    driver.find_element(By.ID, 'robotCheckbox').click()
    driver.find_element(By.ID, 'robotsRule').click()
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()

finally:
    time.sleep(5)
    driver.quit()
