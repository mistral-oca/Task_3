from selenium.webdriver.common.by import By

class FeedPageLocators:
    ORDER_CARD = (By.XPATH, "//div[contains(@class,'OrderHistory_textBox')]")
    ORDER_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]")
    ORDER_MODAL_TITLE = (By.XPATH, "//p[text()='Cостав']")
    TOTAL_COUNTER = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")    
    IN_PROGRESS_SECTION = (By.XPATH, "//p[text()='В работе:']/following-sibling::ul")
    