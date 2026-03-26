from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    
    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def find_element_by_xpath(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)

    
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def click_js(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    def send_keys(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    
    def open_url(self, url):
        self.driver.get(url)

    def wait_for_url_contains(self, text):
        self.wait.until(EC.url_contains(text))

    
    def wait_for_visibility(self, locator, timeout=None):
        w = WebDriverWait(self.driver, timeout) if timeout else self.wait
        return w.until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator, timeout=None):
        w = WebDriverWait(self.driver, timeout) if timeout else self.wait
        return w.until(EC.element_to_be_clickable(locator))

    def wait_for_invisibility(self, locator, timeout=5):
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )