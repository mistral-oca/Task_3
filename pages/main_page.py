from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
from locators.password_recovery_locators import PasswordRecoveryLocators
from locators.main_page_locators import MainPageLocators
from config.urls import MAIN_PAGE
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):

    def go_to_password_recovery(self):
        button = self.find(PasswordRecoveryLocators.RECOVERY_BUTTON)
        self.scroll_into_view(button)
        self.click_js(button)

    def open_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON)

    def open_order_feed(self):
        self.click(MainPageLocators.ORDER_FEED_BUTTON)

    def click_ingredient(self):
        self.click(MainPageLocators.INGREDIENT)

    def close_modal(self):
        self.click(MainPageLocators.CLOSE_MODAL_BUTTON)

    def drag_ingredient_to_constructor(self):
        ingredient = self.find(MainPageLocators.INGREDIENT)
        constructor = self.find(MainPageLocators.CONSTRUCTOR_BASKET)

        self.scroll_into_view(ingredient)

        actions = ActionChains(self.driver)
        actions.drag_and_drop(ingredient, constructor).perform()

    def create_order(self, timeout=10):
        self.click(MainPageLocators.CREATE_ORDER_BUTTON)
        return self.wait_for_visibility(MainPageLocators.ORDER_MODAL, timeout)

    def get_order_number(self, timeout=15):
        order_number_element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_NUMBER)
        )
        
        WebDriverWait(self.driver, timeout).until(
            lambda d: order_number_element.text.strip() not in ["", "9999"]
        )
        return order_number_element.text.strip()
    
    def close_order_modal(self):
        button = self.wait_for_clickable(MainPageLocators.CLOSE_MODAL_BUTTON)
        self.driver.execute_script("arguments[0].click();", button)