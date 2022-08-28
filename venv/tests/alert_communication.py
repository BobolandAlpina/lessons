from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

browser = webdriver.Chrome()
browser.get(link)

moving_btn = browser.find_element(By.CSS_SELECTOR, "button.trollface")
moving_btn.click()

new_window = browser.window_handles[1]

new_tab = browser.switch_to.window(new_window)

#alert = browser.switch_to.alert
#alert.accept()

#time.sleep(1)

x_element = browser.find_element(By.ID, "input_value")
x_value = int(x_element.text)
browser.switch_to.default_content()
answer_input = browser.find_element(By.ID, "answer")
answer_input.send_keys(calc(x_value))

submit_btn = browser.find_element(By.CSS_SELECTOR, "button.btn")
submit_btn.click()