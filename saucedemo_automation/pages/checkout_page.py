from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage(BasePage):
    CHECKOUT_TITLE = (By.CLASS_NAME, "title")
    TITLE =(By.CLASS_NAME,'title')
    FIRST_NAME = (By.XPATH,"//input[@id='first-name']")
    LAST_NAME=(By.XPATH,"//input[@id='last-name']")
    ZIP_CODE=(By.XPATH,"//input[@id='postal-code']")
    CLICK_CONTINUE_BTN =(By.XPATH,"//input[@id='continue']")
    def __init__(self,driver):
        super().__init__(driver)

    def get_title(self):
        try:
           return self.driver.find_element(*self.CHECKOUT_TITLE).text
        except Exception as e:
           self.driver.save_screenshot("get_title_error.png")
           raise e
    def enter_first_name(self,firstname):
        # Wait until the element located by FIRST_NAME is visible
        try:
           WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.FIRST_NAME))
        ## Then type the firstname into the input
           self.type(self.FIRST_NAME,firstname)
        except TimeoutException as e:
           self.driver.save_screenshot("enter_first_name_timeout.png")
           raise e

    def enter_last_name(self,lastname):
        # Wait until the element located by LAST_NAME is visible
        try:
           WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.LAST_NAME))
        # Then type the lastname into the input
           self.type(self.LAST_NAME,lastname)
        except TimeoutException as e :
            self.driver.save_screenshot("enter_last_name_timeout.png")
            raise e

    def enter_zip_code(self,zip_code):
        try:
           WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.ZIP_CODE))
        #Then type the Zip Code into the input
           self.type(self.ZIP_CODE,zip_code)
        except TimeoutException as e :
            self.driver.save_screenshot("enter_zip_code_timeout.png")
            raise e


    def click_continue(self):
        try:
           WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CLICK_CONTINUE_BTN))
           self.click(self.CLICK_CONTINUE_BTN)
        except TimeoutException as e :
            self.driver.save_screenshot("click_continue_timeout.png")
            raise e

