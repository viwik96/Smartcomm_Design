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


    def test_scd_tc_144(self):

        comm = Common_methods(self.driver)
        comm.test_sample1()
        comm.test_proclick()

        Warning = warnings(self.driver)
        Warning.warning_scenario_4()
        actions = ActionChains(self.driver)

        # Step 2: Click feeder circuit
        parent = self.driver.find_element(By.ID, "parent-layout")
        feeder = parent.find_element(By.ID, "fdr-circuit-bbt-3-label-0")
        actions.move_to_element(feeder).click().perform()

        # Step 3: Set protection type to index 1 (Fuse)
        Select(self.driver.find_element(By.ID, "protection-type")).select_by_index(1)
        time.sleep(2)

        # Step 4: Click gear icon and then submit
        self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pt-4 > div > .btn"))).click()
        time.sleep(15)

        # Step 5: Click LV Source
        lv_source = parent.find_element(By.ID, "lv-source-1-label-1")
        actions.move_to_element(lv_source).click().perform()

        # Step 6: Select UN as index 9
        Select(self.driver.find_element(By.ID, "un")).select_by_index(9)

        # Step 7: Click gear icon and submit
        self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pt-4 > div > .btn"))).click()
        time.sleep(5)

        # Step 8: Open report
        self.driver.find_element(By.CSS_SELECTOR, ".report-card > .row > .col-12 > .btn").click()

        # Step 9: Capture and assert the warning message
        msg_elem = self.wait.until(EC.visibility_of_element_located((
            By.CSS_SELECTOR, "#panelsStayOpen-errorOne-1 > div > div > div:nth-child(3) > span"
        )))
        actual_msg = msg_elem.text.strip()
        expected_msg = "Fuses are available upto 415V. For higher system voltage, Please change the Fuse to Circuit breaker"

        print("Validation Message:", actual_msg)
        assert actual_msg == expected_msg, f"Expected: {expected_msg}, Got: {actual_msg}"
