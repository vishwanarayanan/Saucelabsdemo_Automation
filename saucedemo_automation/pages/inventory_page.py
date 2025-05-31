from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from .base_page import BasePage  # another way  from saucedemo_automation.pages.base_page import BasePage
from pages.base_page import BasePage

class InventoryPage(BasePage):
    def __init__(self,driver):
    #    self.driver=driver -->  not needed because of the below line
        super().__init__(driver)

    TITLE =(By.CLASS_NAME,"title")
    ADD_BACK_PACK_BTN= (By.XPATH,"//div[text()='Sauce Labs Backpack']/following::button[1]")
    CART_BADGE = (By.XPATH,"//div/a/span[@class='shopping_cart_badge']")


    def get_title(self):
        return self.driver.find_element(*self.TITLE).text.lower()

    def get_all_products(self):
        WebDriverWait(self.driver,10).until(EC.presence_of_all_elements_located((By.XPATH,"//div[@class='inventory_list']/div[contains(@class,'inventory_item')]"))
        )
        return  self.driver.find_elements(By.XPATH,"//div[@class='inventory_list']/div[contains(@class,'inventory_item')]")

    def sort_by_price_low_to_high(self):
        WebDriverWait(self.driver,10).until(
         EC.presence_of_all_elements_located((By.XPATH,"//select[@class='product_sort_container']"))
        )
        select_element =(self.driver.find_element(By.XPATH, "//select[@class='product_sort_container']"))
        select_sort= Select(select_element)
        select_sort.select_by_visible_text("Price (low to high)")

    def get_product_prices(self):
        #wait for all product items to be present
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH,"//div[@class='inventory_item_price']"))
        )
        #fetching product prices
        product_prices = self.driver.find_elements(By.XPATH, "//div[@class='inventory_item_price']")
        #extract float values from text
        return [float(price.text.strip().replace("$",""))for price in product_prices]

    def add_backpack_to_cart(self):
        self.click(self.ADD_BACK_PACK_BTN)

    def get_cart_badge_count(self):
        return int(self.get_text(self.CART_BADGE))

    def add_product_to_cart_by_name(self,product_name):
        Product_Xpath = f"//div[text()='{product_name}']/following::button[1]"
        locator = (By.XPATH,Product_Xpath)  #locator is a tuple which needs () when passed in click method
        self.click(locator)

