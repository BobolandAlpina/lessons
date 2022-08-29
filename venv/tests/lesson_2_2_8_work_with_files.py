from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os

link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)

name_input = browser.find_element(By.NAME, "firstname")
name_input.send_keys("George")

name_input = browser.find_element(By.NAME, "lastname")
name_input.send_keys("Gubin")

name_input = browser.find_element(By.NAME, "email")
name_input.send_keys("mail@mail.ru")

current_dir = os.path.abspath(os.path.dirname(__file__))
filedir = os.path.join(current_dir, "bio.txt")

ofd = browser.find_element(By.CSS_SELECTOR, "[type=file]")
ofd.send_keys(filedir)

submit = browser.find_element(By.CSS_SELECTOR, "button.btn")
submit.click()

time.sleep(5)