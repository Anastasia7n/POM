from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .base_page import BasePage


class MainPage(BasePage):

    def should_view_products(self):
        assert self.element_is_present(*MainPageLocators.catalogue_link)

    def go_to_catalogue(self):
        self.browser.find_element(*MainPageLocators.catalogue_link).click()



