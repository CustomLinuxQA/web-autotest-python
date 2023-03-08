from .base_page import BasePage
from .locators import BasePageLocators
from .locators import BasketPageLocators


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def expected_message_basket_is_empty(self):    # @pytest.mark.without_localization
        message_basket_is_empty = self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY_LOCATOR).text
        assert "Your basket is empty" in message_basket_is_empty, \
            "AT ERROR! Basket is not empty or language is not en-gb"

    def should_be_basket_button(self):
        assert self.is_element_present(*BasePageLocators.BASKET_LOCATOR), "AT ERROR! Basket is not presented"

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.CHECKOUT_LOCATOR), "AT ERROR! Basket is not empty!"
