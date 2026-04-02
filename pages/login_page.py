import allure
from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from config import urls
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    URL = urls.LOGIN  

    @allure.step("Открываем страницу логина")
    def open(self):
        self.open_url(self.URL)  

    @allure.step("Авторизуемся пользователем")
    def login(self, email, password):
        self.send_keys(LoginLocators.EMAIL_INPUT, email)
        self.send_keys(LoginLocators.PASSWORD_INPUT, password)
        self.click(LoginLocators.LOGIN_BUTTON)

        self.wait.until(
            EC.visibility_of_element_located(LoginLocators.ORDER_BUTTON)
        )

    @allure.step("Переходим на восстановление пароля")
    def go_to_password_recovery(self):
        self.click(LoginLocators.RECOVERY_BUTTON)