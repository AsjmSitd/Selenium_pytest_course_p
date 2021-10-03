from .base_page import BasePage
from .locators import BasePageLocators, LoginPageLocators

link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, f"Login url is not presented, current url is: '{ self.browser.current_url}'"# реализуйте проверку на корректный url адрес
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "Login form is not presented"# реализуйте проверку, что есть форма логина
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "register form is not presented"# реализуйте проверку, что есть форма регистрации на странице
        assert True

    def register_new_user(self, email, password):
        self.input_word(LoginPageLocators.LOGIN_EMAIL, email) #, 'Email area is not defiend'
        self.input_word(LoginPageLocators.LOGIN_PASSWORD, password) #, 'Password area is not defiend'
        self.input_word(LoginPageLocators.LOGIN_PASSWORD_CONFIRM, password) #, 'Password confirm area is not defiend'
        self.click_add_btn(*LoginPageLocators.LOGIN_SUBMIT)
        assert True

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"



