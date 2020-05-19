from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import pyperclip
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    url = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(url)
    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID,'price'), '100'))
    browser.find_element_by_xpath("//button").click()

    num = browser.find_element_by_xpath("//span[@id = 'input_value']").text
    res = calc(num)

    browser.find_element_by_xpath("//input[@id = 'answer']").send_keys(res)
    browser.find_element_by_xpath("//button[@id='solve']").click()

    time.sleep(5)

    alert_text = browser.switch_to.alert.text
    add_to_clipboard = alert_text.split(": ")[-1]
    pyperclip.copy(add_to_clipboard)

finally:
    browser.quit()