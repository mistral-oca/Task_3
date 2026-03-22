from pages.base_page import BasePage
from locators.account_locators import AccountLocators
from selenium.webdriver.support import expected_conditions as EC

class AccountPage(BasePage):

    def open_personal_account(self):
        self.wait.until(EC.element_to_be_clickable(AccountLocators.PERSONAL_ACCOUNT_BUTTON)).click()

    def go_to_order_history(self):
        self.click(AccountLocators.ORDER_HISTORY_LINK)

    def logout(self):
        self.wait.until(EC.url_contains("account"))

        button = self.wait.until(
            EC.presence_of_element_located(AccountLocators.LOGOUT_BUTTON)
        )
        
        self.driver.execute_script("arguments[0].click();", button)

        self.wait.until(EC.url_contains("login"))