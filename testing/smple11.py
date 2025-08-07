from argparse import Action
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from Pages_pack1.sign_in_page import Sign_in_page
from Pages_pack1.sldscreenpage import sldscreentest
from Pages_pack1.warningpage import warnings
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
    
    def test_warning_tc_57(self):

        comm = Common_methods(self.driver)
        Warning = warnings(self.driver)
       

        try:
                # Step 1: Setup framed component via helper function
                comm.test_sample1()
                comm.test_proclick()
                Warning.sld_framed_component()              

                # Step 2: Click on the component
                time.sleep(2)
                self.driver.find_element(By.ID, "parent-layout")
                self.driver.find_element(By.ID, "motor-load-3-label-3").click()
                time.sleep(2)

                scpdtype = self.wait.until(EC.presence_of_element_located((By.ID, "protection-type")))
                Select(scpdtype).select_by_index(2)
                time.sleep(2)

                self.driver.find_element(By.ID, "motor-load-3-label-1").click()
                Motor_kw = self.wait.until(EC.presence_of_element_located((By.ID, "op")))
                Select(Motor_kw).select_by_index(41)
                time.sleep(2)

                # Step 5: Click the close or collapse image
                self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()

                self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()
                time.sleep(10)             

                # Step 7: Click the View Report button
                self.driver.find_element(By.CSS_SELECTOR, ".report-card > .row > .col-12 > .btn").click()

                # Step 8: Capture and validate warning message
                warning_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#panelsStayOpen-errorOne-1 > div > div > div:nth-child(3) > span"))
                )
                actual_message = warning_element.text.strip()
                expected_message = (
                "Circuit breaker is not available with the combination Feeder DOL, Type IE3 and 375 kw"
                )

                assert actual_message == expected_message, f"Mismatch: Expected '{expected_message}', but got '{actual_message}'"
                print("Warning-TC-56 passed: Circuit breaker combination warning verified.")

        except Exception as e:
                print(f"[ERROR] Test failed due to: {e}")
                self.driver.save_screenshot("warning_tc_56_failure.png")
                raise

        finally:
                comm.logo()