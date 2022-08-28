from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    first_name = browser.find_element(By.NAME, "first_name")
    first_name.send_keys("George")

    last_name = browser.find_element(By.NAME, "last_name")
    last_name.send_keys("Gubin")

    city = browser.find_element(By.CSS_SELECTOR, "body > div > form > div:nth-child(3) > input")
    city.send_keys("Ulyanovsk")

    country = browser.find_element(By.ID, "country")
    country.send_keys("Russia")

    button = browser.find_element(By.ID, "submit_button")
    button.click()
    print('m-kay')
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()