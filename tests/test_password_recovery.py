import allure
from pages.main_page import MainPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage

TEST_EMAIL = "dottest@test.ru"
TEST_PASSWORD = "123456"


@allure.feature("Восстановление пароля")
class TestPasswordRecovery:

    @allure.title("Переход на страницу восстановления пароля")
    def test_go_to_password_recovery_page(self, driver):

        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_password_recovery()

        assert "forgot-password" in driver.current_url


    @allure.title("Ввод email и нажатие кнопки восстановления")
    def test_enter_email_and_click_recover(self, driver):

        page = ForgotPasswordPage(driver)
        page.open()
        page.enter_email(TEST_EMAIL)
        page.click_recover()

        assert "reset-password" in driver.current_url


    @allure.title("Кнопка показать/скрыть пароль делает поле активным")
    def test_show_hide_password_button(self, driver):

        forgot_page = ForgotPasswordPage(driver)
        forgot_page.open()
        forgot_page.enter_email(TEST_EMAIL)
        forgot_page.click_recover()

        reset_page = ResetPasswordPage(driver)

        reset_page.enter_password(TEST_PASSWORD)
        reset_page.click_show_hide_password()

        assert reset_page.is_password_active()