from utilities.config_parser import ReadConfig
import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome
from page_objects.login_page import LoginPage


@pytest.fixture()
def create_driver():
    chrome_driver = Chrome(service=Service(ChromeDriverManager().install()))
    chrome_driver.maximize_window()
    chrome_driver.get(ReadConfig().get_base_url())
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture()
def open_login_page(create_driver):
    return LoginPage(create_driver)


@pytest.fixture()
def logg_in(open_login_page):
    login_page = open_login_page
    login_page.set_email('standard_user').set_password('secret_sauce').log_in_click()
