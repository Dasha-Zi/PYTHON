from selenium import webdriver
from selenium.webdriver.common.by import By

def test_page_title():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/")

    title = driver.find_element(By.TAG_NAME, "h1")
    assert "httpbin" in title.text.lower()
   
    driver.quit()
    