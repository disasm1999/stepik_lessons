# Тестовый сценарий 1.2.1 Вход пользователя

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

main_page_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

search_input_username_locator = "[id='id_login-username']"
search_input_password_locator = "[id='id_login-password']"
search_button_locator = "[name='login_submit']"
result_page_title_locator = "[href='/ru/accounts/']"


def test_user_login():
    # Data
    email = "test@stepik.ru"
    password = "Stepik110521"
    search_text = "Аккаунт"

    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(main_page_link)

        search_input_username = browser.find_element_by_css_selector(search_input_username_locator)
        search_input_password = browser.find_element_by_css_selector(search_input_password_locator)
        search_input_username.clear()  # очищаем поле ввода почты (логина)
        search_input_password.clear()  # очищаем поле ввода пароля

        # Act
        search_input_username.send_keys(email)
        search_input_password.send_keys(password)
        browser.find_element_by_css_selector(search_button_locator).click()

        # Assert
        result_page_title = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, result_page_title_locator))
        )
        assert search_text in result_page_title.text, "Login is fail"

    finally:
        browser.quit()

test_user_login()
