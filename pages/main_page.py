from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from pages.base_page import BasePage
from locators.password_recovery_locators import PasswordRecoveryLocators
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    URL = "https://stellarburgers.education-services.ru/login"

    
    def open(self):
        self.driver.get(self.URL)

    
    def go_to_password_recovery(self):
        button = self.find(PasswordRecoveryLocators.RECOVERY_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        
        self.driver.execute_script("arguments[0].click();", button)

    
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

        constructor = self.driver.find_element(
            By.XPATH,
            "//ul[contains(@class,'BurgerConstructor_basket')]"
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            ingredient
        )

        actions = ActionChains(self.driver)

        actions.drag_and_drop(ingredient, constructor).perform()

        time.sleep(1)

    
    def create_order(self, timeout=10):
        
        self.click(MainPageLocators.CREATE_ORDER_BUTTON)

        
        order_modal = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_MODAL)
        )

        
        return order_modal