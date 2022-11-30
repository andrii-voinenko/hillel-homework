from selenium.webdriver.common.by import By


class ProductListing:
    def __init__(self, driver):
        self.__driver = driver

    _add_to_cart_backpack_locator = '//button[@id="add-to-cart-sauce-labs-backpack"]'
    _backpack_title_locator = '//a[@id="item_4_title_link"]'
    _backpack_img_locator = '//a[@id="item_4_img_link"]'
    _sort_dropdown_locator = '//select[@class="product_sort_container"]'
    _shopping_cart_locator = '//a[@class="shopping_cart_link"]'
    _all_products_title_locator = '.inventory_item_name'

    def check_products_titles(self):
        products = ['Sauce Labs Backpack', 'Sauce Labs Bike Light',
                    'Sauce Labs Bolt T-Shirt', 'Sauce Labs Fleece Jacket',
                    'Sauce Labs Onesie', 'Sauce Labs t-shirt'
                    ]
        all_products_titles_elements = self.__driver.find_elements(By.XPATH, self._all_products_title_locator)
        for element in all_products_titles_elements:
            if element not in products:
                return False
