from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_form_interaction():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")

    sleep(2)

    input_name = driver.find_element(By.NAME, "custname")
    input_name.send_keys("Иван Иванов")

    submit_order = driver.find_element(By.XPATH, "//button[text()='Submit order']")
    submit_order.click()
    sleep(5)

    # Заполните поле "custname" значением "Иван Иванов"
    # Найдите кнопку отправки и кликните на нее
    # Ваш код здесь

    driver.quit()
