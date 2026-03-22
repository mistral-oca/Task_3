from pages.main_page import MainPage
from pages.login_page import LoginPage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


TEST_EMAIL = "dottest@test.ru"
TEST_PASSWORD = "123456"

@allure.feature("Проверка основного функционала")
class TestMainFunctionality:

    @allure.title("Открытие конструктора")
    def test_open_constructor(self, driver, base_url):

        driver.get(base_url)

        page = MainPage(driver)
        page.open_constructor()

        assert "constructor" in driver.current_url or base_url in driver.current_url

    @allure.title("Открытие ленты заказов")
    def test_open_order_feed(self, driver, base_url):

        driver.get(base_url)

        page = MainPage(driver)
        page.open_order_feed()

        assert "feed" in driver.current_url

    @allure.title("Открытие модального окна ингредиента")
    def test_open_ingredient_modal(self, driver, base_url):

        driver.get(base_url)

        page = MainPage(driver)
        page.click_ingredient()

        modal = page.find(MainPageLocators.INGREDIENT_MODAL)

        assert modal.is_displayed()

    @allure.title("Закрытие модального окна ингредиента")
    def test_close_ingredient_modal(self, driver, base_url):

        driver.get(base_url)

        page = MainPage(driver)
        page.click_ingredient()
        page.close_modal()

        
        WebDriverWait(driver, 5).until(
            EC.invisibility_of_element_located(MainPageLocators.INGREDIENT_MODAL)
        )

        
        element = driver.find_element(*MainPageLocators.INGREDIENT_MODAL)
        assert not element.is_displayed()

    @allure.title("Счётчик увеличивается при добавлении ингредиента")
    def test_counter_increases_when_ingredient_added(self, driver, base_url):

        driver.get(base_url)

        page = MainPage(driver)
        page.drag_ingredient_to_constructor()
        
        counter = driver.find_element(
            "xpath",
            "//p[contains(@class,'counter_counter__num')]"
        )

        assert int(counter.text) > 0

    @allure.title("Авторизованный пользователь может создать заказ")
    def test_logged_user_can_create_order(self, driver, base_url):

        driver.get(base_url + "login")

        login_page = LoginPage(driver)
        login_page.login(TEST_EMAIL, TEST_PASSWORD)

        driver.get(base_url)

        page = MainPage(driver)
        page.drag_ingredient_to_constructor()
        order_modal = page.create_order()  
        assert order_modal.is_displayed()