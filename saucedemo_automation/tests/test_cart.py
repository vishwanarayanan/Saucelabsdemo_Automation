import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import Cart_page


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