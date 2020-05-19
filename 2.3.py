# from selenium.webdriver.support.ui import Select
# from selenium import webdriver
# import time
# import pyperclip
#
# import math
#
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
#
# try:
#     link = "http://suninjuly.github.io/alert_accept.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     # Ваш код, который заполняет обязательные поля
#     # num1 = browser.find_element_by_xpath("//span[@id='num1']").text
#     # num2 = browser.find_element_by_xpath("//span[@id='num2']").text
#     # num = browser.find_element_by_xpath("//span[@id='input_value']").text
#     # sum = int(num1)+int(num2)
#     # select= Select(browser.find_element_by_tag_name("select"))
#     # select.select_by_visible_text(str(sum))
#     browser.find_element_by_xpath("//button").click()
#     browser.switch_to.alert.accept()
#     num = browser.find_element_by_xpath("//span[@id='input_value']").text
#     res = calc((num))
#     browser.find_element_by_xpath("//input[@id='answer']").send_keys(res)
#     # browser.find_element_by_xpath("//input[@id='robotCheckbox']").click()
#     # rad = browser.find_element_by_xpath("//input[@id='robotsRule']")
#     # browser.execute_script("return arguments[0].scrollIntoView(true);",rad)
#     # rad.click()+
#     # Отправляем заполненную форму
#     button = browser.find_element_by_css_selector("button.btn")
#     browser.execute_script("return arguments[0].scrollIntoView(true);", button)
#     button.click()
#
#
#     # Проверяем, что смогли зарегистрироваться
#     # ждем загрузки страницы
#     time.sleep(10)
#     alert_text = browser.switch_to.alert.text
#     add_to_clipboard = alert_text.split(": ")[-1]
#     pyperclip.copy(add_to_clipboard)
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(1)
#     # закрываем браузер после всех манипуляций
#     browser.quit()


import math
x = 2
y = math.log(abs(12*math.sin(x)))
print(y)


from selenium import webdriver
import math
import pyperclip
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    url = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(url)
    first_window = browser.window_handles[0]
    time.sleep(10)
    browser.find_element_by_xpath("//button").click()
    new_window = browser.window_handles[1]
    time.sleep(3)
    browser.switch_to.window(new_window)

    num = browser.find_element_by_xpath("//span[@id = 'input_value']").text
    res = calc(num)

    browser.find_element_by_xpath("//input[@id = 'answer']").send_keys(res)
    browser.find_element_by_xpath("//button").click()

    time.sleep(3)

    alert_text = browser.switch_to.alert.text
    add_to_clipboard = alert_text.split(": ")[-1]
    pyperclip.copy(add_to_clipboard)

finally:
    browser.quit()