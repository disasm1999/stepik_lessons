#Тестовый сценарий 1.2.1 Вход пользователя

from selenium import webdriver

import time 
#import math

main_page_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

    
search_input_username_locator = "[id='id_login-username']"
search_input_password_locator = "[id='id_login-password']"
search_button_locator = "[name='login_submit']"

def test_item_search():
    # Data
    email = "test@stepik.ru"
    password = "Stepik110521"
    search_text = "Рады видеть вас снова"

    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(main_page_link)
    
        search_input_username = browser.find_element_by_css_selector(search_input_username_locator)
        search_input_password = browser.find_element_by_css_selector(search_input_password_locator)
        search_input_username.clear()
        search_input_password.clear()
    
        # Act
        search_input_username.send_keys(email)
        search_input_password.send_keys(password)
        browser.find_element_by_css_selector(search_button_locator).click()
    
        # Assert
        result_page_title = browser.find_element_by_css_selector(result_page_title_locator)
        assert search_text in search_title.text, "Login is correct"


    finally:
        time.sleep(10)
        browser.quit()

test_item_search()    
# не забываем оставить пустую строку в конце файла
