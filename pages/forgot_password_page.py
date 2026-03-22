from pages.base_page import BasePage
from locators.password_recovery_locators import PasswordRecoveryLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ForgotPasswordPage(BasePage):

    URL = "https://stellarburgers.education-services.ru/forgot-password"

    
    def open(self):
        self.driver.get(self.URL)

    
    def enter_email(self, email):
        self.send_keys(PasswordRecoveryLocators.EMAIL_INPUT, email)

    
    def click_recover(self):

        wait = WebDriverWait(self.driver, 10)

        button = wait.until(
            EC.presence_of_element_located(
                PasswordRecoveryLocators.RECOVER_BUTTON
            )
        )

        
        self.driver.execute_script("arguments[0].scrollIntoView();", button)

        
        self.driver.execute_script("arguments[0].click();", button)

        
        wait.until(EC.url_contains("reset-password"))