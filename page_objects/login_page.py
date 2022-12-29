from time import sleep
from selenium.webdriver.common.by import By

from utilities.web_ui.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    _email = (By.XPATH, '//input[@id="user-name"]')
    _password = (By.XPATH, '//input[@id="password"]')
    _login_button = (By.XPATH, '//input[@id="login-button"]')
    _burger_menu = (By.XPATH, '//button[@id="react-burger-menu-btn"]')
    _error = (By.XPATH, '//div//h3[@data-test="error"]')
    _error_button = (By.XPATH, '//button[@class="error-button"]')

    _error_text = "Epic sadface: Sorry, this user has been locked out."

    def set_email(self, email_value: str):
        self.send_keys(self._email, email_value)
        return self

    def set_password(self, password_value: str):
        self.send_keys(self._password, password_value)
        return self

    def click_log_in(self):
        return self.click(self._login_button)

    def click_error_button(self):
        return self.click(self._error_button)

    def menu_is_displayed(self):
        return self.wait_until_element_displayed(self._burger_menu)

    def error_text(self):
        if self.get_element_text(self._error) == self._error_text:
            return True
        else:
            return False

    def no_error_notification(self):
        if self.element_invisible(self._error):
            return True
        else:
            return False
