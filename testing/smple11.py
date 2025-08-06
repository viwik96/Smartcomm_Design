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
    
    def test_warning_tc_53(self):

        comm = Common_methods(self.driver)
        Warning = warnings(self.driver)

        try:
                # Step 1: Setup framed component via helper function
                comm.test_proclick()
                Warning.warning_scenario_4()

                # Step 2: Click on the component
                parent = self.driver.find_element(By.ID, "parent-layout")
                breaker = self.driver.find_element(By.ID, "fdr-circuit-bbt-3-label-0").click()
                ActionChains(self.driver).move_to_element(breaker).click().perform()
                time.sleep(2)

                # Step 3: Enable the switch toggle
                select_protection = Select(self.driver.find_element(By.ID, "protection-type"))
                select_protection.select_by_index(1)
                time.sleep(1)

                parent = self.driver.find_element(By.ID, "parent-layout")
                genericload = self.driver.find_element(By.CSS_SELECTOR, "#parent-layout #generic-load-5-label-1").click()
                ActionChains(self.driver).move_to_element(genericload).click().perform()
                time.sleep(2)

                ActionChains(self.driver).move_to_element(genericload).click().perform()
                ir = self.driver.find_element(By.ID, "ir")
                ir.clear()
                ir.clear()
                ir.send_keys("2000")

                  # Step 5: Click the close or collapse image
                self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()

                # Step 6: Click the Save button
                self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()
                time.sleep(6)               

                # Step 7: Click the View Report button
                self.driver.find_element(By.CSS_SELECTOR, ".report-card > .row > .col-12 > .btn").click()

                # Step 8: Capture and validate warning message
                warning_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#panelsStayOpen-errorOne-1 > div > div > div:nth-child(3) > span"))
                )
                actual_message = warning_element.text.strip()
                expected_message = (
                "Fuse with Rated current >= 2000 is not available. Pl. contact the customer interaction centre"
                )

                assert actual_message == expected_message, f"Mismatch: Expected '{expected_message}', but got '{actual_message}'"
                print("Warning-TC-53 passed: Circuit breaker combination warning verified.")

        except Exception as e:
                print(f"[ERROR] Test failed due to: {e}")
                self.driver.save_screenshot("warning_tc_53_failure.png")
                raise

        finally:
                comm.logo()