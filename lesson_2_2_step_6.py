
import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

URL = 'http://suninjuly.github.io/execute_script.html'

driver = webdriver.Chrome()
try:
    driver.get(URL)
    x_element = driver.find_element(By.ID, 'input_value')
    x = int(x_element.text)
    result = str(math.log(abs(12*math.sin(x))))
    driver.find_element(By.ID, 'answer').send_keys(result)
    checkbox = driver.find_element(By.ID, 'robotCheckbox')
    checkbox.location_once_scrolled_into_view
    checkbox.click()
    driver.find_element(By.ID, 'robotsRule').click()
    driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

finally:
    time.sleep(5)
    driver.quit()
