import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = 'http://suninjuly.github.io/wait2.html'

try:
    browser = webdriver.Chrome()
    # browser.implicitly_wait(5)
    browser.get(URL)


    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, 'verify'))
)
    button.click()
    message = browser.find_element(By.ID, 'verify_message')

    assert 'successful' in message.text
finally:
    browser.quit()
