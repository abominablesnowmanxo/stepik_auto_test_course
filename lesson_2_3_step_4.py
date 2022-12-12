import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

URL = 'http://suninjuly.github.io/alert_accept.html'

try:
    driver = webdriver.Chrome()
    driver.get(URL)
    driver.find_element(By.TAG_NAME, 'button').click()
    confirm = driver.switch_to.alert
    confirm.accept()
    x_element = driver.find_element(By.ID, 'input_value')
    x = int(x_element.text)
    result = str(math.log(abs(12*math.sin(x))))
    driver.find_element(By.ID, 'answer').send_keys(result)
    driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

finally:
    time.sleep(3)
    driver.quit()
