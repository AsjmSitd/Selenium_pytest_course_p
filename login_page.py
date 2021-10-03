from .base_page import BasePage
from .locators import LoginPageLocators

link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
class LoginPage(BasePage):
    def should_be_login_page(self, b):
        self.should_be_login_url(b)
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self, b):
        assert b.current_url==link, f"Login url is not presented, current url is: '{b.current_url}'"# реализуйте проверку на корректный url адрес
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "Login form is not presented"# реализуйте проверку, что есть форма логина
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "register form is not presented"# реализуйте проверку, что есть форма регистрации на странице
        assert True



