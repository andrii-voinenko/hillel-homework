from time import sleep
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.__driver = driver

    _email_locator = '//input[@id="user-name"]'
    _password_locator = '//input[@id="password"]'
    _login_button_locator = '//input[@id="login-button"]'
    _menu_locator = '//button[@id="react-burger-menu-btn"]'
    _error_locator = '//div//h3[@data-test="error"]'

    def __find_element(self, locator: str):
        web_element = self.__driver.find_element(By.XPATH, locator)
        return web_element

    def set_email(self, email_value: str):
        email_element = self.__find_element(self._email_locator)
        email_element.clear()
        email_element.send_keys(email_value)
        return self

    def set_password(self, password_value: str):
        password_element = self.__find_element(self._password_locator)
        password_element.clear()
        password_element.send_keys(password_value)
        sleep(3)
        return self

    def log_in_click(self):
        login_button_element = self.__find_element(self._login_button_locator)
        login_button_element.click()

    def menu_is_displayed(self):
        menu_element = self.__find_element(self._menu_locator)
        return menu_element.is_displayed()

    def error_message(self):
        error_element = self.__find_element(self._error_locator)
        return error_element.is_displayed()
