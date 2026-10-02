from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    # Класс для страницы авторизации.
    def __init__(self, driver):
        self.driver = driver
        self._user_name = (By.ID, "user-name")
        self._password = (By.ID, "password")
        self._login_button = (By.ID, "login-button")
    

    def open(self):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, timeout=10)

    def login(self, username, password):
        self.driver.find_element(*self._user_name).send_keys(username)
        self.driver.find_element(*self._password).send_keys(password)
        self.driver.find_element(*self._login_button).click()


class ShopPage:
    # Класс главной страницы магазина.
    def __init__(self, driver):
        self.driver = driver
        self._cart_link = (By.ID, "shopping_cart_container")

    def add_item_to_cart(self, item_id_name):
        locator = (By.CSS_SELECTOR, f"#add-to-cart-{item_id_name}")
        self.driver.find_element(*locator).click()

    def go_to_cart(self):
        self.driver.find_element(*self._cart_link).click()


class CartPage:
    # Класс страницы корзины.
    def __init__(self, driver):
        self.driver = driver
        self._checkout_button = (By.ID, "checkout")

    def click_checkout(self):
        self.driver.find_element(*self._checkout_button).click()


class CheckoutPage:
    # Класс страницы оформления заказа и проверки стоимости
    def __init__(self, driver):
        self.driver = driver
        self._first_name = (By.ID, "first-name")
        self._last_name = (By.ID, "last-name")
        self._postal_code = (By.ID, "postal-code")
        self._continue_button = (By.ID, "continue")
        self._total_label = (By.CLASS_NAME, "summary_total_label")

    def fill_checkout_form(self, first_name, last_name, postal_code):
        self.driver.find_element(*self._first_name).send_keys(first_name)
        self.driver.find_element(*self._last_name).send_keys(last_name)
        self.driver.find_element(*self._postal_code).send_keys(postal_code)
        self.driver.find_element(*self._continue_button).click()

    def get_total_price(self):
        return self.driver.find_element(*self._total_label).text