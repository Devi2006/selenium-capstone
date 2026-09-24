from selenium.webdriver.common.by import By


class SearchPage:

    def __init__(self, driver):
        self.driver = driver

    def select_product(self, product_name):
        self.driver.find_element(
            By.LINK_TEXT,
            product_name
        ).click()

    def add_to_cart(self):
        self.driver.find_element(
            By.ID,
            "button-cart"
        ).click()