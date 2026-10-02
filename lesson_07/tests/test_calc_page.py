from selenium import webdriver
from page.calc_page import CalcPage

def test_calculator():
    driver = webdriver.Chrome()
    calc_page = CalcPage(driver)
    calc_page.open()

    calc_page.delay("45")

    calc_page.click_button("7")
    calc_page.click_button("+")
    calc_page.click_button("8")
    calc_page.click_button("=")

    calc_page.wait_for_result("15", timeout=45)

    final_result = calc_page.get_result_text()
    assert final_result == "15", (
        f"Ожидался результат '15', но калькулятор выдал: '{final_result}'"
    )
    driver.quit()

