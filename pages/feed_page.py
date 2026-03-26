from pages.base_page import BasePage
from locators.feed_page_locators import FeedPageLocators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class FeedPage(BasePage):

    URL_FEED = "feed"

    def open_feed(self, base_url):
        self.open_url(base_url + self.URL_FEED)

    def get_all_orders(self):
        self.wait_for_visibility(FeedPageLocators.ORDER_CARD)
        return self.find_all(FeedPageLocators.ORDER_CARD)

    def open_first_order(self):
        first_order = self.wait_for_clickable(FeedPageLocators.ORDER_CARD)
        first_order.click()

    def is_order_in_progress(self, order_number: str, timeout: int = 20) -> bool:
        order_number_ui = order_number.zfill(7)

        try:
            section = self.find_element(FeedPageLocators.IN_PROGRESS_SECTION)

            self.wait.until(
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