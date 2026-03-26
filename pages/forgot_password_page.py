from pages.base_page import BasePage
from locators.password_recovery_locators import PasswordRecoveryLocators
from config import urls


class ForgotPasswordPage(BasePage):

    URL = urls.FORGOT_PASSWORD

    def open(self):
        self.open_url(self.URL)

    def enter_email(self, email):
        self.send_keys(PasswordRecoveryLocators.EMAIL_INPUT, email)

    def click_recover(self):
        
        button = self.find_element(PasswordRecoveryLocators.RECOVER_BUTTON)
        self.scroll_into_view(button)
        self.click_js(button)

        self.wait_for_url_contains(urls.RESET_PASSWORD_ENDPOINT)