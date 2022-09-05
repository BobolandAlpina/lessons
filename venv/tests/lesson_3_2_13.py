from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
import pytest

class TestExceptions(unittest.TestCase):
    link = "http://suninjuly.github.io/registration1.html"
    link2 = "http://suninjuly.github.io/registration2.html"
    def test_registration1(self):
        browser = webdriver.Chrome()
        browser.get(self.link)

        first_name = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
        first_name.send_keys("Ivan")

        last_name = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
        last_name.send_keys("Petrov")

        email = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
        email.send_keys("email@email.ru")

        phone_num = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your phone:']")
        phone_num.send_keys("88005553535")

        address = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your address:']")
        address.send_keys("Leningrad")

        submit_btn = browser.find_element(By.CSS_SELECTOR, "button.btn")
        submit_btn.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        success_div = browser.find_element(By.CSS_SELECTOR, "body > div > h1")
        success_msg = success_div.text

        self.assertEqual(success_msg, "Congratulations! You have successfully registered!")
        browser.quit()

    def test_registration2(self):
        browser = webdriver.Chrome()
        browser.get(self.link2)

        first_name = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
        first_name.send_keys("Ivan")

        last_name = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
        last_name.send_keys("Petrov")

        email = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
        email.send_keys("email@email.ru")

        phone_num = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your phone:']")
        phone_num.send_keys("88005553535")

        address = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your address:']")
        address.send_keys("Leningrad")

        submit_btn = browser.find_element(By.CSS_SELECTOR, "button.btn")
        submit_btn.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        success_div = browser.find_element(By.CSS_SELECTOR, "body > div > h1")
        success_msg = success_div.text

        self.assertEqual(success_msg, "Congratulations! You have successfully registered!")
        browser.quit()

if __name__ == "__main__":
    unittest.main()