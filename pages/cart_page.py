from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.LINK_TEXT, "Shopping Cart")
            )
        ).click()

    def get_product_name(self):
        product_links = self.driver.find_elements(
            By.CSS_SELECTOR,
            "table a"
        )

        for link in product_links:
            text = link.text.strip()

            if text:
                return text

        return ""

    def get_quantity(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "input[name^='quantity']")
            )
        ).get_attribute("value")

    def update_quantity(self, quantity):
        quantity_box = self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "input[name^='quantity']")
            )
        )

        quantity_box.clear()
        quantity_box.send_keys(str(quantity))

        self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button[data-original-title='Update']")
            )
        ).click()