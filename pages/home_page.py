from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_my_account(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "a.dropdown-toggle")
            )
        ).click()

    def click_login(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.LINK_TEXT, "Login")
            )
        ).click()

    def search_product(self, product):
        search_box = self.wait.until(
            EC.visibility_of_element_located(
                (By.NAME, "search")
            )
        )

        search_box.clear()
        search_box.send_keys(product)

        self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    "button.btn.btn-default.btn-lg"
                )
            )
        ).click()