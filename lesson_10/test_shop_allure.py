import allure
from selenium import webdriver
from shop_page_allure import LoginPage, ShopPage, CartPage, CheckoutPage

@allure.epic("Интернет-магазин")
@allure.story("Aвтотест для проверки функциональности интернет-магазина")
@allure.title("Проверка функциональности интернет-магазина")
@allure.description("Тест проверяет функциональность интернет-магазина")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.BLOCKER )

def test_shop_checkout():
    """Тест проверяет работу интернеет-магазин с различными операциями:
    авторизация, добавление товаров в корзину, оформление заказа и проверка стоимости.
    :param driver: WebDriver — объект драйвера, переданный фикстурой.
    """
    driver = webdriver.Firefox()

    login_page = LoginPage(driver)
    chop_page = ShopPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    with allure.step("Открываем сайт магазина"):
        login_page.open()

    with allure.step("Авторизуемся под пользователем standard_user"):
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Добавляем в корзину выбранные товары"):
        chop_page.add_item_to_cart("sauce-labs-backpack")
        chop_page.add_item_to_cart("sauce-labs-bolt-t-shirt")
        chop_page.add_item_to_cart("sauce-labs-onesie")

    with allure.step("Переходим в корзину"):
        chop_page.go_to_cart()

    with allure.step("Нажимаем кнопку Checkout"):
        cart_page.click_checkout()

    with allure.step("Заполняем форму своими данными и нажимаем Continue внутри метода"):
        checkout_page.fill_checkout_form("Дарья", "Зимина", "426000")

    with allure.step("Читаем со страницы итоговую стоимость (Total)"):
        total_price_text = checkout_page.get_total_price()

    with allure.step("Закрываем браузер"):
        driver.quit()

    with allure.step("Проверяем (assert), что итоговая сумма равна $58.29"):
        assert "58.29" in total_price_text, (
        f"Ожидалась итоговая сумма $58.29, но на странице: '{total_price_text}'"
    )
    