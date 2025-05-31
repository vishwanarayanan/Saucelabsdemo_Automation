from selenium.webdriver.common.by import By
from selenium import webdriver

class LoginPage:
     def __init__(self,driver:webdriver):
         self.driver=driver

     USERNAME = (By.XPATH,"//input[@id='user-name']")
     PASSWORD = (By.XPATH,"//input[@id='password']")
     LOGIN_BTN=(By.XPATH,"//input[@id='login-button']")
     ERROR_MESSAGE=(By.XPATH,"//h3[@data-test='error']")
     def login(self,username,password):
         self.driver.find_element(*self.USERNAME).send_keys(username)
         self.driver.find_element(*self.PASSWORD).send_keys(password)
         self.driver.find_element(*self.LOGIN_BTN).click()

     def get_error_message(self):
         return self.driver.find_element(*self.ERROR_MESSAGE).text

