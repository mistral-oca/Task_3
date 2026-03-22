from pages.base_page import BasePage
from locators.password_recovery_locators import PasswordRecoveryLocators


class ResetPasswordPage(BasePage):

    URL = "https://stellarburgers.education-services.ru/reset-password"

    
    def enter_password(self, password):
        self.send_keys(PasswordRecoveryLocators.PASSWORD_INPUT, password)

    def click_show_hide_password(self):
        
        button = self.wait.until(
            lambda d: d.find_element(*PasswordRecoveryLocators.SHOW_HIDE_PASSWORD_BUTTON)
        )
    
        
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
    
        
        self.driver.execute_script("arguments[0].click();", button)

    def is_password_active(self):
        element = self.find(PasswordRecoveryLocators.PASSWORD_INPUT)
        return element.get_attribute("type") == "text"