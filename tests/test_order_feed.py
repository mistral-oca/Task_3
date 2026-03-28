from pages.feed_page import FeedPage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from locators.feed_page_locators import FeedPageLocators
from config.urls import LOGIN, MAIN_PAGE, FEED_PAGE
import allure


TEST_EMAIL = "dottest@test.ru"
TEST_PASSWORD = "123456"

@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("Открытие модального окна заказа")
    def test_open_order_details_modal(self, driver):

        feed = FeedPage(driver)
        feed.open_feed()   # 👈 убрали base_url

        feed.open_first_order()

        modal = feed.find(FeedPageLocators.ORDER_MODAL_TITLE)
        assert modal.is_displayed()

    @allure.title("Авторизованный пользователь видит заказы в ленте")
    def test_user_orders_visible_in_feed(self, driver):

        driver.get(LOGIN)
        login = LoginPage(driver)
        login.login(TEST_EMAIL, TEST_PASSWORD)

        driver.get(FEED_PAGE)
        feed = FeedPage(driver)

        orders = feed.get_all_orders()
        assert len(orders) > 0

    @allure.title("Общий счётчик увеличивается после создания заказа")
    def test_total_counter_increases_after_order(self, driver):

        feed = FeedPage(driver)
        feed.open_feed()

        total_before = feed.get_total_counter()

        driver.get(LOGIN)
        login = LoginPage(driver)
        login.login(TEST_EMAIL, TEST_PASSWORD)

        driver.get(MAIN_PAGE)

        main = MainPage(driver)
        main.drag_ingredient_to_constructor()
        main.create_order()

        driver.get(FEED_PAGE)

        total_after = feed.get_total_counter()
        assert total_after > total_before

    @allure.title("Счётчик заказов за сегодня увеличивается после создания заказа")
    def test_today_counter_increases_after_order(self, driver):

        feed = FeedPage(driver)
        feed.open_feed()

        today_before = feed.get_today_counter()

        driver.get(LOGIN)
        login = LoginPage(driver)
        login.login(TEST_EMAIL, TEST_PASSWORD)

        driver.get(MAIN_PAGE)

        main = MainPage(driver)
        main.drag_ingredient_to_constructor()
        main.create_order()

        driver.get(FEED_PAGE)

        today_after = feed.get_today_counter()
        assert today_after > today_before

    @allure.title("Созданный заказ отображается в статусе 'В работе'")
    def test_order_appears_in_progress(self, driver): 

        driver.get(LOGIN) 
        login = LoginPage(driver) 
        login.login(TEST_EMAIL, TEST_PASSWORD) 
        driver.get(MAIN_PAGE) 
        main = MainPage(driver) 
        main.drag_ingredient_to_constructor() 
        main.create_order() 
        order_number = main.get_order_number() 
        main.close_order_modal() 
        driver.get(FEED_PAGE) 
        feed = FeedPage(driver) 

        assert feed.is_order_in_progress(order_number), f"Заказ #{order_number} не найден в 'В работе'"