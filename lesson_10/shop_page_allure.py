from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import allure

@allure.feature("Страница авторизации")
class LoginPage:
    """Класс страницы авторизации
    Конструктор класса LoginPage.
    :param driver: WebDriver — объект драйвера Selenium."""
    def __init__(self, driver):
        self.driver = driver
        self._user_name = (By.ID, "user-name")
        self._password = (By.ID, "password")
        self._login_button = (By.ID, "login-button")
    
    @allure.step("Открытие страницу авторизации интернет-магазина")
    def open(self):
        """
        Открывает страницу аторизации.
        """
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, timeout=10)
    
    @allure.step("Авторизация на странице интернет-магазина и переход на главную страницу магазина")
    def login(self, username : str, password : str):
        """Авторизуемся на странице, вводим параметры username и password.
        username - standard_user
        password - secret_sauce """
        self.driver.find_element(*self._user_name).send_keys(username)
        self.driver.find_element(*self._password).send_keys(password)
        self.driver.find_element(*self._login_button).click()

@allure.feature("Главна ястраница магазина")
class ShopPage:
    """Класс главной страницы магазина
    Конструктор класса ShopPage.
    :param driver: WebDriver — объект драйвера Selenium."""
    def __init__(self, driver):
        self.driver = driver
        self._cart_link = (By.ID, "shopping_cart_container")
    
    @allure.step("Добавление товаров в корзину")
    def add_item_to_cart(self, item_id_name : str):
        """
        Нажимаем на несколько кнопок для добавления товаров в корзину по очереди.
        :param item_id_name: list[str] — список текстов на кнопках,
        которые нужно нажать. """
        locator = (By.CSS_SELECTOR, f"#add-to-cart-{item_id_name}")
        self.driver.find_element(*locator).click()

    @allure.step("Переход в корзину")
    def go_to_cart(self):
        """
        Нажимаем на кнопку корзины для перехода в нее."""
        self.driver.find_element(*self._cart_link).click()

@allure.feature("Корзина товаров")
class CartPage:
    """Класс страницы корзины
    Конструктор класса CartPage.
    :param driver: WebDriver — объект драйвера Selenium."""
    def __init__(self, driver):
        self.driver = driver
        self._checkout_button = (By.ID, "checkout")
    
    @allure.step("Нажатие кнопки Checkout")
    def click_checkout(self):
        """
            Нажимаем на кнопку Checkout и проверяет содержимое корзины."""
        self.driver.find_element(*self._checkout_button).click()

@allure.feature("Оформление заказа")
class CheckoutPage:
    """Класс страницы оформления заказа и проверки стоимости
    Конструктор класса CartPage.
    :param driver: WebDriver — объект драйвера Selenium."""
    def __init__(self, driver):
        self.driver = driver
        self._first_name = (By.ID, "first-name")
        self._last_name = (By.ID, "last-name")
        self._postal_code = (By.ID, "postal-code")
        self._continue_button = (By.ID, "continue")
        self._total_label = (By.CLASS_NAME, "summary_total_label")

    @allure.feature("Авторизация пользователей")
    @allure.step("Заполнение формы данными (имя, фамилия, почтовый индекс)")
    def fill_checkout_form(self, first_name : str, last_name : str, postal_code : int):
        """Заполняем формы данными (имя, фамилия, почтовый индекс):
        имя - "Дарья", фамилия - "Зимина", почтовый индекс - "426000
        Нажимаем на кнопку continue для проверки итоговой стоимости. """
        self.driver.find_element(*self._first_name).send_keys(first_name)
        self.driver.find_element(*self._last_name).send_keys(last_name)
        self.driver.find_element(*self._postal_code).send_keys(postal_code)
        self.driver.find_element(*self._continue_button).click()

    @allure.step("Проверка итоговой стоимости")
    def get_total_price(self):
        """
        Возвращает итоговую сумму, равную $58.29

        :return: str — текст результата итоговой суммы.
        """
        return self.driver.find_element(*self._total_label).text
    