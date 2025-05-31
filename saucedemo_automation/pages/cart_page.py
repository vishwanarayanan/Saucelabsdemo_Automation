from selenium.webdriver.common.by import By
from selenium import webdriver

class Cart_page:
    def __init__(self,driver):
       self .driver =driver


    def get_cart_items(self):
        items = self.driver.find_elements(By.CASS_NAME,"inventory_item n")
