from pages.base_page import BasePage
from locators.account_locators import AccountLocators

class AccountPage(BasePage):

    def open_personal_account(self):
        self.click(AccountLocators.PERSONAL_ACCOUNT_BUTTON)

    def go_to_order_history(self):
        self.click(AccountLocators.ORDER_HISTORY_LINK)

    def logout(self):
        self.wait_for_url_contains("account")

        button = self.find(AccountLocators.LOGOUT_BUTTON)
        
        self.click_js(button)

        self.wait_for_url_contains("login")

    def is_personal_account_opened(self):
        return "account" in self.get_current_url()

    def is_order_history_opened(self):
        return "order-history" in self.get_current_url()

    def is_logged_out(self):
        return "login" in self.get_current_url()