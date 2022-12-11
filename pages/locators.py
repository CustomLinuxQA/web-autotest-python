from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators():
    ADD_CART = (By.CSS_SELECTOR, "#add_to_basket_form")
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, ".basket-mini")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
    NOTIFICATION_ADD_TO_BASKET = (By.CSS_SELECTOR, "div[id='messages'] div:nth-child(1) div")
    NOTIFICATION_ITEM_NAME = (By.CSS_SELECTOR, "div[id='messages'] div:nth-child(1) strong")
    NOTIFICATION_TOTAL_PRICE = (By.CSS_SELECTOR, "div[id='messages'] div:nth-child(3) strong")
