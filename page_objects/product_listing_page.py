from functools import reduce
from selenium.webdriver.common.by import By
from utilities.web_ui.base_page import BasePage


class ProductListing(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    _backpack_title = (By.XPATH, '//a[@id="item_4_title_link"]')
    _backpack_img = (By.XPATH, '//a[@id="item_4_img_link"]')
    _sort_dropdown = (By.XPATH, '//select[@class="product_sort_container"]')
    _shopping_cart = (By.XPATH, '//a[@class="shopping_cart_link"]')
    _all_products_title = (By.CSS_SELECTOR, '.inventory_item_name')
    _product_details_page = (By.XPATH, '//div[@class="inventory_details"]')
    _add_backpack = (By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')
    _add_light = (By.XPATH, '//button[@id="add-to-cart-sauce-labs-bike-light"]')
    _cart_counter = (By.XPATH, '//span[@class="shopping_cart_badge"]')
    _all_prices = (By.XPATH, '//div[@class="inventory_item_price"]')
    _lohi = (By.XPATH, '//option[@value="lohi"]')

    def check_products_titles(self):
        products = ['Sauce Labs Backpack', 'Sauce Labs Bike Light',
                    'Sauce Labs Bolt T-Shirt', 'Sauce Labs Fleece Jacket',
                    'Sauce Labs Onesie', 'Sauce Labs t-shirt'
                    ]
        all_products_titles_elements = self.find_elements(self._all_products_title)
        for element in all_products_titles_elements:
            if element not in products:
                return False

    def check_low_high(self):
        self.click(self._sort_dropdown)
        self.click(self._lohi)

        all_prices = []
        sorted_prices = ['7.99', '9.99', '15.99', '15.99', '29.99', '49.99']  # Bad solution

        founded_elements = self.find_elements(self._all_prices)
        for item in founded_elements:
            all_prices.append(item.text.replace('$', ''))

        if reduce(lambda x, y: x and y, map(lambda p, q: p == q, sorted_prices, all_prices), True):
            return True
        else:
            return False

    # TODO: product instead element
    def click_on_the_element(self, element_name: str):
        if element_name == 'image':
            self.click(self._backpack_img)
            return self.wait_until_element_displayed(self._product_details_page)
        elif element_name == 'title':
            self.click(self._backpack_title)
            return self.wait_until_element_displayed(self._product_details_page)
        else:
            raise ValueError('Incorrect element name')

    def add_two_items_to_cart(self):
        self.click(self._add_light)
        self.click(self._add_backpack)

    def get_cart_counter_qty(self):
        return self.get_element_text(self._cart_counter)
