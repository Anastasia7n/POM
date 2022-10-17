import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
link = "http://selenium1py.pythonanywhere.com/ru/"

@pytest.fixture(scope='function')

def browser():
    print('\nstart browser...')
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield browser
    print('\nquit browser...')
    browser.quit()


class TestMainPage():

    @pytest.mark.open_page
    def test_1(self, browser):
        browser.get(link)

    @pytest.mark.view_products
    def test_2(self, browser):
        browser.get(link)
        browser.find_element(By.XPATH, "//ul[@id='browse']//ul//a").click()
        time.sleep(3)

