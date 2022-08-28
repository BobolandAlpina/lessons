from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html"

browser = webdriver.Chrome()
browser.get(link)


x_element = browser.find_element(By.CSS_SELECTOR, 'span#input_value.nowrap')
x = x_element.text
y = calc(x)

answer = browser.find_element(By.CSS_SELECTOR, 'input#answer')
answer.send_keys(y)

iamrobot_checkbox = browser.find_element(By.ID, 'robotCheckbox')
iamrobot_checkbox.click()

robotrule_radio = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
robotrule_radio.click()

submit = browser.find_element(By.CSS_SELECTOR, 'button.btn')
submit.click()

time.sleep(5)

browser.close()