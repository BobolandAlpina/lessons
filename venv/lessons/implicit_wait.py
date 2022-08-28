from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
# нужно будет обязательно вынести в отдельный файл и причесать код
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")
button = browser.find_element(By.CSS_SELECTOR, "button.btn")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
price = WebDriverWait(browser,13).until(EC.text_to_be_present_in_element((By.ID,'price'), "$100"))

button.click()

submit_btn = browser.find_element(By.ID, "solve")
browser.execute_script("return arguments[0].scrollIntoView(true);", submit_btn)

x_element = browser.find_element(By.ID, "input_value")
x_value = int(x_element.text)
browser.switch_to.default_content()
answer_input = browser.find_element(By.ID, "answer")
answer_input.send_keys(calc(x_value))


submit_btn.click()

answer_input.get_attribute()