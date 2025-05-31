from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self,driver,timeout=10):
        self.driver= driver
        self.timeout = timeout

    def click(self,locator,timeout=None):
        element = WebDriverWait(self.driver,self.timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def find(self,locator):
        #Wait and return a visble Element
        try:
            return WebDriverWait(self.driver,self.timeout).until(
            EC.visibility_of_element_located(locator)
        )
        except TimeoutException:
            raise Exception(f"Element not visble,{locator}")

    def get_text(self,locator):
        #Get Text from an element
        return self.find(locator).text



