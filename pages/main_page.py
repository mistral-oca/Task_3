from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from pages.base_page import BasePage
from locators.password_recovery_locators import PasswordRecoveryLocators
from locators.main_page_locators import MainPageLocators
from config import urls

class MainPage(BasePage):

    URL = urls.LOGIN  

    def open(self):
        self.open_url(self.URL)

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
        constructor = self.find_element_by_xpath(
            "//ul[contains(@class,'BurgerConstructor_basket')]"
        )
        self.scroll_into_view(ingredient)

        actions = ActionChains(self.driver)
        actions.drag_and_drop(ingredient, constructor).perform()
        time.sleep(1)

    def create_order(self, timeout=10):
        self.click(MainPageLocators.CREATE_ORDER_BUTTON)
        order_modal = self.wait_for_visibility(MainPageLocators.ORDER_MODAL, timeout)
        return order_modal