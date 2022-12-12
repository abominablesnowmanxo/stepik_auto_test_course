import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

URL = 'http://suninjuly.github.io/selects2.html'

driver = webdriver.Chrome()
try:
    driver.get(URL)
    num_1 = driver.find_element(By.ID, "num1")
    num_2 = driver.find_element(By.ID, "num2")
    result = int(num_1.text) + int(num_2.text)
    select = Select(driver.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(str(result))
    driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

finally:
    time.sleep(5)
    driver.quit()
