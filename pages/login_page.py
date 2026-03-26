from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from config import urls
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    URL = urls.LOGIN  

    def open(self):
        self.open_url(self.URL)  

    def login(self, email, password):
        self.send_keys(LoginLocators.EMAIL_INPUT, email)
        self.send_keys(LoginLocators.PASSWORD_INPUT, password)
        self.click(LoginLocators.LOGIN_BUTTON)

        
        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[contains(text(),'Оформить заказ')]")
            )
        )