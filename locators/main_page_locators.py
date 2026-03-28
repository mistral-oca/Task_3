from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']/ancestor::a")
    INGREDIENT = (By.XPATH, "//a[contains(@class,'BurgerIngredient')]")
    INGREDIENT_MODAL = (By.XPATH, "//h2[text()='Детали ингредиента']")
    CLOSE_MODAL_BUTTON = (By.XPATH, "//button[contains(@class,'Modal_modal__close')]")
    ADD_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_MODAL = (By.CSS_SELECTOR, "div.Modal_modal__contentBox__sCy8X")
    CREATE_ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")
    ORDER_NUMBER = (By.XPATH, "//div[contains(@class,'Modal_modal')]//h2[contains(@class,'text_type_digits-large')]")
    CONSTRUCTOR_BASKET = (By.XPATH, "//ul[contains(@class,'BurgerConstructor_basket')]")