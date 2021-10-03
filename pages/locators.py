from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BTN = (By.XPATH, '//*[@id="default"]/header//div/span/a[contains(text(), "")]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    BOOK_NAME = (By.XPATH, '//*[@id="content_inner"]/article//div/h1')
    BOOK_PRICE = (By.XPATH, '//*[@id="content_inner"]/article/div/div[2]/p[1]')
    BOOK_ADDED_MSG = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    BOOK_ADD_MSG = (By.XPATH, '//*[@id="messages"]/div[1]/div[contains(., "")]')
    BOOK_PRICE_MSG = (By.XPATH, '//*[@id="messages"]//div/p[1][contains(text(), "")]')
    TOTAL_PRICE = (By.XPATH, '//*[@id="messages"]//div/p/strong')


class LoginPageLocators():
    LOGIN_SUBMIT = (By.CSS_SELECTOR, '[name = "registration_submit"]')
    LOGIN_LINK = (By.ID, 'login_link')
    LOGIN_EMAIL = (By.ID, 'id_registration-email')
    LOGIN_PASSWORD = (By.ID, 'id_registration-password1')
    LOGIN_PASSWORD_CONFIRM = (By.ID, 'id_registration-password2')
    REGISTER_FORM = (By.ID, 'register_form')

class BasketPageLocators():
    BASKET_MSG = (By.CSS_SELECTOR, '#content_inner')
    BASKET_CONENT = (By.CSS_SELECTOR, '.basket_summary')



