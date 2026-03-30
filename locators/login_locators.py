from selenium.webdriver.common.by import By

class LoginLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@type='text']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    PERSONAL_ACCOUNT_INDICATOR = (By.XPATH, "//p[text()='Личный кабинет']")
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")