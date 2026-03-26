from pages.base_page import BasePage
from locators.account_locators import AccountLocators

class AccountPage(BasePage):

    def open_personal_account(self):
        self.click(AccountLocators.PERSONAL_ACCOUNT_BUTTON)

    def go_to_order_history(self):
        self.click(AccountLocators.ORDER_HISTORY_LINK)

    def logout(self):
        self.wait_for_url_contains("account")

        button = self.find_element(AccountLocators.LOGOUT_BUTTON)
        self.click_js(button)

        self.wait_for_url_contains("login")