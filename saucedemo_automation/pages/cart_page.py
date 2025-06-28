from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage

class Cart_page(BasePage):
    def __init__(self,driver):
       #self .driver =driver   - if we dont use super() constructor timeoutexception will occur so Once you add super().__init__(driver), your Cart_page class will inherit driver, timeout, and all methods (like click(), find(), etc.) from BasePage.
        super().__init__(driver)

    CONTINUE_SHOPPING_BTN= (By.XPATH,"//button[@id ='continue-shopping']")
    CHECKOUT_BTN=(By.XPATH,"//button[@id='checkout']")

    def get_cart_items(self):
        items = self.driver.find_elements(By.CLASS_NAME,"inventory_item_name")
        return [item.text for item in items]

    def click_continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING_BTN)

    def click_checkout(self):
        self.click(self.CHECKOUT_BTN)

