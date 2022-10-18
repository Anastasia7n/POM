import confirm as confirm
import reg as reg
from selenium.webdriver.common.by import By


class MainPageLocators():
    catalogue_link = (By.XPATH, "//ul[@id='browse']//ul//a")
    login_btn = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    login_form = (By.CSS_SELECTOR, '#login_form')
    register_form = (By.CSS_SELECTOR, '#register_form')
    register_email = (By.CSS_SELECTOR, '#id_registration-email')
    reg_password = (By.CSS_SELECTOR, '#id_registration-password1')
    confirm_password = (By.CSS_SELECTOR,'#id_registration-password2')
    reg_btn = (By.XPATH, '//form[@id="register_form"]//button')

class BasePageLocators():
    user_icon = (By.CSS_SELECTOR, '.icon-user')
