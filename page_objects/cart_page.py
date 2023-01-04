from selenium.webdriver.common.by import By

from page_objects.product_listing_page import ProductListing
from utilities.web_ui.base_page import BasePage


class CartPage(BasePage):
    _cart_button = (By.XPATH, '//a[@class="shopping_cart_link"]')
    _checkout_button = (By.XPATH, '//button[@id="checkout"]')
    _remove_backpack_button = (By.XPATH, '//button[@id="remove-sauce-labs-backpack"]')
    _cart_backpack = (By.XPATH, '//a[@id="item_4_title_link"]')
    _continue_shopping = (By.XPATH, '//button[@id="continue-shopping"]')
    _plp_title = (By.XPATH, '//span[@class="title"]')
    _first_name_input = (By.XPATH, '//input[@id="first-name"]')
    _last_name_input = (By.XPATH, '//input[@id="last-name"]')
    _postal_code_input = (By.XPATH, '//input[@id="postal-code"]')
    _checkout_info_title = (By.XPATH, '//span[@class="title"]')
    _continue_checkout = (By.XPATH, '//input[@id="continue"]')
    _finish_checkout = (By.XPATH, '//button[@id="finish"]')
    _complete_title = (By.XPATH, '//h2[@class="complete-header"]')

    def click_cart(self):
        self.click(self._cart_button)
        return self

    def click_remove_backpack(self):
        self.click(self._remove_backpack_button)
        return self

    def backpack_deleted(self):
        if self.element_invisible(self._cart_backpack):
            return True
        else:
            return False

    def click_continue_shopping(self):
        self.click(self._continue_shopping)
        return self.wait_until_element_displayed(self._plp_title)

    def click_checkout(self):
        self.click(self._checkout_button)
        return self

    def click_continue(self):
        self.click(self._continue_checkout)
        return self

    def click_finish_checkout(self):
        self.click(self._finish_checkout)
        return self

    def check_title_info(self):
        return self.compare_text(self._checkout_info_title, 'Checkout: Your Information')

    def check_order_finished(self):
        return self.compare_text(self._complete_title, 'THANK YOU FOR YOUR ORDER')

    def fill_information(self):
        self.send_keys(self._first_name_input, 'Adam')
        self.send_keys(self._last_name_input, 'Sandler')
        self.send_keys(self._postal_code_input, '04595')
        return self
