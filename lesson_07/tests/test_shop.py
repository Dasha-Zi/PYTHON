from selenium import webdriver
from page.shop_page import LoginPage, ShopPage, CartPage, CheckoutPage


def test_shop_checkout():
    driver = webdriver.Firefox()

    login_page = LoginPage(driver)
    chop_page = ShopPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    # 1. Открываем сайт магазина
    login_page.open()

    # 2. Авторизуемся под пользователем standard_user
    # Пароль — secret_sauce
    login_page.login("standard_user", "secret_sauce")

    # 3. Добавляем в корзину выбранные товары
    chop_page.add_item_to_cart("sauce-labs-backpack")
    chop_page.add_item_to_cart("sauce-labs-bolt-t-shirt")
    chop_page.add_item_to_cart("sauce-labs-onesie")

    # 4. Переходим в корзину
    chop_page.go_to_cart()

    # 5. Нажимаем кнопку Checkout
    cart_page.click_checkout()

    # 6. Заполняем форму своими данными и нажимаем Continue внутри метода
    checkout_page.fill_checkout_form("Дарья", "Зимина", "426000")

    # 7. Читаем со страницы итоговую стоимость (Total)
    total_price_text = checkout_page.get_total_price()

    # 8. Закрываем браузер
    driver.quit()

    # 9. Проверяем (assert), что итоговая сумма равна $58.29
    assert "58.29" in total_price_text, (
        f"Ожидалась итоговая сумма $58.29, но на странице: '{total_price_text}'"
    )
