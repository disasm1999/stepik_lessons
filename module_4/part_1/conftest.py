import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

ALLOWED_LANGUAGES = ('ru', 'en-gb', 'es', 'fr', )

def pytest_addoption(parser):
    parser.addoption(
        '--language', action='store',
        choices=ALLOWED_LANGUAGES, default='ru', help="Choose language: ru or en-gb or es or fr",
    )

@pytest.fixture(scope="session")
def user_language(request):
    return request.config.getoption("language")

@pytest.fixture(scope="session")
def options(request, user_language):
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    return options

@pytest.fixture(scope="session")
def browser(options):
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
