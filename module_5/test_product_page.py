from .pages.product_page import ProductPage
#from .pages.basket_page import BasketPage

#pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"])
def test_guest_can_add_product_to_basket(browser):
#def test_guest_can_add_product_to_basket(browser, link):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_book_name()
    page.should_be_book_price()
    page.should_be_success_book_name()
    page.should_be_success_book_price()
    page.is_success_name_correct()
    page.is_success_price_correct() 
#    page.should_be_add_to_basket()

