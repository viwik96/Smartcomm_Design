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
    
    def test_warning_tc_27(self):

        comm = Common_methods(self.driver)
        warning = warnings(self.driver)

        try:
            # Step 1: Navigate to Motor1 screen
            comm.test_sample1()
            comm.test_proclick()
            warning.motor1()

            parent = self.driver.find_element(By.ID, "parent-layout")
            # Step 2: Select Motor Load 3 label 1
            motor1_label = parent.find_element(By.ID, "motor-load-3-label-1")
            ActionChains(self.driver).move_to_element(motor1_label).click().perform()

            # Step 3: Select starter type (index 2)
            Select(self.driver.find_element(By.ID, "starter-type")).select_by_index(2)
            time.sleep(2)

            # Step 4: Click Motor Load 3 label 5
            motor5_label = parent.find_element(By.ID, "motor-load-3-label-5")
            ActionChains(self.driver).move_to_element(motor5_label).click().perform()

            # Step 5: Select External Keypad (index 1)
            Select(self.driver.find_element(By.ID, "ek")).select_by_index(1)
            time.sleep(2)

            # Step 6: Click gear icon and calculate
            self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()
            self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()
            time.sleep(6)

            # Step 7: Select Motor Load 3 label 1 again
            motor1_label = parent.find_element(By.ID, "motor-load-3-label-1")
            ActionChains(self.driver).move_to_element(motor1_label).click().perform()

            # Step 8: Select operation mode (index 36)
            Select(self.driver.find_element(By.ID, "op")).select_by_index(36)
            time.sleep(2)

            # Step 9: Click gear icon and calculate again
            self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()
            self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()
            time.sleep(10)

            # Step 10: Open report
            self.driver.find_element(By.CSS_SELECTOR, ".report-card > .row > .col-12 > .btn").click()

            # Step 11: Validate warning message
            error_elem = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, "#panelsStayOpen-errorOne-1 > .accordion-body > .fs-14 > :nth-child(3) > .fs-12")
                )
            )
            actual_msg = error_elem.text.strip()
            expected_msg = "VFD Cable is not available for undefined"

            print("Validation Message:", actual_msg)
            assert actual_msg == expected_msg, f"Expected: {expected_msg}, Got: {actual_msg}"

        except Exception as e:

           print(f"[Test Failed] Reason: {e}")
           self.driver.save_screenshot("test_warning_tc_22_failed.png")
           raise

        finally:
            comm.logo()



