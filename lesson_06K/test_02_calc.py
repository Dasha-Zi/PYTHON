from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form():
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    wait = WebDriverWait(driver, 20)

    input_field = driver.find_element(By.ID, "delay")
    input_field.clear()
    input_field.send_keys("45")

    btn = driver.find_element(By.XPATH, "//span[text()='7']")
    btn.click()

    btn = driver.find_element(By.XPATH, "//span[text()='+']")
    btn.click()

    btn = driver.find_element(By.XPATH, "//span[text()='8']")
    btn.click()

    btn = driver.find_element(By.XPATH, "//span[text()='=']")
    btn.click()

    WebDriverWait(driver, 45).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME,"screen"), "15")
    )
    assert "15" in driver.find_element(By.CLASS_NAME,"screen").text

    driver.quit()