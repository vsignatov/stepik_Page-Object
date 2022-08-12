import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import base

# Ввод в консоли сокращенного наименования языка
 
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help="Choose lang") 
 
#запуск браузера с добавлением параметра языка 
@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    print("\nstart browser for test..")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.fixture(scope="function")
 def setup (request):
    user_language = request.config.getoption("language")
    print("\nstart browser for test..")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options) 
    
