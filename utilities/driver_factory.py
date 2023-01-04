from selenium.webdriver import Chrome, Edge
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class DriverFactory:
    CHROME = 1
    EDGE = 2

    @staticmethod
    def create_driver(driver_id: int):
        if int(driver_id) == 1:
            driver = Chrome(service=Service(ChromeDriverManager().install()))
        elif int(driver_id) == 2:
            driver = Edge(service=Service(EdgeChromiumDriverManager().install()))
        else:
            driver = Chrome(service=Service(ChromeDriverManager().install()))
        return driver
