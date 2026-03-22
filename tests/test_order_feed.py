from pages.feed_page import FeedPage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from locators.feed_page_locators import FeedPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


TEST_EMAIL = "dottest@test.ru"
TEST_PASSWORD = "123456"

@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("Открытие модального окна заказа")
    def test_open_order_details_modal(self, driver, base_url):

        feed = FeedPage(driver)
        feed.open_feed(base_url)

        feed.open_first_order()

        modal = feed.find(FeedPageLocators.ORDER_MODAL_TITLE)

        assert modal.is_displayed()

    @allure.title("Авторизованный пользователь видит заказы в ленте")
    def test_user_orders_visible_in_feed(self, driver, base_url):
        driver.get(base_url + "login")
        login = LoginPage(driver)
        login.login(TEST_EMAIL, TEST_PASSWORD)

        driver.get(base_url + "feed")
        feed = FeedPage(driver)
        orders = feed.get_all_orders()

        assert len(orders) > 0

    @allure.title("Общий счётчик увеличивается после создания заказа")
    def test_total_counter_increases_after_order(self, driver, base_url):

        feed = FeedPage(driver)
        feed.open_feed(base_url)

        total_before = feed.get_total_counter()

        
        driver.get(base_url + "login")
        login = LoginPage(driver)
        login.login(TEST_EMAIL, TEST_PASSWORD)

        driver.get(base_url)

        main = MainPage(driver)
        main.drag_ingredient_to_constructor()
        main.create_order()

        driver.get(base_url + "feed")

        total_after = feed.get_total_counter()

        assert total_after > total_before

    @allure.title("Счётчик заказов за сегодня увеличивается после создания заказа")
    def test_today_counter_increases_after_order(self, driver, base_url):

        feed = FeedPage(driver)
        feed.open_feed(base_url)

        today_before = feed.get_today_counter()

        
        driver.get(base_url + "login")
        login = LoginPage(driver)
        login.login(TEST_EMAIL, TEST_PASSWORD)

        driver.get(base_url)

        main = MainPage(driver)
        main.drag_ingredient_to_constructor()
        main.create_order()

        driver.get(base_url + "feed")

        today_after = feed.get_today_counter()

        assert today_after > today_before

    @allure.title("Созданный заказ отображается в статусе 'В работе'")
    def test_order_appears_in_progress(self, driver, base_url):
    
        
        driver.get(base_url + "login")
        login = LoginPage(driver)
        login.login(TEST_EMAIL, TEST_PASSWORD)

        
        driver.get(base_url)
        main = MainPage(driver)
        main.drag_ingredient_to_constructor()
        main.create_order()

        
        order_modal = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h2[contains(@class,'Modal_modal__title')]")
            )
        )

        
        WebDriverWait(driver, 15).until(
            lambda d: order_modal.text.strip() not in ["", "9999"]
        )

        
        order_number = order_modal.text.strip()

        
        try:
            close_button = driver.find_element(By.CLASS_NAME, "Modal_closeIcon__1e6Ty")
            close_button.click()
        except:
            pass  
        
        driver.get(base_url + "feed")
        feed = FeedPage(driver)

        
        assert feed.is_order_in_progress(order_number), f"Заказ #{order_number} не найден в 'В работе'"