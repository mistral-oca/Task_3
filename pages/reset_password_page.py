from pages.base_page import BasePage
from locators.password_recovery_locators import PasswordRecoveryLocators
from config import urls


class ResetPasswordPage(BasePage):

    URL = urls.RESET_PASSWORD_ENDPOINT

    def open(self):
        self.open_url(self.URL)

    def enter_password(self, password):
        self.send_keys(PasswordRecoveryLocators.PASSWORD_INPUT, password)

    def click_show_hide_password(self):
        button = self.find_element(PasswordRecoveryLocators.SHOW_HIDE_PASSWORD_BUTTON)
        self.scroll_into_view(button)
        self.click_js(button)

    def is_password_active(self):
        element = self.find(PasswordRecoveryLocators.PASSWORD_INPUT)
        return element.get_attribute("type") == "text"