from selenium.webdriver.common.by import By


class MainPageLocators():
    catalogue_link = (By.XPATH, "//ul[@id='browse']//ul//a")
    login_btn = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    login_form = (By.CSS_SELECTOR, '#id = login_form')
    register_form = (By.CSS_SELECTOR, '#id = register_form')

