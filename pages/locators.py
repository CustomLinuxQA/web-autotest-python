from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LOCATOR = (By.CSS_SELECTOR, "a[class$='btn-default']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    CHECKOUT_LOCATOR = (By.CSS_SELECTOR, "a[class$='btn-block']")
    BASKET_IS_EMPTY_LOCATOR = (By.CSS_SELECTOR, "div p")


class LoginPageLocators():
    DELETE_PASS_INPUT = (By.CSS_SELECTOR, "div [name='password']")
    DELETE_PROFILE_BUTTON = (By.CSS_SELECTOR, "#delete_profile")
    DELETE_PROFILE_BUTTON_CONFIRM = (By.CSS_SELECTOR, ".btn-danger")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[value='Log In']")
    LOGIN_FORM = (By.ID, "login_form")
    LOGIN_EMAIL_INPUT = (By.CSS_SELECTOR, "#login_form [name='login-username']")
    LOGIN_PASS_INPUT = (By.CSS_SELECTOR, "#login_form [name='login-password']")
    REGISTER_BUTTON =(By.CSS_SELECTOR, "button[value=Register]")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_EMAIL_INPUT = (By.CSS_SELECTOR, "#register_form [name='registration-email']")
    REGISTER_PASS_INPUT = (By.CSS_SELECTOR, "#register_form [name='registration-password1']")
    REGISTER_PASS_CONFIRM_INPUT = (By.CSS_SELECTOR, "#register_form [name='registration-password2']")


class MainPageLocators():
    MOK_LOCATOR = (By.CSS_SELECTOR, "#mok")


class ProductPageLocators():
    ADD_CART = (By.CSS_SELECTOR, "#add_to_basket_form")
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, ".basket-mini")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
    NOTIFICATION_ADD_TO_BASKET = (By.CSS_SELECTOR, "div[id='messages'] div:nth-child(1) div")
    NOTIFICATION_ITEM_NAME = (By.CSS_SELECTOR, "div[id='messages'] div:nth-child(1) strong")
    NOTIFICATION_TOTAL_PRICE = (By.CSS_SELECTOR, "div[id='messages'] div:nth-child(3) strong")
    NOTIFICATION_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div[id='messages'] div:nth-child(2) div strong")
