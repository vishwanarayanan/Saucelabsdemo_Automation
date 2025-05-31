import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.mark.inventory
def test_verify_product_count(setup):
    driver = setup
    login_page = LoginPage(driver)
    inventory_page=InventoryPage(driver)

    #login as a valid User
    login_page.login("standard_user","secret_sauce")

    #count the products
    products=inventory_page.get_all_products()

    #Assertion
    assert products is not None
    assert len(products)==6
@pytest.mark.inventory
def test_sort_products_low_to_high(setup):
    driver = setup
    login_page = LoginPage(driver)
    # login as a valid User
    login_page.login("standard_user", "secret_sauce")
    inventory_page = InventoryPage(driver)
    inventory_page.sort_by_price_low_to_high()
    product_prices = inventory_page.get_product_prices()
    assert product_prices == sorted(product_prices),f"Actual:{product_prices},Expected:{sorted(product_prices)}"

@pytest.mark.cart
def test_add_single_item_to_the_cart(setup):
    driver =setup
    login_page =LoginPage(driver)
    inventory_page = InventoryPage(driver)

    #login as a valid user
    login_page.login("standard_user", "secret_sauce")
    #Add item to cart
    inventory_page.add_backpack_to_cart()
    #get the cart badge count and assert
    badge_count = inventory_page.get_cart_badge_count()
    assert badge_count == 1, f"Expected Bagde Count to be 1 but got {badge_count}"

@pytest.mark.cart
def test_add_mutiple_items_to_cart(setup):
    driver = setup
    login_page = LoginPage(driver)
    inventory_page=InventoryPage(driver)
    # login as a valid user
    login_page.login("standard_user", "secret_sauce")
    #List of products to add
    products_to_add=["Sauce Labs Backpack","Sauce Labs Bike Light","Sauce Labs Bolt T-Shirt","Sauce Labs Onesie"]

    #Add products one by one

    for product in products_to_add:
        inventory_page.add_product_to_cart_by_name(product)

    #Assert products
    badge_count= inventory_page.get_cart_badge_count()
    assert badge_count==4,f"Expected Badge Count to be 4 but got {badge_count}"





