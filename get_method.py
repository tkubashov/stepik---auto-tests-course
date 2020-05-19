# # import math
# # from selenium import webdriver
# # import time
# #
# # link = "http://suninjuly.github.io/find_xpath_form"
# # text = str(math.ceil(math.pow(math.pi, math.e)*10000))
# # try:
# #     browser = webdriver.Chrome()
# #     browser.get(link)
# #
# #     # browser.find_element_by_link_text(text).click()
# #
# #     input1 = browser.find_element_by_tag_name("input")
# #     input1.send_keys("Ivan")
# #     input2 = browser.find_element_by_name("last_name")
# #     input2.send_keys("Petrov")
# #     input3 = browser.find_element_by_class_name("city")
# #     input3.send_keys("Smolensk")
# #     input4 = browser.find_element_by_id("country")
# #     input4.send_keys("Russia")
# #     button = browser.find_element_by_xpath("//button[text()='Submit']")
# #     button.click()
# #
# # finally:
# #     # успеваем скопировать код за 30 секунд
# #     time.sleep(30)
# #     # закрываем браузер после всех манипуляций
# #     browser.quit()
#
# #не забываем оставить пустую строку в конце файла
#
# from selenium import webdriver
# import time
#
# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/huge_form.html")
#     elements = browser.find_elements_by_tag_name ("input")
#     for element in elements:
#        element.send_keys("Мой ответ")
#
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
# #не забываем оставить пустую строку в конце файла

from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    browser.find_element_by_xpath("//input[@placeholder='Enter first name']").send_keys("zdorov")
    browser.find_element_by_xpath("//input[@placeholder='Enter last name']").send_keys("zdorov")
    browser.find_element_by_xpath("//input[@placeholder='Enter email']").send_keys("zdorov")
    # browser.find_element_by_xpath("//input[@placeholder='Input your last name']").send_keys("zdorov")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    browser.find_element_by_xpath("//input[@type='file']").send_keys(file_path)
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(10)

    # # находим элемент, содержащий текст
    # welcome_text_elt = browser.find_element_by_tag_name("h1")
    # # записываем в переменную welcome_text текст из элемента welcome_text_elt
    # welcome_text = welcome_text_elt.text
    #
    # # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    # assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()