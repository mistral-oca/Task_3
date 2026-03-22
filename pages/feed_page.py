# feed_page.py
from pages.base_page import BasePage
from locators.feed_page_locators import FeedPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

class FeedPage(BasePage):

    URL_FEED = "/feed"

    def open_feed(self, base_url):
        
        self.driver.get(base_url + "feed")

    def get_all_orders(self):
        self.wait.until(
            EC.visibility_of_element_located(FeedPageLocators.ORDER_CARD)
        )
        return self.driver.find_elements(*FeedPageLocators.ORDER_CARD)

    def open_first_order(self):
        first_order = self.wait.until(
            EC.element_to_be_clickable(FeedPageLocators.ORDER_CARD)
        )
        first_order.click()

    
    def is_order_in_progress(self, order_number: str, timeout: int = 20) -> bool:
        
        order_number_ui = order_number.zfill(7)

        try:
            section = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(FeedPageLocators.IN_PROGRESS_SECTION)
            )

            WebDriverWait(self.driver, timeout).until(
                lambda d: any(
                    el.text.strip() == order_number_ui
                    for el in section.find_elements(By.XPATH, ".//li")
                )
            )

            return True
        except TimeoutException:
            return False

    def get_total_counter(self):
        element = self.find(FeedPageLocators.TOTAL_COUNTER)
        return int(element.text)

    def get_today_counter(self):
        element = self.find(FeedPageLocators.TODAY_COUNTER)
        return int(element.text)