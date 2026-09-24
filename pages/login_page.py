from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_email(self, email):
        self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, "input-email")
            )
        ).send_keys(email)

    def enter_password(self, password):
        self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, "input-password")
            )
        ).send_keys(password)

    def click_login(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "input[type='submit']")
            )
        ).click()

        # Wait for the page after login to load
        self.wait.until(
            EC.presence_of_element_located(
                (By.NAME, "search")
            )
        )