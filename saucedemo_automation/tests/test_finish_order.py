import allure
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import Cart_page
from pages.checkout_page import CheckoutPage
from pages.order_summary_page import OrderSummaryPage


@allure.description("Complete the order and validate the success confirmation message")
@allure.severity("Critical")
@allure.feature("Order")
@allure.story("Finish purchase")
@allure.tag("order_complete")
@pytest.mark.order_complete
def test_finish_order(setup):
    driver=setup
    login_page = LoginPage(driver)
    inventory_page=InventoryPage(driver)
    cart_page=Cart_page(driver)
    checkout_page=CheckoutPage(driver)
    order_summary_page=OrderSummaryPage(driver)


    login_page.login("standard_user","secret_sauce")
    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_cart()
    cart_page.click_checkout()
    checkout_page.enter_first_name("Test")
    checkout_page.enter_last_name("User")
    checkout_page.enter_zip_code("601234")
    checkout_page.click_continue()

    order_summary_page.click_finish()

    confirmation = order_summary_page.get_confirmation_message()
    assert confirmation=="Thank you for your order!",f"Expected Message not shown. got : {confirmation}"

    #click back home once order is finished
    order_summary_page.click_back_home()
    # asssert the title of page
    assert "inventory.html" in driver.current_url
