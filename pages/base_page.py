from selenium.common.exceptions import NoSuchFrameException
from.locators import BasePageLocators

class BasePage():

    def __init__(self, browser, link):
        self.browser = browser
        self.link = link

    def open_page(self):
        self.browser.get(self.link)

    def element_is_present(self, method, locator):
        try:
            self.browser.find_element(method, locator)
        except NoSuchFrameException:
            return False
        return True

    def should_be_authorised_user(self):
        assert self.element_is_present(*BasePageLocators.user_icon)