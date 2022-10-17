from selenium.webdriver.common.devtools.v104 import browser
from selenium.webdriver.common.by import By
from base_page import BasePage
from.locators import MainPageLocators

class MainPage(BasePage):
    def go_to_catalogue(self):
        self.browser.find_element(By.XPATH, "//ul[@id='browse']//ul//a")

