from .base_page import BasePage
from .locators import ProductPageLocators
from .url_rout import ProductPageUrl
from .url_rout import ProductBugPageUrl    # BUG TUSK lesson3_step4.
from .locators import TestList
from selenium.common.exceptions import NoAlertPresentException
import math
import allure
from allure_commons.types import AttachmentType


class ProductPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(ProductPage, self).__init__(*args, **kwargs)

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
        if (ProductPageUrl.PROMO_URL) in self.url:
            print("\nAT! Promo detected ..")
            self.solve_quiz_and_get_code()
        elif (ProductBugPageUrl.PROMO_URL) in self.url:    # BUG TUSK lesson3_step4.
            print("\nAT! Promo detected ..")
            self.solve_quiz_and_get_code()
        else:
            print("\nAT! Test without promo ..")

    @allure.story('Проверка аллюр стори')
    @allure.severity('critical')
    def add_item_to_basket(self):    # @pytest.mark.without_localization
        self.browser.find_element(*ProductPageLocators.ADD_CART).click()
        self.check_promo()
        notification_add_to_basket = self.browser.find_element(*ProductPageLocators.NOTIFICATION_ADD_TO_BASKET).text
        with allure.step('Делаем скриншот'):
            allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        assert notification_add_to_basket in TestList.TEXT_NOTIFICATION_IN_BASKET, \
            f"AT ERROR! Expected - '{notification_add_to_basket}', actual result - '{notification_add_to_basket}'."

    def expected_item_name_in_notification(self):
        self.browser.find_element(*ProductPageLocators.ADD_CART).click()
        self.check_promo()
        notification_item_name = self.browser.find_element(*ProductPageLocators.NOTIFICATION_ITEM_NAME).text
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        assert item_name == notification_item_name, \
            f"AT ERROR! Expected - '{item_name}', actual result - '{notification_item_name}'."

    def expected_total_price_of_items(self):
        self.browser.find_element(*ProductPageLocators.ADD_CART).click()
        self.check_promo()
        basket_total_price = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_PRICE).text
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        assert str(item_price) in str(basket_total_price), \
            f"AT ERROR! Expected - '{item_price}', actual result - '{basket_total_price}'."

    def should_be_product_url(self):  # Ужасная проверка. Нужно подумать ещё.
        current_url = self.browser.current_url
        assert "catalogue" in current_url, \
            "AT ERROR! It's not correct item!"
        f"AT ERROR! Expected - 'catalogue' in '{current_url}'."

    def should_be_correct_total_price_notification(self):
        self.browser.find_element(*ProductPageLocators.ADD_CART).click()
        self.check_promo()
        notification_item_price = self.browser.find_element(*ProductPageLocators.NOTIFICATION_TOTAL_PRICE).text  #
        basket_total_price = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_PRICE).text
        assert str(notification_item_price) in str(basket_total_price), \
            f"AT ERROR! Expected - '{notification_item_price}', actual result - '{basket_total_price}'."

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.NOTIFICATION_SUCCESS_MESSAGE), \
            "Notification success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.NOTIFICATION_SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
