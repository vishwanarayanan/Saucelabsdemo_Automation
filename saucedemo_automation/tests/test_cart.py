import allure
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import Cart_page

@allure.description("Verify a single item can be added to cart and reflected in cart page")
@allure.severity("Critical")
@allure.feature("Cart")
@allure.story("Add item  to cart")
@allure.tag("cart")
@pytest.mark.cart
def test_add_to_cart(setup):
    driver =setup
    login_page=LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page=Cart_page(driver)

    #Login
    login_page.login("standard_user","secret_sauce")
    #Add first product to cart
    inventory_page.add_product_to_cart_by_name("Sauce Labs Backpack")
    inventory_page.go_to_cart()

    cart_items = cart_page.get_cart_items()
    assert "Sauce Labs Backpack" in cart_items

@allure.description("Add multiple items and ensure each is visible in the cart")
@allure.severity("Major")
@allure.feature("Cart")
@allure.story("Add Multiple items to cart")
@allure.tag("cart")
@pytest.mark.cart
def test_view_cart_items(setup):
    driver =setup
    login_page = LoginPage(driver)
    inventory_page =InventoryPage(driver)
    cart_page  = Cart_page(driver)
    # Login
    login_page.login("standard_user","secret_sauce")
    # Add products to cart
    products_to_add=["Sauce Labs Backpack","Sauce Labs Bike Light","Sauce Labs Fleece Jacket","Sauce Labs Onesie"]
    for products in products_to_add:
        inventory_page.add_product_to_cart_by_name(products)
    # Go to Cart
    inventory_page.go_to_cart()
    # Get items in cart and verify
    cart_items = cart_page.get_cart_items()
    for product in products_to_add:
        assert  product in cart_items ,f"{product}not found in cart !"

@allure.description("Test continue shopping button redirects to inventory page")
@allure.severity("Major")
@allure.feature("Cart")
@allure.story("Navigate back to shop")
@allure.tag("cart")
@pytest.mark.shop
def test_continue_shopping(setup):
    driver=setup
    login_page = LoginPage(driver)
    inventory_page=InventoryPage(driver)
    cart_page = Cart_page(driver)

    login_page.login("standard_user","secret_sauce")
    try :
        driver.execute_script("document.querySelector('[role=dialog] button').click()")
    except:
        pass
    # add an optional product
    inventory_page.add_backpack_to_cart()
    #navigate to cartpage
    inventory_page.go_to_cart()
    #click continue shopping
    cart_page.click_continue_shopping()
    # Assert title that we are back in inventory page
    title = inventory_page.get_title()
    assert title == "products",f"Expected 'products' but got {title}"

