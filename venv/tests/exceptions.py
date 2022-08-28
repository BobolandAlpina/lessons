from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link_old = "http://suninjuly.github.io/registration1.html"
link_new = "http://suninjuly.github.io/registration2.html"

def registration_check(link):
    try:
        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.first_class > input")
        first_name.send_keys("Ivan")

        last_name = browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.second_class > input")
        last_name.send_keys("Petrov")

        email = browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.third_class > input")
        email.send_keys("email@email.ru")


        phone_num = browser.find_element(By.CSS_SELECTOR, "div.second_block > div.form-group.first_class > input")
        phone_num.send_keys("88005553535")

        address = browser.find_element(By.CSS_SELECTOR, "div.second_block > div.form-group.second_class > input")
        address.send_keys("Leningrad")

        submit_btn = browser.find_element(By.CSS_SELECTOR, "button.btn")
        submit_btn.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        assert "Congratulations! You have successfully registered!" == welcome_text

    finally:
        time.sleep(5)
        browser.quit()
#Для удобства запускаю метод со старой и новой ссылкой
registration_check(link_old)
registration_check(link_new)