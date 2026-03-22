from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    URL = "https://stellarburgers.education-services.ru/login"  

    def open(self):
        self.driver.get(self.URL)

    def login(self, email, password):
        self.send_keys(LoginLocators.EMAIL_INPUT, email)
        self.send_keys(LoginLocators.PASSWORD_INPUT, password)
        self.click(LoginLocators.LOGIN_BUTTON)

        
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[contains(text(),'Оформить заказ')]")
            )
        )