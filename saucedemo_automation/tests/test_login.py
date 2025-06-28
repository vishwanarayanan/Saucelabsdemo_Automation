import allure
import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from data.test_data import invalid_login
from data.test_data import valid_login
from data.test_data import locked_out_user


@pytest.fixture
def setup():
    driver= webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


@allure.description("Validate standard user login and redirection to inventory")
@allure.severity("Critical")
@allure.feature("Login")
@allure.story("User can log in with valid credentials")
@allure.tag("login")
@pytest.mark.login
def test_valid_login(setup):
    driver=setup
    login_page=LoginPage(driver)
    inventory_page=InventoryPage(driver)

    # Enter valid Credentials
    login_page.login("standard_user","secret_sauce")
    #assert redirection to inventory page
    assert "/inventory.html" in driver.current_url ,"Not redirected to inventory page"

    #Assert products title is visible
    assert inventory_page.get_title()== "products","'products' title not found on Inventory Page "



@allure.description("Validate error messages for invalid usernames and passwords")
@allure.severity("Critical")
@allure.feature("Login")
@allure.story("Error messages on invalid login")
@allure.tag("login")
@pytest.mark.login
@pytest.mark.parametrize("username,password",invalid_login)
def test_invalid_login(setup,username,password):
    driver = setup
    login_page=LoginPage(driver)
    login_page.login(username,password)
    error_text= login_page.get_error_message()
    assert "username and password" in error_text.lower() or "epic sadface" in error_text.lower()

@allure.description("Verify locked out user receives appropriate error message")
@allure.severity("Blocker")
@allure.feature("Login")
@allure.story("Locked out user cannot locked in")
@allure.tag("login")
@pytest.mark.login
@pytest.mark.parametrize("username,password",locked_out_user)
def test_locked_out_user(setup,username,password):
    login_page =LoginPage(setup)
    login_page.login(username,password)
    error_text = login_page.get_error_message()
    assert "sorry, this user has been locked out" in error_text.lower()

""""
def test_verify_product_count(setup):
    driver = setup
    login_page = LoginPage(driver)
    inventory_page=InventoryPage(driver)

    #login as a valid User
    login_page.login("standard_user","secret_sauce")

    #count the products
    products=inventory_page.get_all_products()

    #Assertion
    assert len(products)==6,f"Expected 6 products ,but got {len(products)}"
"""