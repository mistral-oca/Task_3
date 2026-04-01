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

    @allure.step("Открываем конструктор")
    def open_constructor_step(self, page):
        page.open_constructor()

    @allure.title("Открытие ленты заказов")
    def test_open_order_feed(self, driver):
        page = MainPage(driver)
        page.open() 
        self.open_order_feed_step(page)
        assert page.is_feed_page_opened()

    @allure.step("Открываем ленту заказов")
    def open_order_feed_step(self, page):
        page.open_order_feed()

    @allure.title("Открытие модального окна ингредиента")
    def test_open_ingredient_modal(self, driver):
        page = MainPage(driver)
        page.open()
        self.click_ingredient_step(page)

        assert page.is_ingredient_modal_visible()

    @allure.step("Кликаем по ингредиенту")
    def click_ingredient_step(self, page):
        page.click_ingredient()

    @allure.title("Закрытие модального окна ингредиента")
    def test_close_ingredient_modal(self, driver):
        page = MainPage(driver)
        page.open()
        self.click_ingredient_step(page)
        self.close_modal_step(page)

        page.wait_for_modal_close()
        assert not page.is_ingredient_modal_visible()

        
    @allure.step("Закрываем модальное окно")
    def close_modal_step(self, page):
        page.close_modal()

    @allure.title("Счётчик увеличивается при добавлении ингредиента")
    def test_counter_increases_when_ingredient_added(self, driver):
        page = MainPage(driver)
        page.open()
        self.drag_ingredient_step(page)
        assert page.get_counter_value() > 0

    @allure.step("Перетаскиваем ингредиент в конструктор")
    def drag_ingredient_step(self, page):
        page.drag_ingredient_to_constructor()

    @allure.title("Авторизованный пользователь может создать заказ")
    def test_logged_user_can_create_order(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        self.login_step(login_page)

        page = MainPage(driver)
        page.open()
        self.drag_ingredient_step(page)
        order_modal = self.create_order_step(page)
        assert order_modal.is_displayed()

    @allure.step("Авторизуемся пользователем")
    def login_step(self, login_page):
        login_page.login(TEST_EMAIL, TEST_PASSWORD)

    @allure.step("Создаём заказ")
    def create_order_step(self, page):
        return page.create_order()