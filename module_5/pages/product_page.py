from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket.click()

    def should_be_add_to_basket(self):
        self.should_be_message()
        self.should_be_right_price()

    def should_be_book_price(self):
        return self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text

    def should_be_book_name(self):
        return self.browser.find_element(*ProductPageLocators.BOOK_NAME).text

    def should_be_success_book_price(self):
        return self.browser.find_element(*ProductPageLocators.SUCCESS_BOOK_PRICE).text

    def should_be_success_book_name(self):
        return self.browser.find_element(*ProductPageLocators.SUCCESS_BOOK_NAME).text
    
    def is_success_name_correct(self):
        assert self.should_be_book_name() == self.should_be_success_book_name(), \
            'The names of the added product differs from the names of the product'
    
    def is_success_price_correct(self):
        self.should_be_book_price() == self.should_be_success_book_price(), \
            'The price of the added product differs from the price of the product' 