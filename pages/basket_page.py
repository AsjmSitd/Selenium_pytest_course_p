from .base_page import BasePage
from .locators import BasketPageLocators
from .locators import BasePageLocators


class BasketPage(BasePage):
    def go_to_basket(self):
        self.click_add_btn(*BasePageLocators.BASKET_BTN)

    def should_be_msg(self):
        self.msg_is_present(BasketPageLocators.BASKET_MSG, "")

    def should_not_present(self):
        self.is_not_element_present(*BasketPageLocators.BASKET_CONENT)