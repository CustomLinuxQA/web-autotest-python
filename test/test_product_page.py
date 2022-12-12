from pages.product_page import ProductPage
from pages.url import ProductPageUrl


def test_guest_can_open_product_page(browser):
    link = (ProductPageUrl.THE_SHELLCODERS_HANDBOOK_LINK)
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()  # открываем страницу
    page.should_be_product_url()  # проверка url


def test_guest_can_add_product_to_basket(browser):
    link = (ProductPageUrl.THE_SHELLCODERS_HANDBOOK_LINK)
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_basket()  # Проверка добавления товара в корзину.


def test_guest_can_see_added_item_in_notification(browser):
    link = (ProductPageUrl.THE_SHELLCODERS_HANDBOOK_LINK)
    page = ProductPage(browser, link)
    page.open()
    page.excepted_item_name_in_notification()  # Проверка соответствия названия товара в уведомлении.


def test_guest_can_see_total_price_in_notification(browser):
    link = (ProductPageUrl.THE_SHELLCODERS_HANDBOOK_LINK)
    page = ProductPage(browser, link)
    page.open()
    page.should_be_total_price_notification()  # Проверка соответствия цены товара в уведомлении.

def test_guest_can_see_total_price_of_items(browser):
    link = (ProductPageUrl.THE_SHELLCODERS_HANDBOOK_LINK)
    page = ProductPage(browser, link)
    page.open()
    page.excepted_total_price_of_items()  # Стоимость корзины совпадает с ценой товара.
