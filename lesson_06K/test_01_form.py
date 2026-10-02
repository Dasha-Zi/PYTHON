from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form():
    driver = webdriver.Edge()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    wait = WebDriverWait(driver, 20)

    name_field = driver.find_element(By.NAME, "first-name")
    name_field.send_keys("Иван")

    surname_field = driver.find_element(By.NAME, "last-name")
    surname_field.send_keys("Петров")

    address_field = driver.find_element(By.NAME, "address")
    address_field.send_keys("Ленина, 55-3")

    email_field = driver.find_element(By.NAME, "e-mail")
    email_field.send_keys("test@skypro.com")
  
    phone_number_field = driver.find_element(By.NAME, "phone")
    phone_number_field.send_keys("+7985899998787")

    city_field = driver.find_element(By.NAME, "city")
    city_field.send_keys("Москва")

    country_field = driver.find_element(By.NAME, "country")
    country_field.send_keys("Россия")
    
    job_position_field = driver.find_element(By.NAME, "job-position")
    job_position_field.send_keys("QA")
   
    company_field = driver.find_element(By.NAME, "company")
    company_field.send_keys("SkyPro")
   
    submit_btn = driver.find_element(By.CLASS_NAME, "btn-outline-primary")
    submit_btn.click()

    zip_code_element = driver.find_element(By.ID, 'zip-code')

    border_color = zip_code_element.value_of_css_property('border-color')

    assert border_color == 'rgb(245, 194, 199)',"Поле 'Zip code' должно быть красным"

    fields = ["first-name",
              "last-name",
              "address",
              "city",
              "country",
              "e-mail",
              "phone",
              "job-position",
              "company"]

    for field_id in fields:
        field_element = wait.until(EC.visibility_of_element_located((By.ID, field_id)))
        border_color = field_element.value_of_css_property("border-color")
        assert border_color == "rgb(186, 219, 204)",f"Поле {field_id} не подсвечено зеленым"

    driver.quit()
