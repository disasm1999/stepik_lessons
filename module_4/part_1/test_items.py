import pytest
from selenium import webdriver

language_opt = [
    ("ru", "Добавить в корзину",),
    ("en-GB", "Add to basket",),
    ("es", "Añadir al carrito",),
    ("fr", "Ajouter au panier",),
]

ids = [i[0] for i in language_opt]


@pytest.mark.parametrize( "language, wait", language_opt, ids=ids )
def test_add_to_cart_button(language, wait, browser: webdriver.Chrome, user_language):
    if language != user_language:
        pytest.skip( f"skip {language} language" )
    browser.get( "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/" )
    get = browser.find_element_by_css_selector( ".btn-add-to-basket" ).text
    assert wait == get, f"wait '{wait}', get '{get}'"
