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
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#LK_Expand"))).click()
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#sld_menu_section > div > div:nth-child(6) > ul > li > button > i"))).click()
        input_element = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#scenarioName")))
        input_element.click()
        input_element.send_keys("transformer")
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#delete"))).click()
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#close"))).click()
        
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#scenario"))).click()
        select_element = self.driver.find_element(By.ID, "scenario")  
        dropdown = Select(select_element)   
        dropdown.select_by_visible_text("transformer")


        self.wait.until(EC.presence_of_element_located((By.ID, "mv-source-5-label-6"))).click()
        select_element = self.driver.find_element(By.ID, "breaker-status")  
        dropdown = Select(select_element)   
        dropdown.select_by_visible_text("Closed")
    
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#properties-tab-pane > div.d-flex.justify-content-between.mb-2 > button > img"))).click()
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']"))).click()
        time.sleep(9)
        
        #project name : jul1-14-25
        