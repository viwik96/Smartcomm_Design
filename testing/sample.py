import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from pages_pack.sign_in_pack.sign_in_page import Sign_in_page
from utils.common_methods import Common_methods
from selenium.webdriver.support.ui import Select
from utils.configuration_data import config_data
from selenium.webdriver.common.action_chains import ActionChains
   
@pytest.mark.usefixtures("driver")
class Test_Single:
   
    def wait_for_element(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.common_methods = Common_methods(self.driver)
       
    ## get start the application
    def test_get_started(self): # clicking on get started button
        signin = Sign_in_page(self.driver)
        signin.get_started()
        time.sleep(40)

    def test_1(self):
        comm = Common_methods(self.driver)
        comm.test_sample1()
        comm.test_proclick()
        self.wait.until(EC.presence_of_element_located((By.ID, "settings-tab"))).click()
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']"))).click()
        time.sleep(2)
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, " #simulate-tab-pane > div > div.ng-star-inserted > div > div > div.col-12.text-center.px-0 > button"))).click()
        message = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#panelsStayOpen-errorOne-0 > div > div > div:nth-child(3) > span"))).text
        print(message)
       