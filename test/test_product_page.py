import pytest
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.test_link import ProductTestLink
from pages.test_link import ProductBugTestLink


@pytest.mark.guest
class TestGuestFromProductPage():
    @pytest.mark.parametrize("test_link", ProductTestLink.TEST_LINK)
    def test_guest_can_open_product_page(self, browser, test_link):
        page = ProductPage(browser, test_link)
        page.open()
        page.should_be_product_url()  # проверка url


    @pytest.mark.parametrize("test_link", ProductTestLink.TEST_LINK)
    @pytest.mark.without_localization
    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser, test_link):
        page = ProductPage(browser, test_link)
        page.open()
        page.add_item_to_basket()  # Проверка добавления товара в корзину.


    @pytest.mark.parametrize("test_link", ProductTestLink.TEST_LINK)
    def test_guest_can_see_added_item_in_notification(sekf, browser, test_link):
        page = ProductPage(browser, test_link)
        page.open()
        page.excepted_item_name_in_notification()  # Проверка соответствия названия товара в уведомлении.


    @pytest.mark.parametrize("test_link", ProductBugTestLink.TEST_LINK)
    @pytest.mark.bug_task
    @pytest.mark.xfail
    def test_guest_can_see_added_item_in_notification(sekf, browser, test_link):
        page = ProductPage(browser, test_link)
        page.open()
        page.excepted_item_name_in_notification()  # Проверка соответствия названия товара в уведомлении.


    @pytest.mark.parametrize("test_link", ProductTestLink.TEST_LINK)
    def test_guest_can_see_total_price_in_notification(sekf, browser, test_link):
        page = ProductPage(browser, test_link)
        page.open()
        page.should_be_correct_total_price_notification()  # Проверка соответствия цены товара в уведомлении.


    @pytest.mark.parametrize("test_link", ProductTestLink.TEST_LINK)
    def test_guest_can_see_total_price_of_items(sekf, browser, test_link):
        page = ProductPage(browser, test_link)
        page.open()
        page.excepted_total_price_of_items()  # Стоимость корзины совпадает с ценой товара.


    @pytest.mark.parametrize("test_link", ProductTestLink.TEST_LINK)
    @pytest.mark.without_localization
    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(sekf, browser, test_link):
        page = ProductPage(browser, test_link)
        page.open()
        page.add_item_to_basket()
        page.should_not_be_success_message()  # Проверка отсутствия успешного добавления товара.


    @pytest.mark.parametrize("test_link", ProductTestLink.TEST_LINK)
    def test_guest_cant_see_success_message(sekf, browser, test_link):
        page = ProductPage(browser, test_link)
        page.open()
        page.should_not_be_success_message()  # Проверка отсутствия успешного добавления товара.


    @pytest.mark.parametrize("test_link", ProductTestLink.TEST_LINK)
    @pytest.mark.without_localization
    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(sekf, browser, test_link):
        page = ProductPage(browser, test_link)
        page.open()
        page.add_item_to_basket()
        page.should_be_disappeared()  # Проверка исчезновения элемента.


    @pytest.mark.parametrize("test_link", ProductTestLink.TEST_LINK)
    def test_guest_should_see_login_link_on_product_page(sekf, browser, test_link):
        page = ProductPage(browser, test_link)
        page.open()
        page.should_be_login_link()  # Проверка наличия кнопки Login or Register.


    @pytest.mark.parametrize("test_link", ProductTestLink.TEST_LINK)
    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(sekf, browser, test_link):
        page = LoginPage(browser, test_link)
        page.open()
        page.go_to_login_page()
        page.should_be_login_page()  # Проверка нахождения на странице Login or Register.


    @pytest.mark.parametrize("test_link", ProductTestLink.TEST_LINK)
    @pytest.mark.without_localization
    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(sekf, browser, test_link):
        page = MainPage(browser, test_link)
        page.open()
        page.go_to_basket()
        page.should_be_empty_basket()  # Проверка пустой корзины.
        page.excepted_message_basket_is_empty()  # Проверка сообщения "Your basket is empty".


@pytest.mark.login
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function")
    def setup(self, browser, test_link):
        page = LoginPage(browser, test_link)
        page.open()
        page.go_to_login_page()
        page.registration_user()
        page.should_be_authorized_user()
        yield
        page.delete_user()
        page.should_not_be_authorized_user()

    @pytest.mark.parametrize("test_link", ProductTestLink.TEST_LINK)
    @pytest.mark.need_review
    @pytest.mark.without_localization
    def test_user_can_add_product_to_basket(self, setup, browser, test_link):
        page = ProductPage(browser, test_link)
        page.open()
        page.add_item_to_basket()  # Проверка добавления товара в корзину.
