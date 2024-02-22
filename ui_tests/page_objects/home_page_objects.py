from selenium.webdriver.common.by import By
from misc.ui_custom_methods import UIHelpers


class HomePage(UIHelpers):
    base_url = "http://bluelight.inc/"
    APPLY = (By.CSS_SELECTOR, '#subscribe-button')
    EMAILFIELD = (By.XPATH, "//input[@id='form-email']")
    SERVERERROR = (By.CSS_SELECTOR, '#server-error')
    EMPTYFIELD = (By.CSS_SELECTOR, '#empty-field')
    WRONGEMAIL = (By.CSS_SELECTOR, '#wrong-email')
    SEEYASOON = (By.XPATH, "//div[contains(text(),'See ya soon!')]")
    ACCEPT = (By.XPATH, "//a[contains(text(),'accept')]")

    def input_email(self, email):
        self.wait_element_to_be_clickable(self.EMAILFIELD).send_keys(email)

    def click_to_element(self, locator):
        self.wait_element_to_be_clickable(locator).click()

    def get_email_error(self, error_type):
        email_error = self.wait_element_to_be_visibility(error_type)
        return email_error.text

    def accept_email(self):
        email_accept = self.wait_element_to_be_visibility(self.SEEYASOON)
        return email_accept.text
