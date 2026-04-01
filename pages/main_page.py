from pages.base_page import BasePage
from locators.password_recovery_locators import PasswordRecoveryLocators
from locators.main_page_locators import MainPageLocators
from config.urls import MAIN_PAGE


class MainPage(BasePage):

    def open(self):
        self.open_url(MAIN_PAGE)

    def open_constructor(self):
        button = self.find(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.click_js(button)

    def open_order_feed(self):
        self.click(MainPageLocators.ORDER_FEED_BUTTON)

    def click_ingredient(self):
        ingredient = self.find(MainPageLocators.INGREDIENT)
        self.scroll_into_view(ingredient)
        self.click_js(ingredient)

    def close_modal(self):
        self.click(MainPageLocators.CLOSE_MODAL_BUTTON)

    def drag_ingredient_to_constructor(self):
        ingredient = self.find(MainPageLocators.INGREDIENT)
        constructor = self.find(MainPageLocators.CONSTRUCTOR_BASKET)

        self.scroll_into_view(ingredient)

        self.drag_and_drop(ingredient, constructor)

    def create_order(self, timeout=10):
        self.click(MainPageLocators.CREATE_ORDER_BUTTON)
        return self.wait_for_visibility(MainPageLocators.ORDER_MODAL, timeout)

    def get_order_number(self, timeout=15):
        self.wait_for_visibility(MainPageLocators.ORDER_NUMBER, timeout)
        self.wait_for_text_not_empty(MainPageLocators.ORDER_NUMBER, timeout)
        return self.find(MainPageLocators.ORDER_NUMBER).text.strip()
    
    def close_order_modal(self):
        button = self.wait_for_clickable(MainPageLocators.CLOSE_MODAL_BUTTON)
        self.click_js(button)

    def get_counter_value(self):
        counter = self.find(MainPageLocators.COUNTER)
        return int(counter.text)
    
    def is_constructor_visible(self):
        return self.find(MainPageLocators.CONSTRUCTOR_SECTION).is_displayed()
    
    def wait_for_modal_close(self):
        self.wait_for_invisibility(MainPageLocators.INGREDIENT_MODAL)

    def is_ingredient_modal_visible(self):
        try:
            return self.find(MainPageLocators.INGREDIENT_MODAL).is_displayed()
        except:
            return False
        
    def is_constructor_page_opened(self):
        return MAIN_PAGE in self.get_current_url()  

    def is_feed_page_opened(self):
        return "feed" in self.get_current_url()