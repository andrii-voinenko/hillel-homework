from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.__driver = driver
        self.__wait = WebDriverWait(self.__driver, 5)

    def wait_until_element_located(self, locator: tuple):
        return self.__wait.until(EC.presence_of_element_located(locator))

    def wait_until_element_clickable(self, locator: tuple):
        return self.__wait.until(EC.element_to_be_clickable(locator))

    def find_elements(self, locator: tuple):
        return self.__wait.until(EC.visibility_of_all_elements_located(locator))

    def send_keys(self, locator: tuple, value, is_clear=True):
        element = self.wait_until_element_clickable(locator)
        if is_clear:
            element.clear()
        element.send_keys(value)

    def click(self, locator: tuple):
        element = self.wait_until_element_clickable(locator)
        element.click()

    def wait_until_element_displayed(self, locator: tuple):
        return self.__wait.until(EC.visibility_of_element_located(locator))

    def element_invisible(self, locator: tuple):
        return self.__wait.until(EC.invisibility_of_element(locator))

    def get_element_text(self, locator: tuple):
        element = self.wait_until_element_displayed(locator)
        return element.text

    def url_changed(self, url):
        return self.__wait.until(EC.url_changes(url))

    def compare_text(self, locator: tuple, text: str):
        title = text
        text_from_page = self.get_element_text(locator)
        return text_from_page.lower() == title.lower()
