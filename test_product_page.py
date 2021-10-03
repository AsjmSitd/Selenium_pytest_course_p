import time

import pytest

from .pages.basket_page import BasketPage
from .pages.base_page import BasePage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.locators import BasePageLocators
from .pages.main_page import MainPage

@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                 pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)
    page.open()
    pp = ProductPage(browser, browser.current_url)
    pp.should_not_be_success_message()
    pp.shoul_click_add_to_basket_btn()
    #page.solve_quiz_and_get_code()
    pp.check_book_name()
    pp.check_book_price()
    pp.check_msg1()
    pp.check_msg2()
    pp.check_equvalent()
    pp.check_equvalent_of_price()
    time.sleep(1)


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_click_to_login_link()


@pytest.mark.need_reviewr
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    bp = BasketPage(browser, link)
    bp.go_to_basket()
    bp.should_not_present()
    bp.should_be_msg()



@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)
    page.open()
    pp = ProductPage(browser, browser.current_url)
    pp.shoul_click_add_to_basket_btn()
    pp.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)
    page.open()
    pp = ProductPage(browser, browser.current_url)
    pp.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)
    page.open()
    pp = ProductPage(browser, browser.current_url)
    pp.shoul_click_add_to_basket_btn()
    pp.should_not_be_success_message_1()
    
    
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function")
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = MainPage(browser, link)
        page.open()
        lp = LoginPage(browser, browser.current_url)
        lp.register_new_user(email=str(time.time()) + "@fakemail.org", password=str(time.time()) + "hi")
        lp.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser, setup):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = MainPage(browser, link)
        page.open()
        pp = ProductPage(browser, browser.current_url)
        pp.should_not_be_success_message()
        pp.shoul_click_add_to_basket_btn()
        pp.check_book_name()
        pp.check_book_price()
        pp.check_msg1()
        pp.check_msg2()
        pp.check_equvalent()
        pp.check_equvalent_of_price()
        time.sleep(1)

    def test_user_cant_see_success_message(self, browser, setup):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = MainPage(browser, link)
        page.open()
        pp = ProductPage(browser, browser.current_url)
        pp.should_not_be_success_message()

