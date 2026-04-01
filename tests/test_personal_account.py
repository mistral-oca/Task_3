import allure
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from config.credentials import TEST_EMAIL, TEST_PASSWORD

@allure.feature("Личный кабинет")
class TestPersonalAccount:

    @allure.title("Переход в личный кабинет")
    def test_open_personal_account(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(TEST_EMAIL, TEST_PASSWORD)

        account_page = AccountPage(driver)
        account_page.open_personal_account()

        assert account_page.is_personal_account_opened()

    @allure.title("Переход в историю заказов")
    def test_open_order_history(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(TEST_EMAIL, TEST_PASSWORD)

        account_page = AccountPage(driver)
        account_page.open_personal_account()
        account_page.go_to_order_history()

        assert account_page.is_order_history_opened()

    @allure.title("Выход из аккаунта")
    def test_logout(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(TEST_EMAIL, TEST_PASSWORD)

        account_page = AccountPage(driver)
        account_page.open_personal_account()
        account_page.logout()

        assert account_page.is_logged_out()