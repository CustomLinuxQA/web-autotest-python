import pytest
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.test_link import ProductTestLink
from pages.test_link import ProductBugTestLink


@pytest.mark.guest
class TestGuestFromProductPage():
    @pytest.mark.production
    @pytest.mark.parametrize("test_link", ProductTestLink.TEST_LINK)
    def test_guest_can_open_product_page(self, browser, test_link):
        """
        В тесте неавторизованный пользователь может открыть продуктовую страницу.
        """
        page = ProductPage(browser, test_link)
        page.open()
        page.should_be_product_url() # Проверка нахождения на продуктовой странице.

    @pytest.mark.production
    @pytest.mark.parametrize("test_link", ProductTestLink.TEST_LINK)
    def test_guest_can_add_product_to_basket(self, browser, test_link):
        """
        Неавторизованный пользователь может добавить товар в корзину.
        """
        page = ProductPage(browser, test_link)
        page.open()
        page.add_item_to_basket()  # Проверка добавления товара в корзину.

    @pytest.mark.production
    @pytest.mark.parametrize("test_link", ProductTestLink.TEST_LINK)
    def test_guest_can_see_added_item_in_notification(self, browser, test_link):
        """
        В тесте неавторизованный пользователь может видеть уведомление об успешном добавлении товара.
        """
        page = ProductPage(browser, test_link)
        page.open()
        page.expected_item_name_in_notification()  # Проверка соответствия названия товара в уведомлении.

    @pytest.mark.xfail  # проверка работоспособности xfail.
    @pytest.mark.bug_task
    @pytest.mark.parametrize("test_link", ProductBugTestLink.TEST_LINK)
    def test_guest_can_see_added_item_in_notification(self, browser, test_link):
        """
        В тесте неавторизованный пользователь может видеть уведомление об успешном добавлении товара.
        """
        page = ProductPage(browser, test_link)
        page.open()
        page.expected_item_name_in_notification()  # Проверка соответствия названия товара в уведомлении.

    @pytest.mark.production
    @pytest.mark.parametrize("test_link", ProductTestLink.TEST_LINK)
    def test_guest_can_see_total_price_in_notification(self, browser, test_link):
        """
        В тесте неавторизованный пользователь может видеть уведомление итоговой суммы корзины.
        """
        page = ProductPage(browser, test_link)
        page.open()
        page.should_be_correct_total_price_notification()  # Проверка соответствия цены товара в уведомлении.

    @pytest.mark.production
    @pytest.mark.parametrize("test_link", ProductTestLink.TEST_LINK)
    def test_guest_can_see_total_price_of_items(self, browser, test_link):
        """
        В тесте неавторизованный пользователь может видеть итоговую сумму корзины.
        """
        page = ProductPage(browser, test_link)
        page.open()
        page.expected_total_price_of_items()  # Стоимость корзины совпадает с ценой товара.

    @pytest.mark.xfail  # проверка работоспособности xfail.
    @pytest.mark.production
    @pytest.mark.parametrize("test_link", ProductTestLink.TEST_LINK)
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser, test_link):
        """
        В тесте неавторизованный пользователь не может видеть уведомление об успешном добавлении товара.
        """
        page = ProductPage(browser, test_link)
        page.open()
        page.add_item_to_basket()
        page.should_not_be_success_message()  # Проверка отсутствия успешного добавления товара.

    @pytest.mark.production
    @pytest.mark.parametrize("test_link", ProductTestLink.TEST_LINK)
    def test_guest_cant_see_success_message(self, browser, test_link):
        """
        Тест на проверку отсутствия уведомления об успешном добавлении товара без нажатия Add to basket.
        """
        page = ProductPage(browser, test_link)
        page.open()
        page.should_not_be_success_message()  # Проверка отсутствия успешного добавления товара.

    @pytest.mark.xfail
    @pytest.mark.production
    @pytest.mark.parametrize("test_link", ProductTestLink.TEST_LINK)
    def test_message_disappeared_after_adding_product_to_basket(self, browser, test_link):
        """
        Сообщение об успешном добавлении товара в корзину исчезнет в течении 4-секунд.
        """
        page = ProductPage(browser, test_link)
        page.open()
        page.add_item_to_basket()
        page.should_be_disappeared()  # Проверка исчезновения элемента.

    @pytest.mark.production
    @pytest.mark.parametrize("test_link", ProductTestLink.TEST_LINK)
    def test_guest_should_see_login_link_on_product_page(self, browser, test_link):
        """
        Неавторизованный пользователь может видеть ссылку на "Login or register".
        """
        page = ProductPage(browser, test_link)
        page.open()
        page.should_be_login_link()  # Проверка наличия кнопки Login or Register.

    @pytest.mark.production
    @pytest.mark.parametrize("test_link", ProductTestLink.TEST_LINK)
    def test_guest_can_go_to_login_page_from_product_page(self, browser, test_link):
        """
        Неавторизованный пользователь может перейти по ссылке на "Login or register".
        """
        page = LoginPage(browser, test_link)
        page.open()
        page.go_to_login_page()
        page.should_be_login_page()  # Проверка нахождения на странице Login or Register.

    @pytest.mark.production
    @pytest.mark.parametrize("test_link", ProductTestLink.TEST_LINK)
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser, test_link):
        """
        Неавторизованный пользователь не может видеть товары в пустой корзине.
        """
        page = MainPage(browser, test_link)
        page.open()
        page.go_to_basket()
        page.should_be_empty_basket()  # Проверка пустой корзины.
        page.expected_message_basket_is_empty()  # Проверка сообщения "Your basket is empty".


@pytest.mark.login
class TestUserAddToBasketFromProductPage():
    @pytest.mark.setup
    @pytest.fixture(scope="function")
    def setup(self, browser, test_link):
        """
        Setup генерация новых пользователей перед каждым тестом с финальным удалением пользователей.
        """
        page = LoginPage(browser, test_link)
        page.open()
        page.go_to_login_page()
        page.registration_user()
        page.should_be_authorized_user()
        yield
        page.delete_user()
        page.should_not_be_authorized_user()

    @pytest.mark.production
    @pytest.mark.parametrize("test_link", ProductTestLink.TEST_LINK)
    def test_user_can_add_product_to_basket(self, setup, browser, test_link):
        """
        Авторизованный пользователь может добавить товар в корзину.
        """
        page = ProductPage(browser, test_link)
        page.open()
        page.add_item_to_basket()  # Проверка добавления товара в корзину.
