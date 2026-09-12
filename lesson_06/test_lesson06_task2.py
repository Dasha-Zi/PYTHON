from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()

    # Откройте страницу https://gitflic.ru/

    driver.get("https://gitflic.ru/")

    # Установите cookie пользователя 1
    driver.add_cookie({
        "name": "SESSION",
   "value": "NTNiY2ZiNWItZWQ1Yy00OGVlLTg1N2ItOTA5MGNjOGE0YzY3",
   "domain": "gitflic.ru"
})

    # Обновите страницу

    driver.refresh()

    # Перейдите на страницу пользователя 1

    driver.get("https://gitflic.ru/user/sky-best-student")

    # сохранить URL 

    url_user_1 = driver.current_url

    # разлогиньтесь

    driver.delete_all_cookies()

    # Установите cookie пользователя 2

    driver.add_cookie({
            "name": "SESSION",
       "value": "ZjI4MzgyOTMtMjc3My00YmU1LWJkODMtY2Q2ZTU2ZTM3NTQw",
       "domain": "gitflic.ru"
})
    # Обновите страницу
    
    driver.refresh()
    
        # Перейдите на страницу пользователя 2
    
    driver.get("https://gitflic.ru/user/sky-student")
    
        # сохранить URL 
    
    url_user_2 = driver.current_url

    assert url_user_1 != url_user_2

    driver.quit()
