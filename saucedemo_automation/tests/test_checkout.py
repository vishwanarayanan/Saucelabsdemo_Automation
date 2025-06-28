import allure
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import Cart_page
from pages.checkout_page import CheckoutPage


@allure.description("Ensure clicking checkout on cart redirects to info page")
@allure.severity("Critical")
@allure.feature("Checkout")
@allure.story("Access checkout from cart")
@allure.tag("checkout")
@pytest.mark.checkout
def test_proceed_to_checkout(setup):
    driver=setup
    login_page=LoginPage(driver)
    inventory_page=InventoryPage(driver)
    cart_page=Cart_page(driver)
    checkout_page=CheckoutPage(driver)

    #Login
    login_page.login("standard_user","secret_sauce")
    #Add item to cart
    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_cart()
    #Click checkout
    cart_page.click_checkout()
    # Assert checkout title
    assert checkout_page.get_title()=="Checkout: Your Information"

@allure.description("Enter valid first name, last name, and zip to proceed")
@allure.severity("Major")
@allure.feature("Checkout")
@allure.story("Enter valid user info")
@allure.tag("checkout")
@pytest.mark.checkout
def test_checkout_valid_info(setup):
    driver=setup
    login_page=LoginPage(driver)
    inventory_page=InventoryPage(driver)
    cart_page=Cart_page(driver)
    checkout_page=CheckoutPage(driver)

    #login
    login_page.login("standard_user","secret_sauce")
    #Add item to cart
    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_cart()

    #Go  to checkout
    cart_page.click_checkout()

    # Fill valid info
    checkout_page.enter_first_name("Test")
    checkout_page.enter_last_name("User")
    checkout_page.enter_zip_code("603201")
    checkout_page.click_continue()

    #Assert checout page title
    assert checkout_page.get_title()=="Checkout: Overview"

@allure.description("Validate totals calculation during checkout summary")
@allure.severity("Major")
@allure.feature("Order Summary")
@allure.story("Summary values validation")
@allure.tag("order_summary")
def test_verify_order_and_summary_totals(setup):
    driver=setup
    login_page=LoginPage(driver)
    inventory_page=InventoryPage(driver)
    cart_page=Cart_page(driver)
    checkout_page=CheckoutPage(driver)

    #Login
    login_page.login("standard_user","secret_sauce")
    #Add item to cart
    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_cart()

    #Go to checkout
    cart_page.click_checkout()

    #Fill in valid details
    checkout_page.enter_first_name("Test")
    checkout_page.enter_last_name("User")
    checkout_page.enter_zip_code("603201")
    checkout_page.click_continue()

