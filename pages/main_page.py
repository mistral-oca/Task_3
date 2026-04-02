import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from config.urls import MAIN_PAGE


class MainPage(BasePage):

    @allure.step("Открываем главную страницу")
    def open(self):
        self.open_url(MAIN_PAGE)

    @allure.step("Открываем конструктор")
    def open_constructor(self):
        button = self.find(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.click_js(button)

    @allure.step("Открываем ленту заказов")
    def open_order_feed(self):
        self.click(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Кликаем по ингредиенту")
    def click_ingredient(self):
        ingredient = self.find(MainPageLocators.INGREDIENT)
        self.scroll_into_view(ingredient)
        self.click_js(ingredient)

    @allure.step("Закрываем модальное окно")
    def close_modal(self):
        self.click(MainPageLocators.CLOSE_MODAL_BUTTON)

    @allure.step("Перетаскиваем ингредиент в конструктор")
    def drag_ingredient_to_constructor(self):
        ingredient = self.find(MainPageLocators.INGREDIENT)
        constructor = self.find(MainPageLocators.CONSTRUCTOR_BASKET)
        self.scroll_into_view(ingredient)
        self.drag_and_drop(ingredient, constructor)

    @allure.step("Создаём заказ")
    def create_order(self, timeout=10):
        self.click(MainPageLocators.CREATE_ORDER_BUTTON)
        return self.wait_for_visibility(MainPageLocators.ORDER_MODAL, timeout)

    @allure.step("Получаем номер заказа")
    def get_order_number(self, timeout=15):
        self.wait_for_visibility(MainPageLocators.ORDER_NUMBER, timeout)
        self.wait_for_text_not_empty(MainPageLocators.ORDER_NUMBER, timeout)
        return self.find(MainPageLocators.ORDER_NUMBER).text.strip()

    @allure.step("Закрываем модальное окно заказа")
    def close_order_modal(self):
        button = self.wait_for_clickable(MainPageLocators.CLOSE_MODAL_BUTTON)
        self.click_js(button)

    @allure.step("Получаем значение счётчика")
    def get_counter_value(self):
        counter = self.find(MainPageLocators.COUNTER)
        return int(counter.text)