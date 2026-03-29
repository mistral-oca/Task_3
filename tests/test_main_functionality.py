from pages.main_page import MainPage
from pages.login_page import LoginPage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from config.urls import MAIN_PAGE, LOGIN, BASE_URL
from config.credentials import TEST_EMAIL, TEST_PASSWORD  


@allure.feature("Проверка основного функционала")
class TestMainFunctionality:

    @allure.title("Открытие конструктора")
    def test_open_constructor(self, driver):
        
        driver.get(BASE_URL)
        page = MainPage(driver)
        page.open_constructor()

        assert BASE_URL in driver.current_url

    @allure.step("Открываем конструктор")
    def open_constructor_step(self, page):
        page.open_constructor()

    @allure.title("Открытие ленты заказов")
    def test_open_order_feed(self, driver):
        driver.get(MAIN_PAGE)
        page = MainPage(driver)
        self.open_order_feed_step(page)
        assert "feed" in driver.current_url

    @allure.step("Открываем ленту заказов")
    def open_order_feed_step(self, page):
        page.open_order_feed()

    @allure.title("Открытие модального окна ингредиента")
    def test_open_ingredient_modal(self, driver):
        driver.get(MAIN_PAGE)
        page = MainPage(driver)
        self.click_ingredient_step(page)
        modal = page.find(MainPageLocators.INGREDIENT_MODAL)
        assert modal.is_displayed()

    @allure.step("Кликаем по ингредиенту")
    def click_ingredient_step(self, page):
        page.click_ingredient()

    @allure.title("Закрытие модального окна ингредиента")
    def test_close_ingredient_modal(self, driver):
        driver.get(MAIN_PAGE)
        page = MainPage(driver)
        self.click_ingredient_step(page)
        self.close_modal_step(page)

        WebDriverWait(driver, 5).until(
            EC.invisibility_of_element_located(MainPageLocators.INGREDIENT_MODAL)
        )

        element = driver.find_element(*MainPageLocators.INGREDIENT_MODAL)
        assert not element.is_displayed()

    @allure.step("Закрываем модальное окно")
    def close_modal_step(self, page):
        page.close_modal()

    @allure.title("Счётчик увеличивается при добавлении ингредиента")
    def test_counter_increases_when_ingredient_added(self, driver):
        driver.get(MAIN_PAGE)
        page = MainPage(driver)
        self.drag_ingredient_step(page)

        assert page.get_counter_value() > 0

    @allure.step("Перетаскиваем ингредиент в конструктор")
    def drag_ingredient_step(self, page):
        page.drag_ingredient_to_constructor()

    @allure.title("Авторизованный пользователь может создать заказ")
    def test_logged_user_can_create_order(self, driver):
        driver.get(LOGIN)
        login_page = LoginPage(driver)
        self.login_step(login_page)

        driver.get(MAIN_PAGE)
        page = MainPage(driver)
        self.drag_ingredient_step(page)
        order_modal = self.create_order_step(page)
        assert order_modal.is_displayed()

    @allure.step("Авторизуемся пользователем")
    def login_step(self, login_page):
        login_page.login(TEST_EMAIL, TEST_PASSWORD)

    @allure.step("Создаём заказ")
    def create_order_step(self, page):
        return page.create_order()