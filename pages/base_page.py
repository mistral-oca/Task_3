from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def send_keys(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def wait_for_invisibility(self, locator, timeout=5):
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )