import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

URL = 'http://suninjuly.github.io/execute_script.html'

driver = webdriver.Chrome()
try:
    driver.get(URL)
    button = driver.find_element(By.TAG_NAME, 'button')
    button.location_once_scrolled_into_view
    # driver.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(5)
    driver.quit()
