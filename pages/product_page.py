from .base_page import BasePage
from .locators import ProductPageLocators
from .url import ProductPageUrl
from selenium.common.exceptions import NoAlertPresentException
import pytest
import math


class ProductPage(BasePage):

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def check_promo(self):
        if (ProductPageUrl.THE_SHELLCODERS_HANDBOOK_PROMO_LINK) in self.url:
            print("\npromo detected..")
            self.solve_quiz_and_get_code()
        else:
            print("\ntest without promo ..")

    def should_be_product_url(self):
        current_url = self.browser.current_url
        print(f"{ProductPageUrl.THE_SHELLCODERS_HANDBOOK_ENDPOINT}")
        print(f"{current_url}")
        assert (ProductPageUrl.THE_SHELLCODERS_HANDBOOK_ENDPOINT) in current_url, "AT ERROR! It's not correct item!"

    @pytest.mark.without_localization
    def add_item_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_CART).click()
        self.check_promo()
        notification_add_to_basket = self.browser.find_element(*ProductPageLocators.NOTIFICATION_ADD_TO_BASKET).text
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        assert "has been added to your basket" in notification_add_to_basket, \
            f"AT ERROR! No message - '{item_name} has been added to your basket'"

    def excepted_item_name_in_notification(self):
        self.browser.find_element(*ProductPageLocators.ADD_CART).click()
        self.check_promo()
        notification_item_name = self.browser.find_element(*ProductPageLocators.NOTIFICATION_ITEM_NAME).text
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        assert item_name == notification_item_name, \
            f"AT ERROR! Can't find message '{item_name}' in notification"

    def should_be_total_price_notification(self):
        self.browser.find_element(*ProductPageLocators.ADD_CART).click()
        self.check_promo()
        assert self.is_element_present(*ProductPageLocators.NOTIFICATION_TOTAL_PRICE), \
            "AT ERROR! Notification of total price doesn't exist"

    def excepted_total_price_of_items(self):
        self.browser.find_element(*ProductPageLocators.ADD_CART).click()
        self.check_promo()
        basket_total_price = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_PRICE).text
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        assert str(item_price) in str(basket_total_price), \
            "AT ERROR! Total price in the cart does not match the price of the product"
