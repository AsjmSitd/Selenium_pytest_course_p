from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_SUBMIT = (By.CSS_SELECTOR, '[name = "registration_submit"]')
    LOGIN_LINK = (By.ID, 'login_link')
    LOGIN_EMAIL = (By.ID, 'id_registration-email')
    LOGIN_PASSWORD = (By.ID, 'id_registration-password1')
    LOGIN_PASSWORD_CONFIRM = (By.ID, 'id_registration-password2')
    REGISTER_FORM = (By.ID, 'register_form')