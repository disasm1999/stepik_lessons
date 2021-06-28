import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

ALLOWED_LANGUAGES = ('ru', 'en-GB', 'es', 'fr', )

def pytest_addoption(parser):
    parser.addoption(
        '--language', action='store',
        choices=ALLOWED_LANGUAGES, default='en-GB', help="Choose language: ru or en-GB or es or fr",
    )
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")

@pytest.fixture(scope="session")
def user_language(request):
    return request.config.getoption("language")

@pytest.fixture(scope="session")
def options(request, user_language):
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    return options

@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
