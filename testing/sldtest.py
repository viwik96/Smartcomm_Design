from argparse import Action
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from Pages_pack1.sign_in_page import Sign_in_page
from Pages_pack1.sldscreenpage import sldscreentest
from utils.common_methods import Common_methods
from selenium.webdriver.support.ui import Select
from utils.configuration_data import config_data
from selenium.webdriver.common.action_chains import ActionChains



pytest.mark.usefixtures("driver")
class Test_sldscreenpage:

    @pytest.fixture(autouse=True)       
    def wait_for_element(self,driver):
            self.driver = driver
            self.wait = WebDriverWait(self.driver, 10)
            self.common_methods = Common_methods(self.driver)


    def test_get_started(self): # clicking on get started button
            signin = Sign_in_page(self.driver)
            signin.get_started()
            time.sleep(40)

    
    def test_scd_tc_145(self):

        comm = Common_methods(self.driver)
        comm.test_sample1()
        time.sleep(5)
        comm.test_proclick()

        sldscreen = sldscreentest(self.driver)
        sldscreen.sld_framed_component()

        generate_btn = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pt-4 > div > .btn")))
        generate_btn.click()       
        time.sleep(6)

        reports_tab = self.wait.until(EC.visibility_of_element_located((By.ID, "Reports-tab")))
        reports_tab.click()


    

    