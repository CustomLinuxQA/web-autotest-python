import pytest
from selenium import webdriver
import chromedriver_autoinstaller
import geckodriver_autoinstaller
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox

chromedriver_autoinstaller.install()
geckodriver_autoinstaller.install()


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: e.g. '--browser_name=chrome' or '--browser_name=firefox'")

    parser.addoption('--language', action='store', default='en',
                     help="Choose language: e.g. '--language=en' or '--language=ru'")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    options = Options()
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': user_language})

    options_firefox = OptionsFirefox()
    options_firefox.set_preference("intl.accept_languages", user_language)

    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        # options.add_argument("--headless")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(options=options_firefox)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
