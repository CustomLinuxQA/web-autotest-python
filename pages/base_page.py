import allure
from allure_commons.types import AttachmentType
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators


class BasePage():
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)
        with allure.step('Method Open'):
            allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)

    def is_element_present(self, how, what):  # how (CSS/ID/XPATH) what (Selector)
        try:
            self.browser.find_element(how, what)
            with allure.step('Method is_element_present'):
                allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot',
                              attachment_type=AttachmentType.PNG)
        except (NoSuchElementException):
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
            with allure.step('Method is_not_element_present'):
                allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot',
                              attachment_type=AttachmentType.PNG)
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
            with allure.step('Method is_disappeared'):
                allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot',
                              attachment_type=AttachmentType.PNG)
        except TimeoutException:
            return False

        return True

    def go_to_login_page(self):
        self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()
        with allure.step('Method go_to_login_page'):
            allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)

    def go_to_account_page(self):
        self.browser.find_element(*BasePageLocators.USER_ICON).click()
        with allure.step('Method go_to_account_page'):
            allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)

    def go_to_basket(self):
        self.browser.find_element(*BasePageLocators.BASKET_LOCATOR).click()
        with allure.step('Method go_to_basket'):
            allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "AT ERROR! Login link is not presented"
        with allure.step('Method should_be_login_link'):
            allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
