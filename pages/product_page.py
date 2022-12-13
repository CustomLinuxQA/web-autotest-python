from .base_page import BasePage
from .locators import ProductPageLocators
from .url_rout import ProductPageUrl
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
        if (ProductPageUrl.PROMO_BUG_URL) in self.url:
            print("\npromo detected..")
            self.solve_quiz_and_get_code()
        else:
            print("\ntest without promo ..")

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
        print(notification_item_name)
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        print(item_name)
        assert item_name == notification_item_name, \
            f"AT ERROR! Can't find message '{item_name}' in notification"

    def excepted_total_price_of_items(self):
        self.browser.find_element(*ProductPageLocators.ADD_CART).click()
        self.check_promo()
        basket_total_price = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_PRICE).text
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        assert str(item_price) in str(basket_total_price), \
            "AT ERROR! Total price in the cart does not match the price of the product"

    def should_be_product_url(self):  # Ужасная проверка. Нужно подумать ещё.
        current_url = self.browser.current_url
        assert "catalogue" in current_url, "AT ERROR! It's not correct item!"

    def should_be_correct_total_price_notification(self):
        self.browser.find_element(*ProductPageLocators.ADD_CART).click()
        self.check_promo()
        notification_item_price = self.browser.find_element(*ProductPageLocators.NOTIFICATION_TOTAL_PRICE).text  #
        basket_total_price = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_PRICE).text
        assert str(notification_item_price) in str(basket_total_price), \
            "AT ERROR! Notification of total price is not equal to the price in the cart"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.NOTIFICATION_SUCCESS_MESSAGE), \
            "Notification success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.NOTIFICATION_SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
