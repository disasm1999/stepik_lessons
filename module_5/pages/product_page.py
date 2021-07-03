from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket.click()

    def should_be_add_to_basket(self):
        self.should_be_message()
        self.should_be_right_price()

    def should_be_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def should_be_success_product_price(self):
        return self.browser.find_element(*ProductPageLocators.SUCCESS_PRODUCT_PRICE).text

    def should_be_success_product_name(self):
        return self.browser.find_element(*ProductPageLocators.SUCCESS_PRODUCT_NAME).text

    def is_success_name_correct(self):
        assert self.should_be_product_name() == self.should_be_success_product_name(), \
            'The names of the added product differs from the names of the product'

    def is_success_price_correct(self):
        self.should_be_product_price() == self.should_be_success_product_price(), \
        'The price of the added product differs from the price of the product'

    def should_be_success(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_PRODUCT_NAME), \
            "Message of Success added product in "

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_PRODUCT_NAME), \
            "Success message is presented, but should not be"

    def should_not_be_success_product_name(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_PRODUCT_NAME), \
            "Success message is presented, but should not be"

    def should_disappear_success_product_name(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_PRODUCT_NAME), \
            "Success message is presented, but should disappear"

    def should_be_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def should_be_success_product_price(self):
        return self.browser.find_element(*ProductPageLocators.SUCCESS_PRODUCT_PRICE).text

    def should_be_success_product_name(self):
        return self.browser.find_element(*ProductPageLocators.SUCCESS_PRODUCT_NAME).text

    def is_success_name_correct(self):
        assert self.should_be_product_name() == self.should_be_success_product_name(), \
            'The names of the added product differs from the names of the product'

    def is_success_price_correct(self):
        self.should_be_product_price() == self.should_be_success_product_price(), \
        'The price of the added product differs from the price of the product'
