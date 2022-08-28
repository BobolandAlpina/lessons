from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

x_element = browser.find_element(By.ID, "input_value")
x_value = int(x_element.text)

answer_input = browser.find_element(By.ID, "answer")
answer_input.send_keys(calc(x_value))

button = browser.find_element(By.CSS_SELECTOR,  "button.btn")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)

iamrobot_checkbox = browser.find_element(By.ID, 'robotCheckbox')
iamrobot_checkbox.click()

robotrule_radio = browser.find_element(By.ID, 'robotsRule')
robotrule_radio.click()


button.click()
time.sleep(5)