from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    SUCCESS_PRODUCT_NAME = (By.CSS_SELECTOR, '.alert-success:nth-child(1) strong')
    SUCCESS_PRODUCT_PRICE = (By.CSS_SELECTOR, '.alert-info strong')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
