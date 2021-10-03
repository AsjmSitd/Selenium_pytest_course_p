from .base_page import BasePage
from .locators import ProductPageLocators, BasePageLocators


class ProductPage(BasePage):
    def shoul_click_add_to_basket_btn(self):
        self.click_add_btn(*ProductPageLocators.ADD_TO_BASKET)
        assert True

    def check_book_name(self):
        assert self.is_element_present(*ProductPageLocators.BOOK_NAME), "Element is not present"
        assert True

    def check_book_price(self):
        assert self.is_element_present(*ProductPageLocators.BOOK_PRICE), "Element is not present"
        assert True

    def check_msg1(self):
        assert self.is_element_present(*ProductPageLocators.BOOK_ADD_MSG), "Element is not present"
        assert True

    def check_msg2(self):
        assert self.is_element_present(*ProductPageLocators.BOOK_PRICE_MSG), "Element is not present"
        assert True

    def check_equvalent(self):
        self.is_equal(ProductPageLocators.BOOK_NAME, ProductPageLocators.BOOK_ADDED_MSG)

    def check_equvalent_of_price(self):
        self.is_equal(ProductPageLocators.BOOK_PRICE, ProductPageLocators.TOTAL_PRICE)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.BOOK_ADD_MSG), \
            "Success message is presented, but should not be"

    def should_not_be_success_message_1(self):
        assert self.is_disappeared(*ProductPageLocators.BOOK_ADD_MSG), \
            "Success message is presented, but should not be"

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "URL is not present"

    def should_click_to_login_link(self):
        self.click_add_btn(*BasePageLocators.LOGIN_LINK)

