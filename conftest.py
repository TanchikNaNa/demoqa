import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as OptionsChrome
import time

@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    time.sleep(10)
    browser.quit()

