from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

        self._delay_input = (By.ID, "delay")
        self._screen = (By.CLASS_NAME,"screen")


    def open(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def delay (self, seconds: str):
        input_field = self.driver.find_element(*self._delay_input)
        input_field.clear()
        input_field.send_keys(seconds)

    
    def click_button(self, button_text: str):
        button_locator = (By.XPATH, f"//span[text()='{button_text}']")
        self.driver.find_element(*button_locator).click()

    def wait_for_result(self, expected_result: str, timeout: int = 45):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self._screen, expected_result)
    )

    def get_result_text(self) -> str:
        return self.driver.find_element(*self._screen).text
    


