from pages.main_page import MainPage
from pages.login_page import LoginPage
import allure
from config.credentials import TEST_EMAIL, TEST_PASSWORD  


@allure.feature("Проверка основного функционала")
class TestMainFunctionality:

    @allure.title("Открытие конструктора")
    def test_open_constructor(self, driver):
        page = MainPage(driver)
        page.open()

        assert page.is_constructor_page_opened()


    @allure.title("Открытие ленты заказов")
    def test_open_order_feed(self, driver):
        page = MainPage(driver)
        page.open()
        page.open_order_feed()

        assert page.is_feed_page_opened()


    @allure.title("Открытие модального окна ингредиента")
    def test_open_ingredient_modal(self, driver):
        page = MainPage(driver)
        page.open()
        page.click_ingredient()

        assert page.is_ingredient_modal_visible()


    @allure.title("Закрытие модального окна ингредиента")
    def test_close_ingredient_modal(self, driver):
        page = MainPage(driver)
        page.open()
        page.click_ingredient()
        page.close_modal()

        page.wait_for_modal_close()
        assert not page.is_ingredient_modal_visible()


    @allure.title("Счётчик увеличивается при добавлении ингредиента")
    def test_counter_increases_when_ingredient_added(self, driver):
        page = MainPage(driver)
        page.open()
        page.drag_ingredient_to_constructor()

        assert page.get_counter_value() > 0


    @allure.title("Авторизованный пользователь может создать заказ")
    def test_logged_user_can_create_order(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(TEST_EMAIL, TEST_PASSWORD)

        page = MainPage(driver)
        page.open()
        page.drag_ingredient_to_constructor()

        order_modal = page.create_order()
        assert order_modal.is_displayed()