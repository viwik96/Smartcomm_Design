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
        Warning = warnings(self.driver)

        try:
            comm.test_sample1()
            comm.test_proclick()

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

        except Exception as e:

            print(f"Error in test_warning_tc_01: {e}")
            self.driver.save_screenshot("test_warning_tc_01_error.png")
            raise  # Optional: Re-raise if test failure needs to be reported

        


    def test_warning_tc_02(self):
        warning = warnings(self.driver)
        comm = Common_methods(self.driver)

        try:
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

        except Exception as e:
            print(f"Error in test_warning_tc_02: {e}")
            self.driver.save_screenshot("test_warning_tc_02_error.png")
            raise

        finally:
            comm.logo()


    def test_warning_tc_03(self):

        comm = Common_methods(self.driver)

        try:
            comm.test_proclick()

            Warning = warnings(self.driver)
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

        except Exception as e:
            print(f"Error in test_warning_tc_03: {e}")
            self.driver.save_screenshot("test_warning_tc_03_error.png")
            raise

        finally:
            comm.logo()

    def test_warning_tc_4(self):

        comm = Common_methods(self.driver)

        try:
            comm.test_proclick()

            Warning = warnings(self.driver)
            Warning.warning_scenario_4()

            # Step 2: Click on source
            source = self.wait.until(EC.element_to_be_clickable((By.ID, "lv-source-1-label-1")))
            source.click()

            # Step 3: Select UN value
            un_dropdown = self.wait.until(EC.presence_of_element_located((By.ID, "un")))
            Select(un_dropdown).select_by_index(5)
            time.sleep(2)

            # Step 4: Click on generic load
            generic_load = self.wait.until(EC.element_to_be_clickable((By.ID, "generic-load-5-label-3")))
            generic_load.click()
            time.sleep(2)

            # Step 5: Select Standard value
            standard_dropdown = self.wait.until(EC.presence_of_element_located((By.ID, "standard")))
            Select(standard_dropdown).select_by_index(1)

            # Step 6: Click tick button (top-right image)
            tick_btn = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-between > .border-0 > img")))
            tick_btn.click()
            time.sleep(2)

            # Step 7: Click "Yes" button
            yes_btn = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pt-4 > div > .btn")))
            yes_btn.click()
            time.sleep(10)

            # Step 8: Click "View Warning" button
            view_warning_btn = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".report-card > .row > .col-12 > .btn")))
            view_warning_btn.click()

            # Step 9: Get warning text and assert
            message_elem = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ":nth-child(3) > .fs-12")))
            actual_message = message_elem.text.strip()

            print("Warning Message:", actual_message)
            expected_message = "Circuit Breaker Standard has been changed to IEC 60947-2"
            assert actual_message == expected_message, f"Expected '{expected_message}', but got '{actual_message}'"

        except Exception as e:
            print(f"Error in test_warning_tc_4: {e}")
            self.driver.save_screenshot("test_warning_tc_4_error.png")
            raise

        finally:
            comm.logo()

    def test_warning_tc_5(self):
        comm = Common_methods(self.driver)

        try:
            comm.test_proclick()

            Warning = warnings(self.driver)
            Warning.warning_scenario_3()

            actions = ActionChains(self.driver)

            # Step 2: Click on lv-source-1-label-1 inside #parent-layout
            parent_layout = self.driver.find_element(By.ID, "parent-layout")
            lv_source = parent_layout.find_element(By.ID, "lv-source-1-label-1")
            actions.move_to_element(lv_source).click().perform()

            # Step 3: Select 9th option in #un
            select_un = Select(self.driver.find_element(By.ID, "un"))
            select_un.select_by_index(9)
            time.sleep(2)

            # Step 4: Click on generic-load-3-label-3 inside #parent-layout
            generic_load = parent_layout.find_element(By.ID, "generic-load-3-label-3")
            actions.move_to_element(generic_load).click().perform()
            time.sleep(2)

            # Step 5: Select 1st option in #protection-type
            select_protection = Select(self.driver.find_element(By.ID, "protection-type"))
            select_protection.select_by_index(1)
            time.sleep(1)

            # Step 6: Click image inside .justify-content-between > .border-0 > img
            img_button = self.wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".justify-content-between > .border-0 > img")))
            img_button.click()
            time.sleep(2)

            # Step 7: Click on submit button .pt-4 > div > .btn
            submit_button = self.wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".pt-4 > div > .btn")))
            submit_button.click()
            time.sleep(10)

            # Step 8: Click report button .report-card > .row > .col-12 > .btn
            report_button = self.wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".report-card > .row > .col-12 > .btn")))
            report_button.click()

            # Step 9: Get error message text
            error_selector = "#panelsStayOpen-errorOne-1 > .accordion-body > .fs-14 > :nth-child(3) > .fs-12"
            error_message_element = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, error_selector)))
            message = error_message_element.text.strip()

            print("Validation Message:", message)

            expected_message = (
                "Fuses are available upto 415V. For higher system voltage, Please change the Fuse to Circuit breaker"
            )

            assert message == expected_message, f"Expected message does not match. Got: {message}"

        except Exception as e:
            print(f"Error in test_warning_tc_5: {e}")
            self.driver.save_screenshot("test_warning_tc_5_error.png")
            raise

        finally:
            comm.logo()


    def test_warning_tc_6(self):
        comm = Common_methods(self.driver)

        try:
            comm.test_proclick()

            Warning = warnings(self.driver)
            Warning.warning_scenario_3()
            actions = ActionChains(self.driver)

            # Step 2: Click on lv-source-1-label-1 inside #parent-layout
            parent_layout = self.driver.find_element(By.ID, "parent-layout")
            lv_source1 = parent_layout.find_element(By.ID, "lv-source-1-label-1")
            actions.move_to_element(lv_source1).click().perform()

            # Step 3: Select 5th option in #un dropdown
            select_un = Select(self.driver.find_element(By.ID, "un"))
            select_un.select_by_index(5)
            time.sleep(2)

            # Step 4: Click calculate image
            calc_img = self.wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".justify-content-between > .border-0 > img")))
            calc_img.click()

            # Step 5: Click calculate submit button
            submit_btn = self.wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".pt-4 > div > .btn")))
            submit_btn.click()
            time.sleep(10)

            # Step 6: Click lv-source-1-label-3
            lv_source3 = parent_layout.find_element(By.ID, "lv-source-1-label-3")
            actions.move_to_element(lv_source3).click().perform()
            time.sleep(2)

            # Step 7: Click lock/unlock image
            lock_unlock_img = self.driver.find_element(By.CSS_SELECTOR, "img[alt='Lock/Un-Lock']")
            lock_unlock_img.click()

            # Step 8: Click on generic-load-3-label-1
            gen_load = parent_layout.find_element(By.ID, "generic-load-3-label-1")
            actions.move_to_element(gen_load).click().perform()

            # Step 9: Input '400' in #ir field
            ir_input = self.driver.find_element(By.ID, "ir")
            ir_input.click()
            ir_input.clear()
            ir_input.send_keys("400")

            # Step 10: Re-click calculate and submit
            calc_img = self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img")
            calc_img.click()
            time.sleep(2)

            submit_btn = self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn")
            submit_btn.click()

            # Step 11: Click report button
            report_btn = self.wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".report-card > .row > .col-12 > .btn")))
            report_btn.click()

            # Step 12: Get and assert the warning message
            msg_element = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".fs-12")))
            actual_message = msg_element.text.strip()

            expected_message = (
                "Circuit Breaker QA 1 Rating 100 A is insufficient for the design current (400.00 A). Unlock the circuit breaker for alternate product selection"
            )

            print("Validation Message:", actual_message)
            assert actual_message == expected_message, f"Expected: {expected_message}, Got: {actual_message}"

        except Exception as e:
            print(f"Error in test_warning_tc_6: {e}")
            self.driver.save_screenshot("test_warning_tc_6_error.png")
            raise

        finally:
            comm.logo()

    """ def test_warning_tc_7(self):
        comm = Common_methods(self.driver)

        try:
            comm.test_proclick()

            Warning = warnings(self.driver)
            Warning.warning_scenario_4()
            actions = ActionChains(self.driver)

            # Step 2: Click on fdr-circuit-bbt-3-label-0 inside #parent-layout
            parent_layout = self.driver.find_element(By.ID, "parent-layout")
            label = parent_layout.find_element(By.ID, "fdr-circuit-bbt-3-label-0")
            actions.move_to_element(label).click().perform()

            # Step 3: Clear and type 6500 into #ib
            ib_input = self.driver.find_element(By.ID, "ib")
            ib_input.click()
            ib_input.clear()
            ib_input.send_keys("6500")
            time.sleep(2)

            # Step 4: Click calculate image
            calc_icon = self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img")
            calc_icon.click()

            # Step 5: Click calculate submit button
            submit_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pt-4 > div > .btn")))
            submit_button.click()

            # Step 6: Wait for result and open report
            time.sleep(15)
            report_btn = self.wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".report-card > .row > .col-12 > .btn")))
            report_btn.click()

            # Step 7: Validate the error message
            message_element = self.wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".fs-14 > :nth-child(3)")))
            actual_message = message_element.text.strip()

            expected_message = (
                "Circuit Breaker with Rated current >= 6500 is not available. Pl. contact the customer interaction centre"
            )

            print("Validation Message:", actual_message)
            assert actual_message == expected_message, f"Expected: {expected_message}, Got: {actual_message}"

        except Exception as e:
            print(f"Error in test_warning_tc_7: {e}")
            self.driver.save_screenshot("test_warning_tc_7_error.png")
            raise

        finally:
            comm.logo() """ 

    def test_warning_tc_8(self):
        comm = Common_methods(self.driver)

        try:
            # Step 1: Initial project click
            comm.test_proclick()

            # Step 2: Trigger Warning Scenario
            Warning = warnings(self.driver)
            Warning.warning_scenario_4()
            actions = ActionChains(self.driver)

            # Step 3: Click the LV source label
            parent_layout = self.driver.find_element(By.ID, "parent-layout")
            lv_source_label = parent_layout.find_element(By.ID, "lv-source-1-label-1")
            actions.move_to_element(lv_source_label).click().perform()

            # Step 4: Select 10th option from UN dropdown
            un_dropdown = Select(self.driver.find_element(By.ID, "un"))
            un_dropdown.select_by_index(9)
            time.sleep(2)

            # Step 5: Click the calculate (gear) icon
            self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()

            # Step 6: Click the calculate submit button
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pt-4 > div > .btn"))).click()

            # Step 7: Wait and click report card button
            time.sleep(15)
            self.wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".report-card > .row > .col-12 > .btn"))).click()

            # Step 8: Capture the warning message
            message_element = self.wait.until(EC.visibility_of_element_located((
                By.CSS_SELECTOR, "#panelsStayOpen-errorOne-0 > div > div > div:nth-child(3) > span"
            )))
            actual_message = message_element.text.strip()

            # Step 9: Assert the expected message
            expected_message = (
                "Load Power factor 0.85 is less than the default required power factor (0.9). "
                "Capacitor Bank must be included in the installation"
            )

            print("Validation Message:", actual_message)
            assert actual_message == expected_message, f"Expected: {expected_message}, Got: {actual_message}"

        except Exception as e:
            print(f"Error in test_warning_tc_8: {e}")
            self.driver.save_screenshot("test_warning_tc_8_error.png")
            raise

        finally:
            comm.logo()

    def test_warning_tc_9(self):
        comm = Common_methods(self.driver)

        try:
            # Step 1: Navigate to project
            comm.test_proclick()

            # Step 2: Open warning scenario
            Warning = warnings(self.driver)
            Warning.warning_scenario_4()
            actions = ActionChains(self.driver)

            # Step 3: Click on source label
            parent_layout = self.driver.find_element(By.ID, "parent-layout")
            lv_source = parent_layout.find_element(By.ID, "lv-source-1-label-1")
            actions.move_to_element(lv_source).click().perform()

            # Step 4: Select 6th value in UN dropdown
            Select(self.driver.find_element(By.ID, "un")).select_by_index(5)
            time.sleep(2)

            # Step 5: Click feeder circuit
            feeder = parent_layout.find_element(By.ID, "fdr-circuit-bbt-3-label-0")
            actions.move_to_element(feeder).click().perform()

            # Step 6: Select standard dropdown value (index 1)
            Select(self.driver.find_element(By.ID, "standard")).select_by_index(1)
            time.sleep(2)

            # Step 7: Click calculate gear icon
            self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()

            # Step 8: Click calculate submit button
            self.wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".pt-4 > div > .btn"))).click()

            # Step 9: Open report card
            time.sleep(15)
            self.wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".report-card > .row > .col-12 > .btn"))).click()

            # Step 10: Validate warning message
            message_elem = self.wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ":nth-child(3) > .fs-12")))
            actual_message = message_elem.text.strip()

            expected_message = "Circuit Breaker Standard has been changed to IEC 60947-2"

            print("Validation Message:", actual_message)
            assert actual_message == expected_message, f"Expected: {expected_message}, Got: {actual_message}"

        except Exception as e:
            print(f"Error in test_warning_tc_9: {e}")
            self.driver.save_screenshot("test_warning_tc_9_error.png")
            raise

        finally:
            comm.logo()
    
   
    def test_warning_tc_10(self):
        comm = Common_methods(self.driver)

        try:
            # Step 1: Navigate to project
            comm.test_proclick()

            # Step 2: Load warning scenario
            Warning = warnings(self.driver)
            Warning.warning_scenario_4()
            actions = ActionChains(self.driver)

            # Step 3: Click LV Source 1
            parent_layout = self.driver.find_element(By.ID, "parent-layout")
            lv_source = parent_layout.find_element(By.ID, "lv-source-1-label-1")
            actions.move_to_element(lv_source).click().perform()

            # Step 4: Set Voltage UN to index 5
            Select(self.driver.find_element(By.ID, "un")).select_by_index(5)
            time.sleep(2)

            # Step 5: Click gear icon to calculate
            self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()

            # Step 6: Click submit button
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pt-4 > div > .btn"))).click()

            # Step 7: Wait for calculation to complete
            time.sleep(20)

            # Step 8: Click feeder circuit
            feeder = parent_layout.find_element(By.ID, "fdr-circuit-bbt-3-label-0")
            actions.move_to_element(feeder).click().perform()
            time.sleep(2)

            # Step 9: Click lock/unlock icon
            self.driver.find_element(By.CSS_SELECTOR, "img[alt='Lock/Un-Lock']").click()

            # Step 10: Click on Load
            load = parent_layout.find_element(By.ID, "generic-load-5-label-1")
            actions.move_to_element(load).click().perform()

            # Step 11: Set current IR to 400
            ir_input = self.driver.find_element(By.ID, "ir")
            ir_input.click()
            ir_input.clear()
            ir_input.send_keys("400")
            time.sleep(1)

            # Step 12: Recalculate
            self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()
            time.sleep(2)

            # Step 13: Submit again
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pt-4 > div > .btn"))).click()

            # Step 14: Open report card
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".report-card > .row > .col-12 > .btn"))).click()

            # Step 15: Validate message
            message_elem = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".fs-12")))
            actual_message = message_elem.text.strip()

            expected_message = (
                "Circuit Breaker QA 3 Rating 100 A is insufficient for the design current (400.00 A). "
                "Unlock the circuit breaker for alternate product selection"
            )

            print("Validation Message:", actual_message)
            assert actual_message == expected_message, f"Expected: {expected_message}, Got: {actual_message}"

        except Exception as e:
            print(f"Error in test_warning_tc_10: {e}")
            self.driver.save_screenshot("test_warning_tc_10_error.png")
            raise

        finally:
            comm.logo()

    def test_warning_tc_11(self):
        comm = Common_methods(self.driver)

        try:
            # Step 1: Load project and scenario
            comm.test_proclick()
            Warning = warnings(self.driver)
            Warning.warning_scenario_3()
            actions = ActionChains(self.driver)

            # Step 2: Click Load component
            parent = self.driver.find_element(By.ID, "parent-layout")
            load = parent.find_element(By.ID, "generic-load-3-label-3")
            actions.move_to_element(load).click().perform()
            time.sleep(2)

            # Step 3: Select Protection Type (index 1)
            Select(self.driver.find_element(By.ID, "protection-type")).select_by_index(1)
            time.sleep(2)

            # Step 4: Click LV Source component
            lv_source = parent.find_element(By.ID, "lv-source-1-label-1")
            actions.move_to_element(lv_source).click().perform()

            # Step 5: Select Voltage (UN index 9 => 690V)
            Select(self.driver.find_element(By.ID, "un")).select_by_index(9)

            # Step 6: Click gear icon to calculate
            self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()
            time.sleep(2)

            # Step 7: Submit the calculation
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pt-4 > div > .btn"))).click()

            # Step 8: Wait for the backend to complete
            time.sleep(10)

            # Step 9: Open warning report
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".report-card > .row > .col-12 > .btn"))).click()

            # Step 10: Get and validate the warning message
            message_elem = self.wait.until(EC.visibility_of_element_located((
                By.CSS_SELECTOR, "#panelsStayOpen-errorOne-1 > div > div > div:nth-child(3) > span"
            )))
            actual_message = message_elem.text.strip()
            expected_message = "Fuses are available upto 415V. For higher system voltage, Please change the Fuse to Circuit breaker"

            print("Validation Message:", actual_message)
            assert actual_message == expected_message, f"Expected: {expected_message}, Got: {actual_message}"

        except Exception as e:
            print(f"Test failed due to error: {e}")
            self.driver.save_screenshot("test_warning_tc_11_failure.png")
            raise

        finally:
            comm.logo()


    def test_warning_tc_12(self):
        comm = Common_methods(self.driver)

        try:
            # Step 1: Open project and scenario
            comm.test_proclick()
            Warning = warnings(self.driver)
            Warning.warning_scenario_3()
            actions = ActionChains(self.driver)

            # Step 2: Click on Load-3 Label-3
            parent = self.driver.find_element(By.ID, "parent-layout")
            load3 = parent.find_element(By.ID, "generic-load-3-label-3")
            actions.move_to_element(load3).click().perform()
            time.sleep(2)

            # Step 3: Select protection type index 1 (Fuse)
            Select(self.driver.find_element(By.ID, "protection-type")).select_by_index(1)
            time.sleep(2)

            # Step 4: Click on Load-3 Label-1
            load1 = parent.find_element(By.ID, "generic-load-3-label-1")
            actions.move_to_element(load1).click().perform()

            # Step 5: Set current IR to 1300
            ir_input = self.driver.find_element(By.ID, "ir")
            ir_input.click()
            ir_input.clear()
            ir_input.send_keys("1300")

            # Step 6: Click calculate gear icon
            self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()
            time.sleep(2)

            # Step 7: Click Submit button
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pt-4 > div > .btn"))).click()
            time.sleep(5)

            # Step 8: Open Report View
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".report-card > .row > .col-12 > .btn"))).click()

            # Step 9: Fetch and validate error message
            message_elem = self.wait.until(EC.visibility_of_element_located((
                By.CSS_SELECTOR, "#panelsStayOpen-errorOne-1 > .accordion-body > .fs-14 > :nth-child(3)"
            )))
            actual_message = message_elem.text.strip()
            expected_message = "Fuse with Rated current >= 1300 is not available. Pl. contact the customer interaction centre"

            print("Validation Message:", actual_message)
            assert actual_message == expected_message, f"Expected: {expected_message}, Got: {actual_message}"

        except Exception as e:
            print(f"Test failed: {e}")
            self.driver.save_screenshot("test_warning_tc_12_failure.png")
            raise

        finally:
            comm.logo() 

    def test_warning_tc_13(self):
            comm = Common_methods(self.driver)
            Warning = warnings(self.driver)
            actions = ActionChains(self.driver)

            try:
                # Step 1: Launch project and navigate
                comm.test_proclick()
                Warning.warning_scenario_3()

                # Step 2: Click LV Source
                parent_layout = self.driver.find_element(By.ID, "parent-layout")
                lv_source_label = parent_layout.find_element(By.ID, "lv-source-1-label-1")
                actions.move_to_element(lv_source_label).click().perform()

                # Step 3: Select UN dropdown index 5
                Select(self.driver.find_element(By.ID, "un")).select_by_index(5)

                # Step 4: Click Load-3 Label-3
                load3 = parent_layout.find_element(By.ID, "generic-load-3-label-3")
                actions.move_to_element(load3).click().perform()
                time.sleep(2)

                # Step 5: Select protection type index 1
                Select(self.driver.find_element(By.ID, "protection-type")).select_by_index(1)
                time.sleep(2)

                # Step 6: Click gear icon and submit
                self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()
                self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pt-4 > div > .btn"))).click()
                time.sleep(10)

                # Step 7: Lock/Unlock
                actions.move_to_element(parent_layout.find_element(By.ID, "generic-load-3-label-3")).click().perform()
                time.sleep(2)
                self.driver.find_element(By.CSS_SELECTOR, "img[alt='Lock/Un-Lock']").click()

                # Step 8: Click Load-3 Label-1
                actions.move_to_element(parent_layout.find_element(By.ID, "generic-load-3-label-1")).click().perform()

                # Step 9: Set IR to 500
                ir_input = self.driver.find_element(By.ID, "ir")
                ir_input.click()
                ir_input.clear()
                ir_input.send_keys("500")

                # Step 10: Gear icon + Submit again
                self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()
                time.sleep(2)
                self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()
                time.sleep(5)

                # Step 11: Open Report
                self.driver.find_element(By.CSS_SELECTOR, ".report-card > .row > .col-12 > .btn").click()
                time.sleep(2)

                # Step 12: Validate Error Message
                msg_elem = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                    "#panelsStayOpen-errorOne-0 > div > div > div:nth-child(3) > span")))
                actual_msg = msg_elem.text.strip()
                expected_msg = (
                    "Fuse QA 3 Rating 100 A is insufficient for the design current (500 A). "
                    "Unlock the Fuse for alternate product selection"
                )

                print("Validation Message:", actual_msg)
                assert actual_msg == expected_msg, f"Expected: {expected_msg}, Got: {actual_msg}"

            except Exception as e:
                print(f"[Test Failed] Reason: {e}")
                self.driver.save_screenshot("test_warning_tc_13_failed.png")
                raise

            finally:
                comm.logo()


    def test_scd_tc_144(self):

            comm = Common_methods(self.driver)
            Warning = warnings(self.driver)
            actions = ActionChains(self.driver)

            try:
                comm.test_sample1()
                comm.test_proclick()

                Warning.warning_scenario_3()

                parent_layout = self.driver.find_element(By.ID, "parent-layout")
                lv_source_label = parent_layout.find_element(By.ID, "lv-source-1-label-1")
                actions.move_to_element(lv_source_label).click().perform()

                # Step 3: Select UN dropdown value (index 5)
                un_dropdown = Select(self.driver.find_element(By.ID, "un"))
                un_dropdown.select_by_index(5)

                # Step 4: Click on Load-3 Label-3
                parent = self.driver.find_element(By.ID, "parent-layout")
                load3 = parent.find_element(By.ID, "generic-load-3-label-3")
                actions.move_to_element(load3).click().perform()
                time.sleep(2)

                # Step 5: Select protection type index 1
                Select(self.driver.find_element(By.ID, "protection-type")).select_by_index(1)
                time.sleep(2)

                # Step 6: Click gear icon and submit
                self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()
                self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pt-4 > div > .btn"))).click()
                time.sleep(10)

                # Step 7: Click Load-3 Label-3 again and lock/unlock
                actions.move_to_element(parent.find_element(By.ID, "generic-load-3-label-3")).click().perform()
                time.sleep(2)
                self.driver.find_element(By.CSS_SELECTOR, "img[alt='Lock/Un-Lock']").click()

                # Step 8: Click Load-3 Label-1
                actions.move_to_element(parent.find_element(By.ID, "generic-load-3-label-1")).click().perform()

                # Step 9: Set IR value to 500
                ir_input = self.driver.find_element(By.ID, "ir")
                ir_input.click()
                ir_input.clear()
                ir_input.send_keys("500")

                # Step 10: Click gear and submit again
                self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()
                time.sleep(2)
                self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()
                time.sleep(5)

                # Step 11: Open report
                self.driver.find_element(By.CSS_SELECTOR, ".report-card > .row > .col-12 > .btn").click()
                time.sleep(2)

                # Step 12: Fetch and validate message
                msg_elem = self.wait.until(EC.visibility_of_element_located((
                    By.CSS_SELECTOR, "#panelsStayOpen-errorOne-0 > div > div > div:nth-child(3) > span"
                )))
                actual_msg = msg_elem.text.strip()
                expected_msg = "Fuse QA 3 Rating 100 A is insufficient for the design current (500 A). Unlock the Fuse for alternate product selection"

                print("Validation Message:", actual_msg)
                assert actual_msg == expected_msg, f"Expected: {expected_msg}, Got: {actual_msg}"

            except Exception as e:

                print(f"Error in test_scd_tc_144: {e}")
                self.driver.save_screenshot("test_scd_tc_144_error.png")
                raise  # Optional: Re-raise if you want test to fail in test report

            finally:
                comm.logo()


    def test_warning_tc_15(self):
        comm = Common_methods(self.driver)

        try:
            # Step 1: Launch project and scenario
            comm.test_proclick()
            Warning = warnings(self.driver)
            Warning.warning_scenario_4()
            actions = ActionChains(self.driver)

            # Step 2: Click on feeder circuit
            parent = self.driver.find_element(By.ID, "parent-layout")
            feeder = parent.find_element(By.ID, "fdr-circuit-bbt-3-label-0")
            actions.move_to_element(feeder).click().perform()

            # Step 3: Select protection type as Fuse (index 1)
            Select(self.driver.find_element(By.ID, "protection-type")).select_by_index(1)
            time.sleep(2)

            # Step 4: Click gear icon and Submit
            self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pt-4 > div > .btn"))).click()
            time.sleep(15)

            # Step 5: Click LV Source
            lv_source = parent.find_element(By.ID, "lv-source-1-label-1")
            actions.move_to_element(lv_source).click().perform()

            # Step 6: Select voltage (UN index 9 = 690V)
            Select(self.driver.find_element(By.ID, "un")).select_by_index(9)

            # Step 7: Click gear and submit again
            self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pt-4 > div > .btn"))).click()
            time.sleep(5)

            # Step 8: Open report view
            self.driver.find_element(By.CSS_SELECTOR, ".report-card > .row > .col-12 > .btn").click()

            # Step 9: Validate the warning message
            msg_elem = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                "#panelsStayOpen-errorOne-1 > div > div > div:nth-child(3) > span")))
            actual_msg = msg_elem.text.strip()
            expected_msg = "Fuses are available upto 415V. For higher system voltage, Please change the Fuse to Circuit breaker"

            print("Validation Message:", actual_msg)
            assert actual_msg == expected_msg, f"Expected: {expected_msg}, Got: {actual_msg}"

        except Exception as e:
            print(f"Test failed: {e}")
            self.driver.save_screenshot("test_warning_tc_15_failure.png")
            raise

        finally:
            comm.logo()

    
    def test_get_started(self): # clicking on get started button
            signin = Sign_in_page(self.driver)
            signin.get_started()
            time.sleep(40)


    def test_warning_tc_16(self):

        comm = Common_methods(self.driver)
        Warning = warnings(self.driver)
        actions = ActionChains(self.driver)

        try:
            # Step 1: Precondition setup
            comm.test_sample1()
            comm.test_proclick()
            Warning.warning_scenario_4()

            # Step 2: Click LV Source
            parent = self.driver.find_element(By.ID, "parent-layout")
            lv_source = parent.find_element(By.ID, "lv-source-1-label-1")
            actions.move_to_element(lv_source).click().perform()

            # Step 3: Select UN dropdown value (index 5)
            Select(self.driver.find_element(By.ID, "un")).select_by_index(5)
            time.sleep(2)

            # Step 4: Click on Feeder circuit
            feeder = parent.find_element(By.ID, "fdr-circuit-bbt-3-label-0")
            actions.move_to_element(feeder).click().perform()
            time.sleep(2)

            # Step 5: Select Protection Type (index 1)
            Select(self.driver.find_element(By.ID, "protection-type")).select_by_index(1)
            time.sleep(2)

            # Step 6: Click gear icon and submit
            self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()
            self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()
            time.sleep(13)

            # Step 7: Click on Feeder again and lock/unlock
            actions.move_to_element(parent.find_element(By.ID, "fdr-circuit-bbt-3-label-0")).click().perform()
            self.driver.find_element(By.CSS_SELECTOR, "img[alt='Lock/Un-Lock']").click()

            # Step 8: Click Load-5 Label-1
            load = parent.find_element(By.ID, "generic-load-5-label-1")
            actions.move_to_element(load).click().perform()

            # Step 9: Set IR value to 700
            ir_input = self.driver.find_element(By.ID, "ir")
            ir_input.click()
            ir_input.clear()
            ir_input.send_keys("700")

            # Step 10: Submit configuration
            self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()
            time.sleep(2)
            self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()
            time.sleep(5)

            # Step 11: Open report
            self.driver.find_element(By.CSS_SELECTOR, ".report-card > .row > .col-12 > .btn").click()

            # Step 12: Capture and assert message
            msg_elem = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                "#panelsStayOpen-errorOne-0 > .accordion-body > .fs-14 > :nth-child(3) > .fs-12")))
            actual_msg = msg_elem.text.strip()
            expected_msg = "Fuse QA 3 Rating 100 A is insufficient for the design current (700.00 A). Unlock the Fuse for alternate product selection"

            print("Validation Message:", actual_msg)
            assert actual_msg == expected_msg, f"Expected: {expected_msg}, Got: {actual_msg}"

        except Exception as e:
            print(f"[Test Failed] Reason: {e}")
            self.driver.save_screenshot("test_warning_tc_16_failed.png")
            raise

        finally:
            comm.logo()


    def test_warning_tc_17(self):

        comm = Common_methods(self.driver)
        Warning = warnings(self.driver)
        actions = ActionChains(self.driver)

        try:
            # Step 1: Precondition setup
            comm.test_sample1()
             # Step 1: Setup and Switch2 operation
            comm.test_proclick()
            Warning.switch2()

            # Step 2: Click LV Source ST
            parent = self.driver.find_element(By.ID, "parent-layout")
            lv_source_st = parent.find_element(By.ID, "lv-source-st-1-label-1")
            actions.move_to_element(lv_source_st).click().perform()

            # Step 3: Select UN dropdown value (index 5)
            Select(self.driver.find_element(By.ID, "un")).select_by_index(5)
            time.sleep(2)

            # Step 4: Gear icon + Submit
            self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()
            self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()
            time.sleep(13)

            # Step 5: Click Feeder circuit + Lock/Unlock
            feeder = parent.find_element(By.ID, "fdr-circuit-bbt-3-label-0")
            actions.move_to_element(feeder).click().perform()
            self.driver.find_element(By.CSS_SELECTOR, "img[alt='Lock/Un-Lock']").click()

            # Step 6: Click Load-5 Label-1
            load = parent.find_element(By.ID, "generic-load-5-label-1")
            actions.move_to_element(load).click().perform()

            # Step 7: Set IR to 500
            ir_input = self.driver.find_element(By.ID, "ir")
            ir_input.click()
            ir_input.clear()
            ir_input.send_keys("500")

            # Step 8: Gear icon + Submit
            self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()
            time.sleep(2)
            self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()
            time.sleep(5)

            # Step 9: Open Report
            self.driver.find_element(By.CSS_SELECTOR, ".report-card > .row > .col-12 > .btn").click()

            # Step 10: Validate Error Message
            msg_elem = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".fs-12")))
            actual_msg = msg_elem.text.strip()
            expected_msg = "Switch QB 3 Rating 100 A is insufficient for the design current (500.00 A). Unlock the Switch for alternate product selection"

            print("Validation Message:", actual_msg)
            assert actual_msg == expected_msg, f"Expected: {expected_msg}, Got: {actual_msg}"

        except Exception as e:
            print(f"[Test Failed] Reason: {e}")
            self.driver.save_screenshot("test_warning_tc_17_failed.png")
            raise

        finally:
            comm.logo()

    
    


    


