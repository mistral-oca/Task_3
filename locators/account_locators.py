from selenium.webdriver.common.by import By

class AccountLocators:
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[contains(., 'Личный Кабинет')]")
    ORDER_HISTORY_LINK = (By.XPATH, "//a[text()='История заказов']")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(., 'Выход')]")