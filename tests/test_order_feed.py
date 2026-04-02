import allure
from pages.feed_page import FeedPage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from config.credentials import TEST_EMAIL, TEST_PASSWORD

@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("Открытие модального окна заказа")
    def test_open_order_details_modal(self, driver):
        feed = FeedPage(driver)
        feed.open_feed()
        feed.open_first_order()

        assert feed.is_order_modal_visible(), "Модальное окно заказа не отображается"

    @allure.title("Авторизованный пользователь видит заказы в ленте")
    def test_user_orders_visible_in_feed(self, driver):
        login = LoginPage(driver)
        login.open()
        login.login(TEST_EMAIL, TEST_PASSWORD)

        feed = FeedPage(driver)
        feed.open_feed()

        assert feed.get_all_orders_count() > 0, "Список заказов пуст"

    @allure.title("Общий счётчик увеличивается после создания заказа")
    def test_total_counter_increases_after_order(self, driver):
        feed = FeedPage(driver)
        feed.open_feed()
        total_before = feed.get_total_counter()

        login = LoginPage(driver)
        login.open()
        login.login(TEST_EMAIL, TEST_PASSWORD)

        main = MainPage(driver)
        main.open()
        main.drag_ingredient_to_constructor()
        main.create_order()

        feed.open_feed()
        total_after = feed.get_total_counter()
        assert total_after > total_before, "Общий счётчик не увеличился после создания заказа"

    @allure.title("Счётчик заказов за сегодня увеличивается после создания заказа")
    def test_today_counter_increases_after_order(self, driver):
        feed = FeedPage(driver)
        feed.open_feed()
        today_before = feed.get_today_counter()

        login = LoginPage(driver)
        login.open()
        login.login(TEST_EMAIL, TEST_PASSWORD)

        main = MainPage(driver)
        main.open()
        main.drag_ingredient_to_constructor()
        main.create_order()

        feed.open_feed()
        today_after = feed.get_today_counter()
        assert today_after > today_before, "Счётчик заказов за сегодня не увеличился"

    @allure.title("Созданный заказ отображается в статусе 'В работе'")
    def test_order_appears_in_progress(self, driver):
        login = LoginPage(driver)
        login.open()
        login.login(TEST_EMAIL, TEST_PASSWORD)

        main = MainPage(driver)
        main.open()
        main.drag_ingredient_to_constructor()
        main.create_order()
        order_number = main.get_order_number()
        main.close_order_modal()

        feed = FeedPage(driver)
        feed.open_feed()

        assert feed.is_order_in_progress(order_number), f"Заказ #{order_number} не найден в 'В работе'"