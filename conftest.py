from page_objects.cart_page import CartPage
from page_objects.footer import Footer
from utilities.config_parser import ReadConfig
import pytest
import json
from page_objects.login_page import LoginPage
from page_objects.product_listing_page import ProductListing
from utilities.driver_factory import DriverFactory
from CONSTANTS import ROOT_DIR
from utilities.web_ui.json_configuraion import Configuration


@pytest.fixture(scope='session')
def parse():
    with open(f'{ROOT_DIR}/configurations/configuration.json') as file:
        parse_dict = json.loads(file.read())
    return Configuration(**parse_dict)


@pytest.fixture(scope='session')
def create_driver(parse):
    driver = DriverFactory.create_driver(parse.browser_id)
    driver.maximize_window()
    driver.get(parse.base_url)
    yield driver
    driver.quit()


@pytest.fixture()
def open_login_page(create_driver):
    return LoginPage(create_driver)


@pytest.fixture()
def logg_in(open_login_page, create_driver, parse):
    login_page = open_login_page
    login_page.set_email(parse.user_name).set_password(parse.password).click_log_in()
    return ProductListing(create_driver)


@pytest.fixture()
def open_footer(open_login_page, create_driver):
    login_page = open_login_page
    login_page.set_email(parse.user_name).set_password(parse.password).click_log_in()
    return Footer(create_driver)


@pytest.fixture()
def open_cart_with_items(logg_in, create_driver):
    logg_in.add_two_items_to_cart()
    return CartPage(create_driver)
