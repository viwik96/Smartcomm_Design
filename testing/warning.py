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

    def test_warning_tc_01(self):
        
        comm = Common_methods(self.driver)
        comm.test_sample1()
        comm.test_proclick()

        Warning = warnings(self.driver)
        Warning.single_component()

        # Step 2: Click the component inside #parent-layout
        parent_layout = self.wait.until(EC.presence_of_element_located((By.ID, "parent-layout")))
        component = parent_layout.find_element(By.ID, "lv-source-1-label-1")
        component.click()

        time.sleep(2)

        # Step 3: Click radio button with for="rbtn-result"
        radio_label = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[for="rbtn-result"]')))
        radio_label.click()

        # Step 4: Click on close image icon
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.justify-content-between > .border-0 > img'))).click()

        # Step 5: Click confirmation button in popup
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.pt-4 > div > .btn'))).click()

        time.sleep(5)

        # Step 6: Click button to open report
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.report-card > .row > .col-12 > .btn'))).click()

        # Step 7: Get the message text
        message_element = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.fs-14 > :nth-child(3)')))
        message_text = message_element.text
        print("Captured Message:", message_text)

        # Step 8: Validate message
        expected_message = "There is no load in the network"
        assert message_text == expected_message, f"Expected message '{expected_message}', but got '{message_text}'"


    def test_warning_tc_02(self):
           
        warning = warnings(self.driver)
        warning.delete_all_components()
        warning.sld_framed1_component()
    

        # Step 2: Click the component inside #parent-layout
        parent_layout = self.wait.until(EC.presence_of_element_located((By.ID, "parent-layout")))
        component = parent_layout.find_element(By.ID, "lv-source-2-label-1")
        component.click()

        time.sleep(2)

        # Step 3: Click result radio button
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[for="rbtn-result"]'))).click()

        # Step 4: Click close (img)
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.justify-content-between > .border-0 > img'))).click()

        # Step 5: Confirm action in popup
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.pt-4 > div > .btn'))).click()

        time.sleep(2)

        # Step 6: Open warning report
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.report-card > .row > .col-12 > .btn'))).click()

        # Step 7: Capture warning message
        message_element = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.fs-14 > :nth-child(3)')))
        message_text = message_element.text
        print("Captured Message:", message_text)

        # Step 8: Validate warning text
        expected_message = "The Component Circuit Breaker QA 4 is not supplied"
        assert message_text == expected_message, f"Expected message '{expected_message}', but got '{message_text}'"


    def test_warning_tc_03(self):
       
        Warning = warnings(self.driver)
        Warning.delete_all_components()
        Warning.warning_scenario_3()

        # Step 2: Click the component inside #parent-layout
        layout = self.wait.until(EC.presence_of_element_located((By.ID, "parent-layout")))
        component = layout.find_element(By.ID, "generic-load-3-label-1")
        component.click()

        time.sleep(2)

        # Step 3: Click radio button for result
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[for="rbtn-result"]'))).click()
        time.sleep(2)

        # Step 4: Input value into #ir field
        ir_field = self.wait.until(EC.element_to_be_clickable((By.ID, "ir")))
        ir_field.click()
        ir_field.clear()
        ir_field.send_keys("6500")

        # Step 5: Click close icon
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.justify-content-between > .border-0 > img'))).click()

        time.sleep(2)

        # Step 6: Confirm popup action
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.pt-4 > div > .btn'))).click()

        time.sleep(10)

        # Step 7: Open warning report
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.report-card > .row > .col-12 > .btn'))).click()

        # Step 8: Capture and validate the warning message
        message_elem = self.wait.until(EC.visibility_of_element_located((
            By.CSS_SELECTOR,
            '#panelsStayOpen-errorOne-1 > .accordion-body > .fs-14 > :nth-child(3)'
        )))
        actual_message = message_elem.text.strip()

        expected_message = (
            "Circuit Breaker with Rated current >= 6500 is not available. "
            "Pl. contact the customer interaction centre"
        )

        print("Captured Message:", actual_message)
        assert actual_message == expected_message, f"Expected: '{expected_message}', but got: '{actual_message}'"