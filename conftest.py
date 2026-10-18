import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    options = webdriver.FirefoxOptions()
    browser = webdriver.Firefox(options=options)
    try:
        browser.maximize_window()
    except Exception:
        pass
    yield browser
    try:
        browser.quit()
    except Exception:
        pass