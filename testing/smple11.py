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


    def test_warning_tc_18(self):

        comm = Common_methods(self.driver)
        Warning = warnings(self.driver)

        try:
            # Step 1: Click project and go to Motor1 screen
            comm.test_sample1()
            comm.test_proclick()
            Warning.motor1()

            # Step 2: Click on LV Source label
            parent = self.driver.find_element(By.ID, "parent-layout")
            lv_source = parent.find_element(By.ID, "lv-source-1-label-1")
            ActionChains(self.driver).move_to_element(lv_source).click().perform()

            # Step 3: Select UN dropdown (index 7)
            Select(self.driver.find_element(By.ID, "un")).select_by_index(7)
            time.sleep(2)

            # Step 4: Click gear icon and submit
            self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()
            self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()
            time.sleep(13)

            # Step 5: Click report button
            self.driver.find_element(By.CSS_SELECTOR, ".report-card > .row > .col-12 > .btn").click()

            # Step 6: Capture and validate error message
            msg_elem = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".fs-12")))
            actual_msg = msg_elem.text.strip()
            expected_msg = (
                "Type-2 Coordination chart is available for 415V & 433V. "
                "For other voltage requirements, please contact customer interaction centre"
            )

            print("Validation Message:", actual_msg)
            assert actual_msg == expected_msg, f"Expected: {expected_msg}, Got: {actual_msg}"

        except Exception as e:
            print(f"[Test Failed] Reason: {e}")
            self.driver.save_screenshot("test_warning_tc_18_failed.png")
            raise

        finally:
            comm.logo()