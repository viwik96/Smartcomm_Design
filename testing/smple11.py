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
    
    def test_warning_tc_30(self):
        
        comm = Common_methods(self.driver)
        warning = warnings(self.driver)

        try:
            # Step 1: Navigate to Earthing System page
            comm.test_sample1()
            comm.test_proclick()
            warning.earthingsys2()

            # Step 2: Click gear icon and Calculate button
            self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()
            time.sleep(5)

            # Step 3: Click Report button
            self.driver.find_element(By.CSS_SELECTOR, ".report-card > .row > .col-12 > .btn").click()

            # Step 4: Validate error message
            error_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, "#panelsStayOpen-errorOne-0 > .accordion-body > .fs-14 > :nth-child(3) > .fs-12")
                )
            )
            actual_msg = error_element.text.strip()
            expected_msg = "The component LV CB QA 3 is never closed, try adding scenario."

            print("Validation Message:", actual_msg)
            assert actual_msg == expected_msg, f"Expected: {expected_msg}, Got: {actual_msg}"

        except Exception as e:
                
                print(f"[Test Failed] Reason: {e}")
                self.driver.save_screenshot("test_warning_tc_22_failed.png")
                raise

        finally:
            comm.logo()



