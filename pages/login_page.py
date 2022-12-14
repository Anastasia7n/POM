from .locators import LoginPageLocators
from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_link()
        self.should_be_login_form_link()
        self.should_be_login_form_link()

    def should_be_login_link(self):
        assert 'login' in self.browser.current_url, 'wrong url'

    def should_be_login_form_link(self):
        assert self.element_is_present(*LoginPageLocators.login_form)

    def should_be_register_form(self):
        assert self.element_is_present(*LoginPageLocators.register_form)

    def register_user(self, email='email', password='password'):
        email_input = self.browser.find_element(*LoginPageLocators.register_email)
        email_input.send_keys(email)
        password_input = self.browser.find_element(*LoginPageLocators.reg_password)
        password_input.send_keys(password)
        password_conf_input = self.browser.find_element(*LoginPageLocators.confirm_password)
        password_conf_input.send_keys(password)
        self.browser.find_element(*LoginPageLocators.reg_btn).click()


