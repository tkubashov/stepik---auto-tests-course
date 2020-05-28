from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    # num1 = browser.find_element_by_xpath("//span[@id='num1']").text
    # num2 = browser.find_element_by_xpath("//span[@id='num2']").text
    num = browser.find_element_by_xpath("//span[@id='input_value']").text
    # sum = int(num1)+int(num2)
    # select= Select(browser.find_element_by_tag_name("select"))
    # select.select_by_visible_text(str(sum))
    res = calc((num))
    browser.find_element_by_xpath("//input[@id='answer']").send_keys(res)
    browser.find_element_by_xpath("//input[@id='robotCheckbox']").click()
    rad = browser.find_element_by_xpath("//input[@id='robotsRule']")
    browser.execute_script("return arguments[0].scrollIntoView(true);",rad)
    rad.click()
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(10)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

kjfdvkdndkbnd
dbjndkjdkf
djfndkjbndkfbn
dfbndjbnkdjfndn
dfoijdobfdnb
dojbnjdnbf
