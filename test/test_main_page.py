import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.test_link import MainTestLink


@pytest.mark.login_guest
class TestLoginFromMainPage():
    @pytest.mark.parametrize("test_link", MainTestLink.TEST_LINK)
    def test_guest_can_go_to_login_page(self, browser, test_link):
        page = LoginPage(browser, test_link)
        page.open()
        page.go_to_login_page()
        page.should_be_login_page()  # Проверка нахождения на странице Login or Register.


    @pytest.mark.parametrize("test_link", MainTestLink.TEST_LINK)
    def test_guest_should_see_login_link(self, browser, test_link):
        page = MainPage(browser, test_link)
        page.open()
        page.should_be_login_link()  # Проверка наличия кнопки Login or Register.


@pytest.mark.parametrize("test_link", MainTestLink.TEST_LINK)
@pytest.mark.without_localization
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser, test_link):
    page = MainPage(browser, test_link)
    page.open()
    page.should_be_basket_button()
    page.go_to_basket()
    page.should_be_empty_basket()  # Проверка пустой корзины.
    page.expected_message_basket_is_empty()  # Проверка сообщения "Your basket is empty".
