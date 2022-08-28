from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
import lesson_1_6_4

link = "http://suninjuly.github.io/find_link_text"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    encoded_lnk = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    encoded_lnk.click()
    time.sleep(1)
    lesson_1_6_4.formFiller(browser)
finally:
    browser.quit()