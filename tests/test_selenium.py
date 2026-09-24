from selenium import webdriver

from pages import cart_page
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.search_page import SearchPage
from pages.cart_page import CartPage


def test_purchase_product():

    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.get(
        "https://tutorialsninja.com/demo/"
    )

    home_page = HomePage(driver)
    login_page = LoginPage(driver)
    search_page = SearchPage(driver)
    cart_page = CartPage(driver)

    # =========================
    # LOGIN
    # =========================

    home_page.open_my_account()
    home_page.click_login()

    login_page.enter_email(
        "d91691576@gmail.com"
    )

    login_page.enter_password(
        "Test@1122"
    )

    login_page.click_login()

    print("Login successful")

    # =========================
    # SEARCH PRODUCT
    # =========================

    home_page.search_product("iPhone")

    print("Product search completed")

    # =========================
    # SELECT PRODUCT
    # =========================

    search_page.select_product("iPhone")

    print("Product selected")

    # =========================
    # ADD TO CART
    # =========================

    search_page.add_to_cart()

    print("Product added to cart")

    # =========================
    # OPEN CART
    # =========================

    cart_page.open_cart()

    print("Cart opened")

    # =========================
    # VERIFY CART
    # =========================

    actual_product = cart_page.get_product_name()

    print("Product in cart:", actual_product)

    assert actual_product == "iPhone"

# =========================
# UPDATE QUANTITY
# =========================

    cart_page.update_quantity(2)

    print("Quantity updated to 2")

    actual_quantity = cart_page.get_quantity()

    print("Updated quantity:", actual_quantity)

    assert actual_quantity == "2"

    print("Cart verification successful")

    # =========================
    # CLOSE BROWSER
    # =========================

    driver.quit()