from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.go_to_login_page()
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def go_to_login_page(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_LINK).click()

    def should_be_login_url(self):
        self.is_element_present(*LoginPageLocators.LOGIN_LINK), "AT ERROR! Login link is not presented"
        current_url = self.browser.current_url
        assert "/accounts/login/" in current_url, "AT ERROR! It's not login link!"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "AT ERROR! Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "AT ERROR! Register form is not presented"
