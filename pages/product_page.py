from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_product_url(self):
        current_url = self.browser.current_url
        assert "the-shellcoders-handbook" in current_url, "AT ERROR! It's not correct item!"

    def add_item_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_CART).click()
        text_notification = self.browser.find_element(*ProductPageLocators.NOTIFICATION_ADD_TO_BASKET).text
        assert "has been added to your basket" in text_notification, \
            "AT ERROR! No message '{ITEM} has been added to your basket'"

    def excepted_item_name_in_notification(self):
        self.browser.find_element(*ProductPageLocators.ADD_CART).click()
        notification_item_name = self.browser.find_element(*ProductPageLocators.NOTIFICATION_ITEM_NAME).text
        product_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        assert product_name == notification_item_name, \
            f"AT ERROR! Can't find message '{product_name}' in notification"


    def should_be_total_price_notification(self):
        self.browser.find_element(*ProductPageLocators.ADD_CART).click()
        assert self.is_element_present(*ProductPageLocators.NOTIFICATION_TOTAL_PRICE), \
            "AT ERROR! Notification of total price doesn't exist"


    def excepted_total_price_of_items(self):
        self.browser.find_element(*ProductPageLocators.ADD_CART).click()
        basket_total_price = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_PRICE).text
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        assert str(item_price) in str(basket_total_price), \
            "AT ERROR! Total price in the cart does not match the price of the product"
