from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

browser = webdriver.Chrome()
browser.get(link)


chest = browser.find_element(By.ID, 'treasure')
value_x = chest.get_attribute('valuex')
y = calc(value_x)
print(value_x)
answer = browser.find_element(By.CSS_SELECTOR, 'input#answer')
answer.send_keys(y)

iamrobot_checkbox = browser.find_element(By.ID, 'robotCheckbox')
iamrobot_checkbox.click()
print(iamrobot_checkbox.get_attribute("checked"))
robotrule_radio = browser.find_element(By.ID, 'robotsRule')
robotrule_radio.click()

submit = browser.find_element(By.CSS_SELECTOR, 'button.btn')
submit.click()

time.sleep(5)

browser.close()