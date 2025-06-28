import allure
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import Cart_page
from pages.checkout_page import CheckoutPage
from pages.order_summary_page import OrderSummaryPage


@allure.description("Verify total = item total + tax with accurate rounding")
@allure.severity("Critical")
@allure.feature("Order_Summary")
@allure.story("Totals calculation")
@allure.tag("order_summary")
@pytest.mark.order_summary
def test_verify_order_summary_totals(setup):
    driver=setup

    #pageobjects
    login_page =LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = Cart_page(driver)
    checkout_page=CheckoutPage(driver)
    order_summary = OrderSummaryPage(driver)

    #Login
    login_page.login("standard_user","secret_sauce")

    #inventory page
    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_cart()

    #go to checkout
    cart_page.click_checkout()

    #fill in valid info
    checkout_page.enter_first_name("Test")
    checkout_page.enter_last_name("User")
    checkout_page.enter_zip_code("601234")
    checkout_page.click_continue()

    #Read values from order summary
    item_total = order_summary.get_item_total()
    tax = order_summary.get_tax()
    total = order_summary.get_total()

    expected_total = round(item_total + tax,2)

    assert total == expected_total ,(f"Mismatch : ${item_total} + ${tax} = ${expected_total}, but got ${total}")

    order_summary.click_finish()