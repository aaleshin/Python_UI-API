from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as Wait


class UIHelpers:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def wait_element_to_be_clickable(self, locator):
        return Wait(self.driver, 10).until(EC.element_to_be_clickable(locator))

    def wait_element_to_be_visibility(self, locator):
        return Wait(self.driver, 10).until(EC.visibility_of_element_located(locator))

