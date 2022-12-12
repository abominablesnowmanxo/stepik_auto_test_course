import time
import math
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    driver = webdriver.Chrome()
    driver.get(URL)

    wait = WebDriverWait(driver, 12)
    wait.until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
)
    driver.find_element(By.ID, 'book').click()
    x_element = driver.find_element(By.ID, 'input_value')
    x = int(x_element.text)
    time.sleep(1)
    result = str(math.log(abs(12*math.sin(x))))
    time.sleep(1)
    driver.find_element(By.ID, 'answer').send_keys(result)
    driver.find_element(By.ID, 'solve').click()

finally:
    # driver.switch_to.alert
    time.sleep(5)
    driver.quit()
