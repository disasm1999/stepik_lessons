from .pages.product_page import ProductPage
import pytest

@pytest.mark.parametrize('promo_offer',
["offer0","offer1","offer2","offer3","offer4","offer5","offer6","offer7","offer8","offer9"])

def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?"
    page = ProductPage(browser, link+promo_offer)
    page.open()
    page.add_product_to_basket()
#    page.solve_quiz_and_get_code()
    page.should_be_book_name()
    page.should_be_book_price()
    page.should_be_success_book_name()
    page.should_be_success_book_price()
    page.is_success_name_correct()
    page.is_success_price_correct() 


