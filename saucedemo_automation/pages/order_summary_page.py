from selenium.webdriver.common.by import By
from pages.base_page import BasePage
class OrderSummaryPage(BasePage):
    ITEM_TOTAL=(By.XPATH,"//div[@class='summary_subtotal_label']")
    TAX=(By.XPATH,"//div[@class='summary_tax_label']")
    TOTAL=(By.XPATH,"//div[@class='summary_total_label']")
    CLICK_FINISH_BTN= (By.XPATH,"//button[@id='finish']")
    CONFIRM_TXT_MSG=(By.XPATH,"//h2[@class='complete-header']")
    CLICK_BACK_HOME_BTN=(By.XPATH,"//button[contains(text(),'Back Home')]")

    def __init__(self,driver):
        super().__init__(driver)# Pass driver to BasePage
        self.driver=driver  # Store driver locally

    def get_item_total(self):
        text = self.driver.find_element(*self.ITEM_TOTAL).text
        return float(text.split('$')[1])

    def get_tax(self):
        text =self.driver.find_element(*self.TAX).text
        return float(text.split('$')[1])

    def get_total(self):
        text=self.driver.find_element(*self.TOTAL).text
        return float(text.split('$')[1])

    def click_finish(self):
        self.click(self.CLICK_FINISH_BTN)

    def get_confirmation_message(self):
        return self.driver.find_element(*self.CONFIRM_TXT_MSG).text

    def click_back_home(self):
        self.click(self.CLICK_BACK_HOME_BTN)