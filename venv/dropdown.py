from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()
browser.get(link)
first_number_element = browser.find_element(By.ID, 'num1')
first_number_value = first_number_element.text

second_number_element = browser.find_element(By.ID, 'num2')
second_number_value = second_number_element.text

result = int(first_number_value) + int(second_number_value)

select = Select(browser.find_element(By.ID, "dropdown"))
select.select_by_value(str(result))
browser.execute_script("alert('hello world!')")

submit_btn = browser.find_element(By.CSS_SELECTOR, "button.btn")
submit_btn.click()