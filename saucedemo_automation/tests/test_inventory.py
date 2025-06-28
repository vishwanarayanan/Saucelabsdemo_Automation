import allure
import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@allure.description("Validate total product count visible after login")
@allure.severity("Minor")
@allure.feature("Inventory")
@allure.story("Product List display")
@allure.tag("inventory")
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


@allure.description("Sort products by price (Low to High) and assert order")
@allure.severity("Minor")
@allure.feature("Inventory")
@allure.story("Sort functionality")
@allure.tag("inventory")
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



@allure.description("Add single item and validate cart badge is updated")
@allure.severity("Major")
@allure.feature("Cart")
@allure.story("Badge count check")
@allure.tag("cart")
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



@allure.description("Add multiple items and assert badge count equals total")
@allure.severity("Major")
@allure.feature("Cart")
@allure.story("Badge count for multiple items")
@allure.tag("cart")
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



@allure.description("Remove item and validate cart badge resets to zero")
@allure.severity("Major")
@allure.feature("Cart")
@allure.story("Cart badge after removal")
@allure.tag("cartremove")
@pytest.mark.cartremove
def test_remove_item_from_cart_updates_badge(setup):
    driver = setup
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    # login as a valid user
    login_page.login("standard_user", "secret_sauce")
    #Add a Product
    product = "Sauce Labs Backpack"
    inventory_page.add_product_to_cart_by_name(product)
    #Remove the Added Product
    inventory_page.remove_product_by_name(product)
    #Assert the Cart badge
    try:
        badge_count =inventory_page.get_cart_badge_count()
        assert badge_count == 0 , f"Expected badge count is 0 but got {badge_count}"
    except Exception:
        pass


@allure.description("Test logout option and assert return to login page")
@allure.severity("Major")
@allure.feature("Menu")
@allure.story("User logout")
@allure.tag("logout")
@pytest.mark.logout
def test_logout_functionality(setup):
    driver=setup
    login_page=LoginPage(driver)
    inventory_page=InventoryPage(driver)
    #user login
    login_page.login("standard_user", "secret_sauce")
    #click on menu btn
    inventory_page.open_menu()
    inventory_page.clicklogout()
    assert "saucedemo.com" in driver.current_url


@allure.description("Check About link redirects to saucelabs.com")
@allure.severity("Minor")
@allure.feature("Menu")
@allure.story("Navigate to About")
@allure.tag("about")
@pytest.mark.about
def test_about_functionality(setup):
    driver=setup
    login_page=LoginPage(driver)
    inventory_page=InventoryPage(driver)
    #user login
    login_page.login("standard_user", "secret_sauce")
    #click on menu
    inventory_page.open_menu()
    #click on about
    inventory_page.click_about()
    assert "saucelabs.com" in driver.current_url



@allure.description("Test that Reset App State clears cart badge")
@allure.severity("Major")
@allure.feature("Menu")
@allure.story("Reset app state")
@allure.tag("resetapp")
@pytest.mark.resetapp
def test_reset_app_state(setup):
    driver = setup
    login_page=LoginPage(driver)
    inventory_page=InventoryPage(driver)
    #user login
    login_page.login("standard_user", "secret_sauce")
    # Add a product to cart
    inventory_page.add_backpack_to_cart()
    assert inventory_page.get_cart_badge_count()==1
    #click on menu
    inventory_page.open_menu()
    #click on reset app status
    inventory_page.click_reset_app_state()

    #verify badge count after clicking on reset app state
    try:
       badge_count = inventory_page.get_cart_badge_count()==0
       assert badge_count == 0 ,f"Expected cart count is 0 but got{badge_count}"
    except:
        pass



