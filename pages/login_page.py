import time
from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators
from dotenv import load_dotenv
from os import getenv

load_dotenv()
AUTH_EMAIL = getenv('AUTH__EMAIL')
AUTH_PASSWORD = getenv('AUTH__PASSWORD')


class LoginPage(BasePage):

    def delete_user(self):
        self.go_to_account_page()
        self.browser.find_element(*LoginPageLocators.DELETE_PROFILE_BUTTON).click()
        self.browser.find_element(*LoginPageLocators.DELETE_PASS_INPUT).send_keys("11111111Q")
        self.browser.find_element(*LoginPageLocators.DELETE_PROFILE_BUTTON_CONFIRM).click()

    def email_gen(self):
        email = str(time.time()) + "@fakemail.org"
        return email

    def login_user(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL_INPUT).send_keys(AUTH_EMAIL)
        self.browser.find_element(*LoginPageLocators.LOGIN_PASS_INPUT).send_keys(AUTH_PASSWORD)
        self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    def registration_user(self):
        email = self.email_gen()
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_INPUT).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASS_INPUT).send_keys("11111111Q")
        self.browser.find_element(*LoginPageLocators.REGISTER_PASS_CONFIRM_INPUT).send_keys("11111111Q")
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        self.is_element_present(*BasePageLocators.LOGIN_LINK), "AT ERROR! Login link is not presented"
        current_url = self.browser.current_url
        assert "/accounts/login/" in current_url, "AT ERROR! It's not login link!"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "AT ERROR! Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "AT ERROR! Register form is not presented"

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def should_not_be_authorized_user(self):
        assert self.is_not_element_present(*BasePageLocators.USER_ICON), "User icon is presented," \
                                                                     " probably authorised user"
