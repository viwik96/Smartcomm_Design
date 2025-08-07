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

    def test_warning_tc_04(self):

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

    def test_warning_tc_05(self):
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

    def test_warning_tc_06(self):
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

    """ def test_warning_tc_07(self):
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

    def test_warning_tc_08(self):
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

    def test_warning_tc_09(self):
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

    def test_warning_tc_14(self):

            comm = Common_methods(self.driver)
            Warning = warnings(self.driver)
            actions = ActionChains(self.driver)

            try:
           
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

    def test_warning_tc_16(self):

        comm = Common_methods(self.driver)
        Warning = warnings(self.driver)
        actions = ActionChains(self.driver)

        try:

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

    def test_warning_tc_18(self):

        comm = Common_methods(self.driver)
        Warning = warnings(self.driver)

        try:
            
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

    def test_warning_tc_19(self):

        comm = Common_methods(self.driver)
        Warning = warnings(self.driver)

        try:

            comm.test_proclick()
            Warning.motor1()

            # Step 2: Click LV Source label
            parent = self.driver.find_element(By.ID, "parent-layout")
            lv_source = parent.find_element(By.ID, "lv-source-1-label-1")
            ActionChains(self.driver).move_to_element(lv_source).click().perform()

            # Step 3: Select UN dropdown (index 5)
            Select(self.driver.find_element(By.ID, "un")).select_by_index(5)
            time.sleep(2)

            # Step 4: Click gear icon and submit
            self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()
            self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()
            time.sleep(13)

            # Step 5: Click on motor-load-3 label and lock/unlock
            motor_label_3 = parent.find_element(By.ID, "motor-load-3-label-3")
            ActionChains(self.driver).move_to_element(motor_label_3).click().perform()
            self.driver.find_element(By.CSS_SELECTOR, "img[alt='Lock/Un-Lock']").click()

            # Step 6: Click motor-load-3 label-1
            motor_label_1 = parent.find_element(By.ID, "motor-load-3-label-1")
            ActionChains(self.driver).move_to_element(motor_label_1).click().perform()

            # Step 7: Select OP dropdown value (index 12)
            Select(self.driver.find_element(By.ID, "op")).select_by_index(12)
            time.sleep(2)

            # Step 8: Click gear and submit again
            self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()
           
            self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()
            time.sleep(2)

            # Step 9: Click report button
            self.driver.find_element(By.CSS_SELECTOR, ".report-card > .row > .col-12 > .btn").click()

            # Step 10: Capture and assert warning message
            msg_elem = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#panelsStayOpen-errorOne-0 > div > div > div:nth-child(3) > span")))
            actual_msg = msg_elem.text.strip()
            expected_msg = "The Circuit Breaker QA 3 Rating 4 A is insufficient for the design current (8.5 A)"

            print("Validation Message:", actual_msg)
            assert actual_msg == expected_msg, f"Expected: {expected_msg}, Got: {actual_msg}"

        except Exception as e:
            print(f"[Test Failed] Reason: {e}")
            self.driver.save_screenshot("test_warning_tc_19_failed.png")
            raise

        finally:
            comm.logo()

    def test_warning_tc_20(self):

        comm = Common_methods(self.driver)
        Warning = warnings(self.driver)

        try:
           
            comm.test_proclick()
            Warning.motor1()

            # Step 2: Click on LV Source label
            parent = self.driver.find_element(By.ID, "parent-layout")
            lv_source = parent.find_element(By.ID, "lv-source-1-label-1")
            ActionChains(self.driver).move_to_element(lv_source).click().perform()

            # Step 3: Select UN dropdown (index 9)
            Select(self.driver.find_element(By.ID, "un")).select_by_index(9)
            time.sleep(2)

            # Step 4: Click gear icon and submit
            self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()
            self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()
            time.sleep(13)

            # Step 5: Click report button
            self.driver.find_element(By.CSS_SELECTOR, ".report-card > .row > .col-12 > .btn").click()

            # Step 6: Capture and assert warning message
            msg_elem = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#panelsStayOpen-errorOne-0 > div > div > div:nth-child(3) > span")))
            actual_msg = msg_elem.text.strip()
            expected_msg = "Type-2 Coordination chart is available for 415V & 433V. For other voltage requirements, please contact customer interaction centre"

            print("Validation Message:", actual_msg)
            assert actual_msg == expected_msg, f"Expected: {expected_msg}, Got: {actual_msg}"

        except Exception as e:
            print(f"[Test Failed] Reason: {e}")
            self.driver.save_screenshot("test_warning_tc_20_failed.png")
            raise

        finally:
            comm.logo()

    def test_warning_tc_21(self):

        comm = Common_methods(self.driver)
        Warning = warnings(self.driver)

        try:
            
            comm.test_proclick()
            Warning.motor1()

            # Step 2: Click LV Source
            parent = self.driver.find_element(By.ID, "parent-layout")
            lv_source = parent.find_element(By.ID, "lv-source-1-label-1")
            ActionChains(self.driver).move_to_element(lv_source).click().perform()

            # Step 3: Select UN dropdown (index 5)
            Select(self.driver.find_element(By.ID, "un")).select_by_index(5)
            time.sleep(2)

            # Step 4: Click motor load
            motor_load_3 = parent.find_element(By.ID, "motor-load-3-label-3")
            ActionChains(self.driver).move_to_element(motor_load_3).click().perform()
            time.sleep(2)

            # Step 5: Select protection type (index 2)
            Select(self.driver.find_element(By.ID, "protection-type")).select_by_index(2)

            # Step 6: Click gear icon and calculate
            self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()
            self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()
            time.sleep(15)

            # Step 7: Re-click motor load and unlock
            motor_load_3 = parent.find_element(By.ID, "motor-load-3-label-3")
            ActionChains(self.driver).move_to_element(motor_load_3).click().perform()
            self.driver.find_element(By.CSS_SELECTOR, "img[alt='Lock/Un-Lock']").click()

            # Step 8: Click target motor label
            motor_target = parent.find_element(By.ID, "motor-load-3-label-1")
            ActionChains(self.driver).move_to_element(motor_target).click().perform()
            time.sleep(5)

            # Step 9: Set IR value = 300
            ir_input = self.driver.find_element(By.ID, "ir")
            ir_input.click()
            ir_input.clear()
            ir_input.clear()
            ir_input.send_keys("300")
            time.sleep(2)

            # Step 10: Recalculate
            self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()
            self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()
            time.sleep(10)

            # Step 11: Open report
            self.driver.find_element(By.CSS_SELECTOR, ".report-card > .row > .col-12 > .btn").click()

            # Step 12: Validate warning message
            msg_elem = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".fs-14 > :nth-child(3)")))
            actual_msg = msg_elem.text.strip()
            expected_msg = "The Fuse QA 3 Rating 8 A is insufficient for the design current (300 A)"

            print("Validation Message:", actual_msg)
            assert actual_msg == expected_msg, f"Expected: {expected_msg}, Got: {actual_msg}"

        except Exception as e:
            print(f"[Test Failed] Reason: {e}")
            self.driver.save_screenshot("test_warning_tc_21_failed.png")
            raise

        finally:
            comm.logo()
    
    def test_warning_tc_22(self):
        comm = Common_methods(self.driver)
        Warning = warnings(self.driver)

        try:
            # Step 1: Navigate to Coupling1 screen
            comm.test_proclick()
            Warning.coupling2()

            # Step 2: Add new scenario
            self.driver.find_element(By.CSS_SELECTOR, "i.bi.bi-plus").click()
            self.driver.find_element(By.ID, "scenarioName").send_keys("s2")
            self.driver.find_element(By.ID, "delete").click()
            time.sleep(2)

            parent = self.driver.find_element(By.CSS_SELECTOR,"body > modal-container > div.modal-dialog.modal-dialog-centered.new-popup-xs > div")
            cancelbutton = parent.find_element(By.ID, "close")
            ActionChains(self.driver).move_to_element(cancelbutton).click().perform()

            # Step 3: Select scenario (index 1)
            Select(self.driver.find_element(By.ID, "scenario")).select_by_index(1)
            time.sleep(2)

            # Step 4: Click LV Source
            parent = self.driver.find_element(By.ID, "parent-layout")
            lv_source = parent.find_element(By.ID, "lv-source-7-label-3")
            ActionChains(self.driver).move_to_element(lv_source).click().perform()

            # Step 5: Select breaker status
            Select(self.driver.find_element(By.ID, "breaker-status")).select_by_index(1)

            # Step 6: Click gear icon and calculate
            self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()
            self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()
            time.sleep(15)

            # Step 7: Wait for simulate button
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#simulate-tab-pane > .pt-4 > div > .btn"))
            )

            time.sleep(15)
            coupler = parent.find_element(By.ID, "coupler-4-label-1")
            ActionChains(self.driver).move_to_element(coupler).click().perform()
            self.driver.find_element(By.CSS_SELECTOR, "img[alt='Lock/Un-Lock']").click()

            # Step 9: Click generic load label
            load = parent.find_element(By.ID, "generic-load-3-label-1")
            ActionChains(self.driver).move_to_element(load).click().perform()

            # Step 10: Set IR value
            ir_input = self.driver.find_element(By.ID, "ir")
            ir_input.click()
            ir_input.clear()
            ir_input.clear()
            ir_input.send_keys("300")

            # Step 11: Recalculate
            self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()
            time.sleep(2)
            self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()
            time.sleep(5)

            # Step 12: Open report and verify message
            self.driver.find_element(By.CSS_SELECTOR, ".report-card > .row > .col-12 > .btn").click()
            msg_elem = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".fs-14 > :nth-child(3)")))
            actual_msg = msg_elem.text.strip()
            expected_msg = (
                 
                "Switch QB 4 Rating 100 A is insufficient for the design current (300 A). Unlock the Switch for alternate product selection"
            )

            print("Validation Message:", actual_msg)
            assert actual_msg == expected_msg, f"Expected: {expected_msg}, Got: {actual_msg}"

        except Exception as e:
            print(f"[Test Failed] Reason: {e}")
            self.driver.save_screenshot("test_warning_tc_22_failed.png")
            raise

        finally:
            comm.logo()
    
    
    def test_warning_tc_23(self):

        common = Common_methods(self.driver)
        warning_page = warnings(self.driver)

        try:
            
            common.test_proclick()
            warning_page.coupling2()

            # Step 2: Add and delete scenario
            self.driver.find_element(By.CSS_SELECTOR, "i.bi.bi-plus").click()
            self.driver.find_element(By.ID, "scenarioName").send_keys("s1")
            self.driver.find_element(By.ID, "delete").click()
            time.sleep(2)
            parent = self.driver.find_element(By.CSS_SELECTOR,"body > modal-container > div.modal-dialog.modal-dialog-centered.new-popup-xs > div")
            cancelbutton = parent.find_element(By.ID, "close")
            ActionChains(self.driver).move_to_element(cancelbutton).click().perform()

            # Step 3: Select scenario index 1
            Select(self.driver.find_element(By.ID, "scenario")).select_by_index(1)
            time.sleep(2)

            # Step 4: Click LV Source
            parent = self.driver.find_element(By.ID, "parent-layout")
            lv_source = parent.find_element(By.ID, "lv-source-7-label-3")
            ActionChains(self.driver).move_to_element(lv_source).click().perform()

            # Step 5: Select breaker status
            Select(self.driver.find_element(By.ID, "breaker-status")).select_by_index(1)

            # Step 6: Gear icon and calculate
            self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()
            self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()
            time.sleep(15)

            # Step 7: Wait until simulate button is visible
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#simulate-tab-pane > .pt-4 > div > .btn"))
            )

            # Step 8: Click Coupler label
            time.sleep(10)
            coupler = parent.find_element(By.ID, "coupler-4-label-1")
            ActionChains(self.driver).move_to_element(coupler).click().perform()

            # Step 9: Unlock Switch
            self.driver.find_element(By.CSS_SELECTOR, "img[alt='Lock/Un-Lock']").click()

            # Step 10: Click Generic Load
            generic_load = parent.find_element(By.ID, "generic-load-3-label-1")
            ActionChains(self.driver).move_to_element(generic_load).click().perform()

            # Step 11: Set IR value to 300
            ir_input = self.driver.find_element(By.ID, "ir")
            ir_input.click()
            ir_input.clear()
            ir_input.send_keys("300")

            # Step 12: Recalculate
            self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()
            time.sleep(2)
            self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()
            time.sleep(5)

            # Step 13: Open report
            self.driver.find_element(By.CSS_SELECTOR, ".report-card > .row > .col-12 > .btn").click()

            # Step 14: Validate warning message
            msg_elem = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".fs-14 > :nth-child(3)"))
            )
            actual_msg = msg_elem.text.strip()
            expected_msg = (
                
                "Switch QB 4 Rating 100 A is insufficient for the design current (300 A). Unlock the Switch for alternate product selection"
            )

            print("Validation Message:", actual_msg)
            assert actual_msg == expected_msg, f"Expected: {expected_msg}, Got: {actual_msg}"

        except Exception as e:
           print(f"[Test Failed] Reason: {e}")
           self.driver.save_screenshot("test_warning_tc_22_failed.png")
           raise

        finally:
            common.logo()

        
    def test_warning_tc_24(self):

        warning_page = warnings(self.driver)
        comm = Common_methods(self.driver)

        try:
            # Step 1: Navigate to Warning3 screen
            comm.test_proclick()
            warning_page.warning_scenario_3()

            # Step 2: Click Generic Load label
            parent = self.driver.find_element(By.ID, "parent-layout")
            generic_load = parent.find_element(By.ID, "generic-load-3-label-3")
            ActionChains(self.driver).move_to_element(generic_load).click().perform()
            time.sleep(2)

            # Step 3: Toggle switch inside the 10th accordion group
            toggle_label = self.driver.find_element(
                By.CSS_SELECTOR,
                ":nth-child(10) > #offcanvas_accordion > .accordion-item > .accordion-header > .accordion-button > .ms-auto > .form-switch > .switchToggle > label"
            )
            toggle_label.click()
            time.sleep(2)

            # Step 4: Select RCD type (index 2)
            Select(self.driver.find_element(By.ID, "rcdType")).select_by_index(2)

            # Step 5: Recalculate
            self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()
            time.sleep(2)
            self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()
            time.sleep(10)

            # Step 6: Open Report
            self.driver.find_element(By.CSS_SELECTOR, ".report-card > .row > .col-12 > .btn").click()

            # Step 7: Validate warning message
            message_elem = self.driver.find_element(By.CSS_SELECTOR, ":nth-child(3) > .fs-12")
            actual_msg = message_elem.text.strip()
            expected_msg = (
                 
                'Circuit Breaker is not available with the combination Rated Voltage = 415, Current = 100, Pole = 4P, Withdrawable = No. Try with the Withdrawable option "Yes" or contact the customer interaction centre'
            )

            print("Validation Message:", actual_msg)
            assert actual_msg == expected_msg, f"Expected: {expected_msg}, Got: {actual_msg}"

        except Exception as e:
        
           print(f"[Test Failed] Reason: {e}")
           self.driver.save_screenshot("test_warning_tc_22_failed.png")
           raise

        finally:
            comm.logo()


    def test_warning_tc_25(self):

        warning_page = warnings(self.driver)
        comm = Common_methods(self.driver)

        try:
            # Step 1: Navigate to Warning3 screen
            comm.test_proclick()
            warning_page.warning_scenario_3()

            # Step 2: Click Generic Load label
            parent = self.driver.find_element(By.ID, "parent-layout")
            generic_load = parent.find_element(By.ID, "generic-load-3-label-3")
            ActionChains(self.driver).move_to_element(generic_load).click().perform()
            time.sleep(2)

            # Step 3: Toggle switch in the 10th accordion section
            toggle = self.driver.find_element(
                By.CSS_SELECTOR,
                ":nth-child(10) > #offcanvas_accordion > .accordion-item > .accordion-header > .accordion-button > .ms-auto > .form-switch > .switchToggle > label"
            )
            toggle.click()
            time.sleep(2)

            # Step 4: Click gear icon and Calculate
            self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()
            time.sleep(2)
            self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()
            time.sleep(10)

            # Step 5: Unlock the same Generic Load label
            ActionChains(self.driver).move_to_element(generic_load).click().perform()
            self.driver.find_element(By.CSS_SELECTOR, "img[alt='Lock/Un-Lock']").click()

            # Step 6: Select second Generic Load
            alt_generic = parent.find_element(By.ID, "generic-load-3-label-1")
            ActionChains(self.driver).move_to_element(alt_generic).click().perform()

            # Step 7: Enter IR value 300
            ir_input = self.driver.find_element(By.ID, "ir")
            ir_input.click()
            ir_input.clear()
            ir_input.send_keys("300")

            # Step 8: Recalculate
            self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()
            time.sleep(2)
            self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()
            time.sleep(5)

            # Step 9: Open Report and Validate message
            self.driver.find_element(By.CSS_SELECTOR, ".report-card > .row > .col-12 > .btn").click()
            message_elem = self.driver.find_element(By.CSS_SELECTOR, ".fs-12")
            actual_msg = message_elem.text.strip()

            expected_msg = (
                 
               "Circuit Breaker QA 3 Rating 100 A is insufficient for the design current (300 A). Unlock the circuit breaker for alternate product selection"
            )

            print("Validation Message:", actual_msg)
            assert actual_msg == expected_msg, f"Expected: {expected_msg}, Got: {actual_msg}"

        except Exception as e:
           
           print(f"[Test Failed] Reason: {e}")
           self.driver.save_screenshot("test_warning_tc_22_failed.png")
           raise

        finally:
            comm.logo()


    def test_warning_tc_26(self):

        warning_page = warnings(self.driver)
        comm = Common_methods(self.driver)

        try:
            # Step 1: Navigate to Motor1 screen
            comm.test_proclick()
            warning_page.motor1()

            # Step 2: Click on Motor Load 3 Label 1
            parent_layout = self.driver.find_element(By.ID, "parent-layout")
            motor_label_1 = parent_layout.find_element(By.ID, "motor-load-3-label-1")
            ActionChains(self.driver).move_to_element(motor_label_1).click().perform()

            # Step 3: Select Starter Type (Dropdown index 2)
            Select(self.driver.find_element(By.ID, "starter-type")).select_by_index(2)
            time.sleep(2)

            # Step 4: Click calculate (gear icon + simulate button)
            self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()
            self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()
            time.sleep(13)

            # Step 5: Click Motor Load 3 Label 5 and unlock
            motor_label_5 = parent_layout.find_element(By.ID, "motor-load-3-label-5")
            ActionChains(self.driver).move_to_element(motor_label_5).click().perform()
            self.driver.find_element(By.CSS_SELECTOR, "img[alt='Lock/Un-Lock']").click()

            # Step 6: Re-click Motor Load 3 Label 1 and set Operating Point (OP) index 10
            ActionChains(self.driver).move_to_element(motor_label_1).click().perform()
            Select(self.driver.find_element(By.ID, "op")).select_by_index(10)

            # Step 7: Recalculate
            self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()
            self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()
            time.sleep(5)

            # Step 8: Open Report & validate error message
            self.driver.find_element(By.CSS_SELECTOR, ".report-card > .row > .col-12 > .btn").click()
            actual_message = self.driver.find_element(By.CSS_SELECTOR, ".fs-12").text.strip()

            expected_message = (
                 
                "VFD TA 3 (4 A) rating is insufficient for Motor full load current (6 A). Please unlock VFD"
            )

            assert actual_message == expected_message, (
                 
                f"[Assertion Failed]\nExpected: {expected_message}\nGot     : {actual_message}"
            )

            print(f"[Test Passed] Validation message matched: {actual_message}")

        except Exception as e:
            
           print(f"[Test Failed] Reason: {e}")
           self.driver.save_screenshot("test_warning_tc_22_failed.png")
           raise


        finally:
            comm.logo()


    def test_warning_tc_27(self):

        comm = Common_methods(self.driver)
        warning = warnings(self.driver)

        try:
            # Step 1: Navigate to Motor1 screen
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


    def test_warning_tc_28(self):
        comm = Common_methods(self.driver)
        warning = warnings(self.driver)

        try:
            # Step 1: Navigate to Motor1 screen
            comm.test_proclick()
            warning.motor1()

            parent = self.driver.find_element(By.ID, "parent-layout")

            # Step 2: Click Motor Load 3 Label 1
            motor_label_1 = parent.find_element(By.ID, "motor-load-3-label-1")
            ActionChains(self.driver).move_to_element(motor_label_1).click().perform()

            # Step 3: Select starter type index 3
            Select(self.driver.find_element(By.ID, "starter-type")).select_by_index(3)
            time.sleep(2)

            # Step 4: Click gear icon and calculate
            self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()
            self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()
            time.sleep(8)

            # Step 5: Click Motor Load 3 Label 6 and unlock
            motor_label_6 = parent.find_element(By.ID, "motor-load-3-label-6")
            ActionChains(self.driver).move_to_element(motor_label_6).click().perform()
            self.driver.find_element(By.CSS_SELECTOR, "img[alt='Lock/Un-Lock']").click()

            # Step 6: Click Motor Load 3 Label 1 again
            motor_label_1 = parent.find_element(By.ID, "motor-load-3-label-1")
            ActionChains(self.driver).move_to_element(motor_label_1).click().perform()

            # Step 7: Select operation type index 36
            Select(self.driver.find_element(By.ID, "op")).select_by_index(36)

            # Step 8: Recalculate
            self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()
            self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()
            time.sleep(5)

            # Step 9: Open report
            self.driver.find_element(By.CSS_SELECTOR, ".report-card > .row > .col-12 > .btn").click()

            # Step 10: Validate error message
            error_elem = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, "#panelsStayOpen-errorOne-0 > .accordion-body > .fs-14 > :nth-child(3) > .fs-12")
                )
            )
            actual_msg = error_elem.text.strip()
            expected_msg = (
                "Soft Starter ST 3 (17 A) rating is insufficient for Motor full load current (420 A). "
                "Please unlock Soft Starter"
            )

            print("Validation Message:", actual_msg)
            assert actual_msg == expected_msg, f"Expected: {expected_msg}, Got: {actual_msg}"

        except Exception as e:
        
            print(f"[Test Failed] Reason: {e}")
            self.driver.save_screenshot("test_warning_tc_22_failed.png")
            raise

        finally:
            comm.logo()


    def test_warning_tc_29(self):
        comm = Common_methods(self.driver)
        warning = warnings(self.driver)

        try:
            # Step 1: Navigate to AHF Warning page
            comm.test_sample1()
            comm.test_proclick()
            warning.ahfwarning()

            # Step 2: Click gear icon (settings) and Calculate button
            self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()
            time.sleep(10)

            # Step 3: Click Report button
            self.driver.find_element(By.CSS_SELECTOR, ".report-card > .row > .col-12 > .btn").click()

            # Step 4: Get validation message and assert
            error_elem = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, "#panelsStayOpen-errorOne-0 > div > div > div:nth-child(3) > span")
                )
            )
            actual_msg = error_elem.text.strip()
            expected_msg = "Harmonic Filter is not required as there as no non-linear loads defined. Non-linear loads can be defined in Non-Linear load selection in AHF"

            print("Validation Message:", actual_msg)
            assert actual_msg == expected_msg, f"Expected: {expected_msg}, Got: {actual_msg}"

        except Exception as e:
                
                print(f"[Test Failed] Reason: {e}")
                self.driver.save_screenshot("test_warning_tc_22_failed.png")
                raise

        finally:
            comm.logo()


    def test_warning_tc_30(self):
        
        comm = Common_methods(self.driver)
        warning = warnings(self.driver)

        try:
            # Step 1: Navigate to Earthing System page
            comm.test_proclick()
            warning.earthingsys()

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


    """ def test_warning_tc_31(self):

        comm = Common_methods(self.driver)
        Warning = warnings(self.driver)

        try:
            # Step 1: Navigate to Cable screen
            comm.test_proclick()
            Warning.cable()

            # Step 2: Click Calculate button
            self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()
            time.sleep(15)

            # Step 3: Click on Generic Load label
            self.driver.find_element(By.ID, "generic-load-3-label-2").click()
            time.sleep(2)

            # Step 4: Click lock/unlock icon
            self.driver.find_element(By.CSS_SELECTOR, "img[alt='Lock/Un-Lock']").click()

            # Step 5: Open Properties tab
            #self.driver.find_element(By.ID, "properties-tab").click()

            # Step 6: Set cable length to 500
            length_input = self.driver.find_element(By.ID, "length")
            length_input.clear()
            length_input.send_keys("500")

            # Step 7: Recalculate
            self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()
            self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()
            time.sleep(15)

            # Step 8: Open report
            self.driver.find_element(By.CSS_SELECTOR, ".report-card > .row > .col-12 > .btn").click()

            # Step 9: Validate the warning message
            msg_elem = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#panelsStayOpen-errorOne-1 > .accordion-body > .fs-14 > :nth-child(3)"))
            )
            actual_msg = msg_elem.text.strip()
            expected_msg = "Voltage drop 2.19 % of LV Cable LV CABLE WD 3 is greater than the permissible voltage limit 2 %"

            print("Validation Message:", actual_msg)
            assert actual_msg == expected_msg, f"Expected: {expected_msg}, Got: {actual_msg}"

        except Exception as e:
            print(f"[Test Failed] Reason: {e}")
            self.driver.save_screenshot("test_warning_tc_31_failed.png")
            raise

        finally:
            comm.logo() """


    def test_warning_tc_32(self):
        comm = Common_methods(self.driver)
        Warning = warnings(self.driver)

        try:
            # Step 1: Navigate to Cable screen
            comm.test_proclick()
            Warning.cable()

            # Step 2: Click on LV Source
            parent = self.driver.find_element(By.ID, "parent-layout")
            lv_source = parent.find_element(By.ID, "lv-source-1-label-1")
            ActionChains(self.driver).move_to_element(lv_source).click().perform()

            # Step 3: Select 'un' value
            Select(self.driver.find_element(By.ID, "un")).select_by_index(9)
            time.sleep(2)

            # Step 4: Click on Generic Load 1 and enter IR value
            generic_load_1 = parent.find_element(By.ID, "generic-load-3-label-1")
            ActionChains(self.driver).move_to_element(generic_load_1).click().perform()
            ir_input = self.driver.find_element(By.ID, "ir")
            ir_input.clear()
            ir_input.send_keys("1000")
            time.sleep(2)

            # Step 5: Click on Generic Load 2 and set length
            generic_load_2 = parent.find_element(By.ID, "generic-load-3-label-2")
            ActionChains(self.driver).move_to_element(generic_load_2).click().perform()
            length_input = self.driver.find_element(By.ID, "length")
            length_input.clear()
            length_input.send_keys("1000")
            time.sleep(2)
            length_input.clear()
            length_input.send_keys("500")

            # Step 6: Click gear icon and calculate
            self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()
            self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()
            time.sleep(10)

            # Step 7: Open report and validate message
            self.driver.find_element(By.CSS_SELECTOR, ".report-card > .row > .col-12 > .btn").click()
            msg_elem = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#panelsStayOpen-errorOne-1 > .accordion-body > .fs-14 > :nth-child(3)"))
            )
            actual_msg = msg_elem.text.strip()
            expected_msg = (
                "To satisfy the voltage drop limits, LV Cable LV CABLE WD 3 size 1 x 16 mm² has been increased to 1 x 150 mm²"
            )

            print("Validation Message:", actual_msg)
            assert actual_msg == expected_msg, f"Expected: {expected_msg}, Got: {actual_msg}"

        except Exception as e:
            print(f"[Test Failed] Reason: {e}")
            self.driver.save_screenshot("test_warning_tc_32_failed.png")
            raise

        finally:
            comm.logo()

    
    def test_warning_tc_33(self):
        comm = Common_methods(self.driver)
        Warning = warnings(self.driver)

        try:
            # Step 1: Navigate to Cable screen
            comm.test_proclick()
            Warning.cable()

            # Step 2: Click on Generic Load 2
            parent = self.driver.find_element(By.ID, "parent-layout")
            load2 = parent.find_element(By.ID, "generic-load-3-label-2")
            ActionChains(self.driver).move_to_element(load2).click().perform()

            # Step 3: Select LV Cable Type
            Select(self.driver.find_element(By.ID, "lv-cable-type")).select_by_index(1)
            time.sleep(2)

            # Step 4: Click on Generic Load 1 and set IR
            load1 = parent.find_element(By.ID, "generic-load-3-label-1")
            ActionChains(self.driver).move_to_element(load1).click().perform()
            ir_input = self.driver.find_element(By.ID, "ir")
            ir_input.clear()
            ir_input.send_keys("6300")

            # Step 5: Click gear icon and calculate
            self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()
            self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()
            time.sleep(5)

            # Step 6: Click Report button
            self.driver.find_element(By.CSS_SELECTOR, ".report-card > .row > .col-12 > .btn").click()

            # Step 7: Capture and assert the warning message
            msg_elem = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#panelsStayOpen-errorOne-1 > .accordion-body > .fs-14 > :nth-child(3)"))
            )
            actual_msg = msg_elem.text.strip()
            expected_msg = (
                "BBT is available upto to the rated current 6300A in Cu & Al. Please contact the customer interaction centre"
            )

            print("Validation Message:", actual_msg)
            assert actual_msg == expected_msg, f"Expected: {expected_msg}, Got: {actual_msg}"

        except Exception as e:
            print(f"[Test Failed] Reason: {e}")
            self.driver.save_screenshot("test_warning_tc_33_failed.png")
            raise

        finally:
            comm.logo()


    def test_warning_tc_34(self):

        comm = Common_methods(self.driver)
        Warning = warnings(self.driver)

        try:
            # Step 1: Navigate to Cable warning screen
            comm.test_proclick()
            Warning.cable()

            # Step 2: Click on Generic Load 1
            parent = self.driver.find_element(By.ID, "parent-layout")
            load1 = parent.find_element(By.ID, "generic-load-3-label-1")
            ActionChains(self.driver).move_to_element(load1).click().perform()

            # Step 3: Enter IR value
            ir_input = self.driver.find_element(By.ID, "ir")
            ir_input.clear()
            ir_input.send_keys("300")

            # Step 4: Click gear icon and then Calculate button
            self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()
            self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()
            time.sleep(10)

            # Step 5: Click on Report button
            self.driver.find_element(By.CSS_SELECTOR, ".report-card > .row > .col-12 > .btn").click()

            # Step 6: Get and assert warning message
            msg_elem = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((
                    By.CSS_SELECTOR, "#panelsStayOpen-errorOne-0 > .accordion-body > .fs-14 > :nth-child(3) > .fs-12"
                ))
            )
            actual_msg = msg_elem.text.strip()
            expected_msg = (
                "Load Power factor 0.85 is less than the default required power factor (0.9). Capacitor Bank must be included in the installation"
            )

            print("Validation Message:", actual_msg)
            assert actual_msg == expected_msg, f"Expected: {expected_msg}, Got: {actual_msg}"

        except Exception as e:
            print(f"[Test Failed] Reason: {e}")
            self.driver.save_screenshot("test_warning_tc_34_failed.png")
            raise

        finally:
            comm.logo()


    def test_warning_tc_35(self):
        comm = Common_methods(self.driver)
        Warning = warnings(self.driver)

        try:
            # Step 1: Navigate to Capacitor Bank screen
            comm.test_proclick()
            Warning.capacitor()

            # Step 2: Click on LV Source 1
            parent = self.driver.find_element(By.ID, "parent-layout")
            lv_source = parent.find_element(By.ID, "lv-source-1-label-1")
            ActionChains(self.driver).move_to_element(lv_source).click().perform()

            # Step 3: Select UN value = 5
            un_dropdown = self.driver.find_element(By.ID, "un")
            Select(un_dropdown).select_by_index(5)  # Index 5 means 6th item (0-based)

            time.sleep(2)

            # Step 4: Click gear icon and Calculate button
            self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()
            self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()
            time.sleep(10)

            # Step 5: Click Report button
            self.driver.find_element(By.CSS_SELECTOR, ".report-card > .row > .col-12 > .btn").click()

            # Step 6: Validate warning message
            msg_elem = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((
                    By.CSS_SELECTOR,
                    "#panelsStayOpen-errorOne-0 > .accordion-body > .fs-14 > :nth-child(3) > .fs-12"
                ))
            )
            actual_msg = msg_elem.text.strip()
            expected_msg = (
                "Capacitor Bank is not required. The reactive power to compensate is lower then threshold"
            )

            print("Validation Message:", actual_msg)
            assert actual_msg == expected_msg, f"Expected: {expected_msg}, Got: {actual_msg}"

        except Exception as e:
            print(f"[Test Failed] Reason: {e}")
            self.driver.save_screenshot("test_warning_tc_35_failed.png")
            raise

        finally:
            comm.logo()

    
    def test_warning_tc_36(self):
        comm = Common_methods(self.driver)
        Warning = warnings(self.driver)

        try:
            # Step 1: Navigate to Capacitor Bank screen
            comm.test_proclick()
            Warning.capacitor()

            # Step 2: Click on LV Source 1
            parent = self.driver.find_element(By.ID, "parent-layout")
            lv_source = parent.find_element(By.ID, "lv-source-1-label-1")
            ActionChains(self.driver).move_to_element(lv_source).click().perform()

            # Step 3: Select UN dropdown option index 5
            un_dropdown = self.driver.find_element(By.ID, "un")
            Select(un_dropdown).select_by_index(5)
            time.sleep(2)

            # Step 4: Click gear icon and Calculate button
            self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()
            self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()
            time.sleep(10)

            # Step 5: Click on Capacitor Bank 4
            cap_bank = parent.find_element(By.ID, "capacitor-bank-4-label-1")
            ActionChains(self.driver).move_to_element(cap_bank).click().perform()

            # Step 6: Click lock/unlock icon
            self.driver.find_element(By.CSS_SELECTOR, "img[alt='Lock/Un-Lock']").click()
            time.sleep(3)

            # Step 7: Click Generic Load 1 and enter IR = 600
            gen_load = parent.find_element(By.ID, "generic-load-3-label-1")
            ActionChains(self.driver).move_to_element(gen_load).click().perform()

            ir_input = self.driver.find_element(By.ID, "ir")
            ir_input.clear()
            ir_input.send_keys("600")
            time.sleep(2)

            # Step 8: Click gear icon and Calculate again
            self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()
            self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()
            time.sleep(10)

            # Step 9: Click Report button
            self.driver.find_element(By.CSS_SELECTOR, ".report-card > .row > .col-12 > .btn").click()

            # Step 10: Validate warning message
            msg_elem = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((
                    By.CSS_SELECTOR,
                    "#panelsStayOpen-errorOne-0 > .accordion-body > .fs-14 > :nth-child(3) > .fs-12"
                ))
            )
            actual_msg = msg_elem.text.strip()
            expected_msg = (
                "APFC Relay is not suitable for the selected no. of steps / switching device. Please unlock the APFC Relay"
            )

            print("Validation Message:", actual_msg)
            assert actual_msg == expected_msg, f"Expected: {expected_msg}, Got: {actual_msg}"

        except Exception as e:
            print(f"[Test Failed] Reason: {e}")
            self.driver.save_screenshot("test_warning_tc_36_failed.png")
            raise

        finally:
            comm.logo()


    def test_warning_tc_37(self):
        comm = Common_methods(self.driver)
        Warning = warnings(self.driver)

        try:
            # Step 1: Navigate to Motor1 Warning screen
            comm.test_proclick()
            Warning.motor1()

            # Step 2: Click LV Source 1
            parent = self.driver.find_element(By.ID, "parent-layout")
            lv_source = parent.find_element(By.ID, "lv-source-1-label-1")
            ActionChains(self.driver).move_to_element(lv_source).click().perform()

            # Step 3: Select UN index 5
            un_dropdown = self.driver.find_element(By.ID, "un")
            Select(un_dropdown).select_by_index(5)
            time.sleep(2)

            # Step 4: Click Motor Load 1
            motor = parent.find_element(By.ID, "motor-load-3-label-1")
            ActionChains(self.driver).move_to_element(motor).click().perform()

            # Step 5: Select starter type index 3
            starter_dropdown = self.driver.find_element(By.ID, "starter-type")
            Select(starter_dropdown).select_by_index(3)

            # Step 6: Open settings tab and update Ambient Temperature
            self.driver.find_element(By.ID, "settings-tab").click()
            time.sleep(2)
            ambient_input = self.driver.find_element(By.ID, "generalAmbientTempAir")
            ambient_input.clear()
            ambient_input.send_keys("60")

            # Step 7: Save settings
            self.driver.find_element(By.ID, "saveSettings").click()
            comm.settingpopup()

            # Step 8: Gear icon → Calculate
            self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()
            self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()
            time.sleep(10)

            # Step 9: Click Report button
            self.driver.find_element(By.CSS_SELECTOR, ".report-card > .row > .col-12 > .btn").click()

            # Step 10: Validate warning message
            msg_elem = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((
                    By.CSS_SELECTOR,
                    "#panelsStayOpen-errorOne-0 > .accordion-body > .fs-14 > :nth-child(3) > .fs-12"
                ))
            )
            actual_msg = msg_elem.text.strip()
            expected_msg = (
                 
                "Soft starter has to be selected"
            )

            print("Validation Message:", actual_msg)
            assert actual_msg == expected_msg, f"Expected: {expected_msg}, Got: {actual_msg}"

        except Exception as e:
            print(f"[Test Failed] Reason: {e}")
            self.driver.save_screenshot("test_warning_tc_37_failed.png")
            raise

        finally:
            comm.logo()



    def test_warning_tc_38(self):
        comm = Common_methods(self.driver)
        Warning = warnings(self.driver)

        try:
            # Step 1: Navigate to Cable warning screen
            comm.test_proclick()
            Warning.cable()

            # Step 2: Select LV source
            parent = self.driver.find_element(By.ID, "parent-layout")
            lv_source = parent.find_element(By.ID, "lv-source-1-label-1")
            ActionChains(self.driver).move_to_element(lv_source).click().perform()

            # Step 3: Select UN index 5
            Select(self.driver.find_element(By.ID, "un")).select_by_index(5)
            time.sleep(2)

            # Step 4: Click Generic Load 2
            load2 = parent.find_element(By.ID, "generic-load-3-label-2")
            ActionChains(self.driver).move_to_element(load2).click().perform()

            # Step 5: Select cable type index 1
            Select(self.driver.find_element(By.ID, "lv-cable-type")).select_by_index(1)

            # Step 6: Gear icon → Calculate
            self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()
            self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()
            time.sleep(12)

            # Step 7: Re-click load and unlock
            ActionChains(self.driver).move_to_element(load2).click().perform()
            self.driver.find_element(By.CSS_SELECTOR, "img[alt='Lock/Un-Lock']").click()
            time.sleep(3)


            # Step 8: Go to properties tab and update length
            length_input = self.driver.find_element(By.ID, "length")
            length_input.clear()
            length_input.send_keys("500")

            # Step 9: Gear icon → Recalculate
            self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()
            self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()
            time.sleep(12)

            # Step 10: Open Report
            self.driver.find_element(By.CSS_SELECTOR, ".report-card > .row > .col-12 > .btn").click()

            # Step 11: Validate the warning message
            msg_elem = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((
                    By.CSS_SELECTOR,
                    "#panelsStayOpen-errorOne-0 > .accordion-body > .fs-14 > :nth-child(3) > .fs-12"
                ))
            )
            actual_msg = msg_elem.text.strip()
            expected_msg = (

                "Voltage drop 3.41 % of Feeder BBT Feeder BBT WD 3 is greater than the permissible voltage limit 2 %"
            )

            print("Validation Message:", actual_msg)
            assert actual_msg == expected_msg, f"Expected: {expected_msg}, Got: {actual_msg}"

        except Exception as e:
            print(f"[Test Failed] Reason: {e}")
            self.driver.save_screenshot("test_warning_tc_38_failed.png")
            raise

        finally:
            comm.logo()


    def test_warning_tc_39(self):
        comm = Common_methods(self.driver)
        Warning = warnings(self.driver)

        try:
            # Step 1: Go to Capacitor screen
            comm.test_proclick()
            Warning.capacitor()

            # Step 2: Select LV Source
            parent = self.driver.find_element(By.ID, "parent-layout")
            lv_source = parent.find_element(By.ID, "lv-source-1-label-1")
            ActionChains(self.driver).move_to_element(lv_source).click().perform()

            # Step 3: Select UN index 5
            Select(self.driver.find_element(By.ID, "un")).select_by_index(5)
            time.sleep(2)

            # Step 4: Select Generic Load and set IR = 200
            generic_load = parent.find_element(By.ID, "generic-load-3-label-1")
            ActionChains(self.driver).move_to_element(generic_load).click().perform()
            ir_field = self.driver.find_element(By.ID, "ir")
            ir_field.clear()
            ir_field.send_keys("200")

            # Step 5: Calculate
            self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()
            self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()
            time.sleep(12)

            # Step 6: Click Capacitor Bank
            capacitor = parent.find_element(By.ID, "capacitor-bank-4-label-1")
            ActionChains(self.driver).move_to_element(capacitor).click().perform()

            properties = self.driver.find_element(By.CSS_SELECTOR, "#properties-tab")
            properties.click()


            # Scroll into view of "Capacitor Bank Selection"
            self.driver.execute_script("arguments[0].scrollIntoView();", 
                self.driver.find_element(By.XPATH, "//*[contains(text(),'Capacitor Bank Selection')]")
            )

            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Capacitor Bank Selection')]"))
            )
            time.sleep(2)

            # Step 7: Unlock
            self.driver.find_element(By.CSS_SELECTOR, "img[alt='Lock/Unlock']").click()

            # Step 8: Update IR to 1000
            ActionChains(self.driver).move_to_element(generic_load).click().perform()
            ir_field = self.driver.find_element(By.ID, "ir")
            ir_field.clear()
            ir_field.clear()
            ir_field.send_keys("1000")
            time.sleep(2)

            # Step 9: Recalculate
            self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()
            self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()
            time.sleep(10)

            # Step 10: Click Report Button
            self.driver.find_element(By.CSS_SELECTOR, ".report-card > .row > .col-12 > .btn").click()

            # Step 11: Validate the warning message
            msg_elem = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((
                    By.CSS_SELECTOR,
                    "#panelsStayOpen-errorOne-0 > .accordion-body > .fs-14 > :nth-child(3) > .fs-12"
                ))
            )
            actual_msg = msg_elem.text.strip()
            expected_msg = (
                "Unlock the Capacitor bank 35 as the Reactive power requirement 100 kVAr has changed"
            )

            print("Validation Message:", actual_msg)
            assert actual_msg == expected_msg, f"Expected: {expected_msg}, Got: {actual_msg}"

        except Exception as e:
            print(f"[Test Failed] Reason: {e}")
            self.driver.save_screenshot("test_warning_tc_39_failed.png")
            raise

        finally:
            comm.logo()


    
    def test_warning_tc_40(self):
        comm = Common_methods(self.driver)
        Warning = warnings(self.driver)

        try:
            # Step 1: Navigate to Capacitor Page
            comm.test_proclick()
            Warning.capacitor()

            # Step 2: Click LV Source
            parent = self.driver.find_element(By.ID, "parent-layout")
            lv_source = parent.find_element(By.ID, "lv-source-1-label-1")
            ActionChains(self.driver).move_to_element(lv_source).click().perform()

            # Step 3: Select UN index 5
            Select(self.driver.find_element(By.ID, "un")).select_by_index(5)
            time.sleep(2)

            # Step 4: Select Generic Load and enter IR = 200
            generic_load = parent.find_element(By.ID, "generic-load-3-label-1")
            ActionChains(self.driver).move_to_element(generic_load).click().perform()
            ir = self.driver.find_element(By.ID, "ir")
            ir.clear()
            ir.send_keys("200")

            # Step 5: Calculate
            self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()
            self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()
            time.sleep(12)

            # Step 6: Lock capacitor bank
            capacitor = parent.find_element(By.ID, "capacitor-bank-4-label-1")
            ActionChains(self.driver).move_to_element(capacitor).click().perform()
            time.sleep(2)
            self.driver.find_element(By.CSS_SELECTOR, "img[alt='Lock/Un-Lock']").click()
           

            # Step 7: Revisit generic load, set IR = 1000
            ActionChains(self.driver).move_to_element(generic_load).click().perform()
            ir = self.driver.find_element(By.ID, "ir")
            ir.clear()
            ir.clear()
            ir.send_keys("1000")

            # Step 8: Recalculate
            self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()
            self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()
            time.sleep(10)

            # Step 9: Generate Report
            self.driver.find_element(By.CSS_SELECTOR, ".report-card > .row > .col-12 > .btn").click()

            # Step 10: Validate error message
            error_msg = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#panelsStayOpen-errorOne-0 > .accordion-body > .fs-14 > :nth-child(3) > .fs-12"))
            ).text.strip()

            expected_msg = "APFC Relay is not suitable for the selected no. of steps / switching device. Please unlock the APFC Relay"
            assert error_msg == expected_msg, f"[Assertion Failed] Expected: {expected_msg}, Got: {error_msg}"
            print("[Assertion Passed] Warning message verified.")

        except Exception as e:
            print(f"[Test Failed] Exception: {e}")
            self.driver.save_screenshot("test_warning_tc_40_failed.png")
            raise

        finally:
            comm.logo()



    def test_warning_tc_41(self):
        comm = Common_methods(self.driver)
        Warning = warnings(self.driver)

        try:
                # Step 1: Navigate to IBCal screen
                comm.test_proclick()
                Warning.ibcal()

                # Step 2: Click Generic Load
                parent_layout = self.driver.find_element(By.ID, "parent-layout")
                generic_load = parent_layout.find_element(By.ID, "generic-load-3-label-1")
                ActionChains(self.driver).move_to_element(generic_load).click().perform()

                # Step 3: Update IR value
                ir_input = self.driver.find_element(By.ID, "ir")
                ir_input.clear()
                ir_input.clear()
                ir_input.send_keys("4500")

                # Step 4: Click Calculator icon and Save
                self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()
                self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()

                # Step 5: Wait for calculation to complete
                time.sleep(12)

                # Step 6: Click View Report button
                self.driver.find_element(By.CSS_SELECTOR, ".report-card > .row > .col-12 > .btn").click()

                # Step 7: Validate Warning Message
                warning_element = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located(
                        (By.CSS_SELECTOR, "#panelsStayOpen-errorOne-1 > div > div > div:nth-child(3) > span")
                )
                )
                actual_message = warning_element.text.strip()
                expected_message = "Transformer rating 3150 kVA is lesser than the required rating 3234.6 kVA. Transformer in undersized"

                assert actual_message == expected_message, f"Mismatch: Expected '{expected_message}', got '{actual_message}'"
                print("Warning-TC-41 passed: Transformer undersized warning verified.")

        except Exception as e:
                print(f"[ERROR] Test failed due to: {e}")
                self.driver.save_screenshot("warning_tc_41_failure.png")
                raise

        finally:
                comm.logo()



    def test_warning_tc_42(self):
        comm = Common_methods(self.driver)
        Warning = warnings(self.driver)

        try:
                # Step 1: Navigate to IBCal1 screen
                comm.test_proclick()
                Warning.ibcal1()

                # Step 2: Click Generic Load
                parent_layout = self.driver.find_element(By.ID, "parent-layout")
                generic_load = parent_layout.find_element(By.ID, "generic-load-3-label-1")
                ActionChains(self.driver).move_to_element(generic_load).click().perform()

                # Step 3: Set IR value to 4500
                ir_input = self.driver.find_element(By.ID, "ir")
                ir_input.clear()
                ir_input.send_keys("4500")

                # Step 4: Click Calculate button and Save
                self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()
                self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()

                # Step 5: Wait for backend processing
                time.sleep(12)

                # Step 6: Click View Report
                self.driver.find_element(By.CSS_SELECTOR, ".report-card > .row > .col-12 > .btn").click()

                # Step 7: Validate Generator Warning Message
                warning_element = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((
                        By.CSS_SELECTOR,
                        "#panelsStayOpen-errorOne-1 > div > div > div:nth-child(3) > span"
                ))
                )
                actual_message = warning_element.text.strip()
                expected_message = "Generator rating 2058 kVA is lesser than the required rating 3234.6 kVA. Generator is undersized"

                assert actual_message == expected_message, f"Mismatch: Expected '{expected_message}', but got '{actual_message}'"
                print("Warning-TC-42 passed: Generator undersized warning verified.")

        except Exception as e:
                print(f"[ERROR] Test failed due to: {e}")
                self.driver.save_screenshot("warning_tc_42_failure.png")
                raise

        finally:
                comm.logo()


    
    def test_warning_tc_43(self):
        comm = Common_methods(self.driver)

        try:
               
                comm.test_proclick()
                # Step 1: Click the Save button (bottom of screen)
                self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()

                # Step 2: Wait for processing
                time.sleep(3)

                # Step 4: Capture and validate the warning message
                warning_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((
                       
                        By.CSS_SELECTOR, ".fs-14 > .mb-2"
                ))
                )
                actual_message = warning_element.text.strip()
                expected_message = "Please create the SLD"

                assert actual_message == expected_message, f"Mismatch: Expected '{expected_message}', but got '{actual_message}'"
                print("Warning-TC-43 passed: SLD warning verified.")

        except Exception as e:
                print(f"[ERROR] Test failed due to: {e}")
                self.driver.save_screenshot("warning_tc_43_failure.png")
                raise

        finally:
                comm.logo()


    def test_warning_tc_44(self):
        comm = Common_methods(self.driver)
        Warning = warnings(self.driver)

        try:
                # Step 1: Call the IBCal2 setup (custom page setup)
                comm.test_proclick()    
                Warning.ibcal2()

                # Step 2: Click the Save button
                self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()

                # Step 3: Wait for processing
                time.sleep(2)

                # Step 4: Click the View Report button
                self.driver.find_element(By.CSS_SELECTOR, ".report-card > .row > .col-12 > .btn").click()

                # Step 5: Validate the warning message
                warning_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((
                        By.CSS_SELECTOR, ".fs-14 > :nth-child(3)"
                ))
                )
                actual_message = warning_element.text.strip()
                expected_message = "There is no load in the network"

                assert actual_message == expected_message, f"Mismatch: Expected '{expected_message}', but got '{actual_message}'"
                print("Warning-TC-44 passed: 'No load in the network' warning verified.")

        except Exception as e:
                print(f"[ERROR] Test failed due to: {e}")
                self.driver.save_screenshot("warning_tc_44_failure.png")
                raise

        finally:
                comm.logo()


    def test_warning_tc_45(self):
        comm = Common_methods(self.driver)
        Warning = warnings(self.driver) 

        try:
                # Step 1: Call ibcal3 setup function to configure test scenario
                comm.test_proclick()
                Warning.ibcal3()

                # Step 2: Wait for potential rendering (Cypress: cy.get(3000) seems incorrect; replacing with time.sleep)
                time.sleep(3)

                # Step 3: Click the Save button
                self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()
                time.sleep(2)

                # Step 4: Click the View Report button
                self.driver.find_element(By.CSS_SELECTOR, ".report-card > .row > .col-12 > .btn").click()

                # Step 5: Validate the warning message
                warning_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((
                        By.CSS_SELECTOR, "#panelsStayOpen-errorOne-0 > .accordion-body > .fs-14 > :nth-child(3) > .fs-12"
                ))
                )
                actual_message = warning_element.text.strip()
                expected_message = "The Component Circuit Breaker QA 4 does not feed any load in operating mode"

                assert actual_message == expected_message, f"Mismatch: Expected '{expected_message}', but got '{actual_message}'"
                print("Warning-TC-45 passed: Circuit breaker not feeding load warning verified.")

        except Exception as e:
                print(f"[ERROR] Test failed due to: {e}")
                self.driver.save_screenshot("warning_tc_45_failure.png")
                raise

        finally:
                comm.logo()


    def test_warning_tc_46(self):
        comm = Common_methods(self.driver)
        Warning = warnings(self.driver)

        try:
                # Step 1: Setup framed component via helper function
                comm.test_proclick()
                Warning.sld_framed_component()

                # Step 2: Click on the component
                self.driver.find_element(By.CSS_SELECTOR, "#parent-layout #generic-load-3-label-3").click()
                time.sleep(2)

                # Step 3: Enable the switch toggle
                self.driver.find_element(By.CSS_SELECTOR, ":nth-child(10) > #offcanvas_accordion > .accordion-item > .accordion-header > .accordion-button > .ms-auto > .form-switch > .switchToggle > label").click()

                # Step 4: Select option in dropdown
                Select(self.driver.find_element(By.ID, "rcdType")).select_by_index(2)

                # Step 5: Click the close or collapse image
                self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()

                # Step 6: Click the Save button
                self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()
                time.sleep(10)

                # Step 7: Click the View Report button
                self.driver.find_element(By.CSS_SELECTOR, ".report-card > .row > .col-12 > .btn").click()

                # Step 8: Capture and validate warning message
                warning_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".fs-14 > :nth-child(3)"))
                )
                actual_message = warning_element.text.strip()
                expected_message = (
                "Circuit Breaker is not available with the combination Rated Voltage = 415, "
                "Current = 100, Pole = 4P, Withdrawable = No. Try with the Withdrawable option "
                "\"Yes\" or contact the customer interaction centre"
                )

                assert actual_message == expected_message, f"Mismatch: Expected '{expected_message}', but got '{actual_message}'"
                print("Warning-TC-46 passed: Circuit breaker combination warning verified.")

        except Exception as e:
                print(f"[ERROR] Test failed due to: {e}")
                self.driver.save_screenshot("warning_tc_46_failure.png")
                raise

        finally:
                comm.logo()

    def test_warning_tc_47(self):
        comm = Common_methods(self.driver)
        Warning = warnings(self.driver)

        try:
                # Step 1: Setup framed component via helper function
                comm.test_sample1()
                comm.test_proclick()
                Warning.sld_framed_component()

                # Step 2: Click on the component
                self.driver.find_element(By.CSS_SELECTOR, "#parent-layout #generic-load-3-label-3").click()
                time.sleep(2)

                # Step 3: Enable the switch toggle
                self.driver.find_element(By.CSS_SELECTOR, "#offcanvas_accordion > div > h2 > button > app-toggle-input > div > div > label").click()
                time.sleep(2)

                # Step 4: Select option in dropdown
                parent = self.driver.find_element(By.ID, "parent-layout")
                lv_source = parent.find_element(By.ID, "lv-source-1-label-1")
                ActionChains(self.driver).move_to_element(lv_source).click().perform()  

                Select(self.driver.find_element(By.ID, "earth")).select_by_index(0)

                 # Step 5: Click the close or collapse image
                self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()

                # Step 6: Click the Save button
                self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()
                time.sleep(3)

                # Step 7: Click the View Report button
                self.driver.find_element(By.CSS_SELECTOR, ".report-card > .row > .col-12 > .btn").click()

                # Step 8: Capture and validate warning message
                warning_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".fs-14 > :nth-child(3)"))
                )
                actual_message = warning_element.text.strip()
                expected_message = (
                "RCD is not allowed in TN-C earthing system"
                )

                assert actual_message == expected_message, f"Mismatch: Expected '{expected_message}', but got '{actual_message}'"
                print("Warning-TC-47 passed: Circuit breaker combination warning verified.")

        except Exception as e:
                print(f"[ERROR] Test failed due to: {e}")
                self.driver.save_screenshot("warning_tc_46_failure.png")
                raise

        finally:
                comm.logo()


    def test_warning_tc_48(self):

        comm = Common_methods(self.driver)

        try:
            # Step 1: Initial project click
            comm.test_proclick()

            # Step 2: Trigger Warning Scenario
            Warning = warnings(self.driver)
            Warning.warning_scenario_4()
            actions = ActionChains(self.driver)

             # Step 6: Click the calculate submit button
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pt-4 > div > .btn"))).click()
            time.sleep(10)

            # Step 3: Click the LV source label
            parent_layout = self.driver.find_element(By.ID, "parent-layout")
            lv_source_label = parent_layout.find_element(By.ID, "fdr-circuit-bbt-3-label-0")
            actions.move_to_element(lv_source_label).click().perform()
            time.sleep(2)

            self.driver.find_element(By.CSS_SELECTOR, "img[alt='Lock/Un-Lock']").click()

            layout = self.wait.until(EC.presence_of_element_located((By.ID, "parent-layout")))
            component = layout.find_element(By.ID, "generic-load-5-label-1")
            component.click()
            time.sleep(2)           

            ir_field = self.wait.until(EC.element_to_be_clickable((By.ID, "ir")))
            ir_field.click()
            ir_field.clear()
            ir_field.send_keys("30")


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
                "Circuit Breaker QA 3 Rating 100 A is insufficient for the design current (300.00 A). Unlock the circuit breaker for alternate product selection"
            )

            print("Validation Message:", actual_message)
            assert actual_message == expected_message, f"Expected: {expected_message}, Got: {actual_message}"

        except Exception as e:
            print(f"Error in test_warning_tc_8: {e}")
            self.driver.save_screenshot("test_warning_tc_48_error.png")
            raise

        finally:
            comm.logo()


    def test_warning_tc_49(self):

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
            generic_load = self.wait.until(EC.element_to_be_clickable((By.ID, "fdr-circuit-bbt-3-label-0")))
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
            


    def test_warning_tc_50(self):

        comm = Common_methods(self.driver)
        Warning = warnings(self.driver)

        try:
                # Step 1: Setup framed component via helper function
                comm.test_proclick()
                Warning.sld_framed_component()

                # Step 2: Click on the component
                parent = self.driver.find_element(By.ID, "parent-layout")
                genericload = self.driver.find_element(By.CSS_SELECTOR, "#parent-layout #generic-load-3-label-3").click()
                ActionChains(self.driver).move_to_element(genericload).click().perform()
                time.sleep(2)

                # Step 3: Enable the switch toggle
                select_protection = Select(self.driver.find_element(By.ID, "protection-type"))
                select_protection.select_by_index(1)
                time.sleep(1)

                 # Step 5: Click the close or collapse image
                self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()

                # Step 6: Click the Save button
                self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()
                time.sleep(10)
                
                fusebreaker = self.driver.find_element(By.CSS_SELECTOR, "#parent-layout #generic-load-3-label-3").click()
                ActionChains(self.driver).move_to_element(fusebreaker).click().perform()
                time.sleep(2)
                self.driver.find_element(By.CSS_SELECTOR, "img[alt='Lock/Un-Lock']").click()

                ActionChains(self.driver).move_to_element(genericload).click().perform()
                ir = self.driver.find_element(By.ID, "ir")
                ir.clear()
                ir.clear()
                ir.send_keys("300")


                # Step 7: Click the View Report button
                self.driver.find_element(By.CSS_SELECTOR, ".report-card > .row > .col-12 > .btn").click()


                # Step 8: Capture and validate warning message
                warning_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".fs-14 > :nth-child(3)"))
                )
                actual_message = warning_element.text.strip()
                expected_message = (
                "Fuse QA 3 Rating 100 A is insufficient for the design current (300 A). Unlock the Fuse for alternate product selection"
                )

                assert actual_message == expected_message, f"Mismatch: Expected '{expected_message}', but got '{actual_message}'"
                print("Warning-TC-50 passed: Circuit breaker combination warning verified.")

        except Exception as e:
                print(f"[ERROR] Test failed due to: {e}")
                self.driver.save_screenshot("warning_tc_46_failure.png")
                raise

        finally:
                comm.logo()



    def test_warning_tc_51(self):

        comm = Common_methods(self.driver)
        Warning = warnings(self.driver)

        try:
                # Step 1: Setup framed component via helper function
                comm.test_proclick()
                Warning.warning_scenario_4()

                # Step 2: Click on the component
                parent = self.driver.find_element(By.ID, "parent-layout")
                breaker = self.driver.find_element(By.ID, "fdr-circuit-bbt-4-label-0").click()
                ActionChains(self.driver).move_to_element(breaker).click().perform()
                time.sleep(2)

                # Step 3: Enable the switch toggle
                select_protection = Select(self.driver.find_element(By.ID, "protection-type"))
                select_protection.select_by_index(1)
                time.sleep(1)

                 # Step 5: Click the close or collapse image
                self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()

                # Step 6: Click the Save button
                self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()
                time.sleep(10)               

                fusebreaker = self.driver.find_element(By.ID, "fdr-circuit-bbt-4-label-0").click()
                ActionChains(self.driver).move_to_element(fusebreaker).click().perform()
                time.sleep(2)
                self.driver.find_element(By.CSS_SELECTOR, "img[alt='Lock/Un-Lock']").click()

                parent = self.driver.find_element(By.ID, "parent-layout")
                genericload = self.driver.find_element(By.CSS_SELECTOR, "#parent-layout #generic-load-6-label-1").click()
                ActionChains(self.driver).move_to_element(genericload).click().perform()
                time.sleep(2)

                ActionChains(self.driver).move_to_element(genericload).click().perform()
                ir = self.driver.find_element(By.ID, "ir")
                ir.clear()
                ir.clear()
                ir.send_keys("300")

                  # Step 5: Click the close or collapse image
                self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()

                # Step 6: Click the Save button
                self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()
                time.sleep(6)               

                # Step 7: Click the View Report button
                self.driver.find_element(By.CSS_SELECTOR, ".report-card > .row > .col-12 > .btn").click()

                # Step 8: Capture and validate warning message
                warning_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".fs-14 > :nth-child(3)"))
                )
                actual_message = warning_element.text.strip()
                expected_message = (
                "Fuse QA 4 Rating 100 A is insufficient for the design current (300.00 A). Unlock the Fuse for alternate product selection"
                )

                assert actual_message == expected_message, f"Mismatch: Expected '{expected_message}', but got '{actual_message}'"
                print("Warning-TC-50 passed: Circuit breaker combination warning verified.")

        except Exception as e:
                print(f"[ERROR] Test failed due to: {e}")
                self.driver.save_screenshot("warning_tc_46_failure.png")
                raise

        finally:
                comm.logo()

            

    def test_warning_tc_52(self):

        comm = Common_methods(self.driver)
        Warning = warnings(self.driver)

        try:
                # Step 1: Setup framed component via helper function
                comm.test_proclick()
                Warning.sld_framed_component()

                # Step 2: Click on the component
                self.driver.find_element(By.ID, "parent-layout")
                self.driver.find_element(By.ID, "generic-load-3-label-3").click()

                time.sleep(2)

                # Step 3: Enable the switch toggle
                select_protection = Select(self.driver.find_element(By.ID, "protection-type"))
                select_protection.select_by_index(1)
                time.sleep(1)

                self.driver.find_element(By.ID, "parent-layout")
                self.driver.find_element(By.CSS_SELECTOR, "#parent-layout #generic-load-3-label-1").click()               
                time.sleep(2)

                ir = self.driver.find_element(By.ID, "ir").click()
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
                print("Warning-TC-50 passed: Circuit breaker combination warning verified.")

        except Exception as e:
                print(f"[ERROR] Test failed due to: {e}")
                self.driver.save_screenshot("warning_tc_46_failure.png")
                raise

        finally:
                comm.logo()



    def test_warning_tc_53(self):

        comm = Common_methods(self.driver)
        Warning = warnings(self.driver)

        try:
                # Step 1: Setup framed component via helper function
                comm.test_proclick()
                Warning.warning_scenario_4()

                # Step 2: Click on the component
    
                self.driver.find_element(By.ID, "fdr-circuit-bbt-3-label-0").click()
                time.sleep(2)

                # Step 3: Enable the switch toggle
                select_protection = Select(self.driver.find_element(By.ID, "protection-type"))
                select_protection.select_by_index(1)
                time.sleep(1)

                
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

    def test_warning_tc_54(self):

        comm = Common_methods(self.driver)
        Warning = warnings(self.driver)

        try:
                # Step 1: Setup framed component via helper function
                comm.test_proclick()
                Warning.switch2()

                # Step 6: Click the Save button
                self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()
                time.sleep(10) 

                # Step 2: Click on the component
                parent = self.driver.find_element(By.ID, "parent-layout")
                breaker = self.driver.find_element(By.ID, "fdr-circuit-bbt-3-label-0").click()
                ActionChains(self.driver).move_to_element(breaker).click().perform()
                time.sleep(2)
                self.driver.find_element(By.CSS_SELECTOR, "img[alt='Lock/Un-Lock']").click()

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
                ir.send_keys("1000")

                  # Step 5: Click the close or collapse image
                self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()

                self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()
                time.sleep(3)             

                # Step 7: Click the View Report button
                self.driver.find_element(By.CSS_SELECTOR, ".report-card > .row > .col-12 > .btn").click()

                # Step 8: Capture and validate warning message
                warning_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#panelsStayOpen-errorOne-0 > div > div > div:nth-child(3) > span"))
                )
                actual_message = warning_element.text.strip()
                expected_message = (
                "Switch QB 3 Rating 100 A is insufficient for the design current (1000.00 A). Unlock the Switch for alternate product selection"
                )

                assert actual_message == expected_message, f"Mismatch: Expected '{expected_message}', but got '{actual_message}'"
                print("Warning-TC-54 passed: Circuit breaker combination warning verified.")

        except Exception as e:
                print(f"[ERROR] Test failed due to: {e}")
                self.driver.save_screenshot("warning_tc_54_failure.png")
                raise

        finally:
                comm.logo()


    def test_warning_tc_55(self):

        comm = Common_methods(self.driver)
        Warning = warnings(self.driver)
       

        try:
                # Step 1: Setup framed component via helper function
                comm.test_proclick()
                Warning.switch2()
               

                # Step 2: Click on the component
                time.sleep(2)
                self.driver.find_element(By.ID, "parent-layout")
                self.driver.find_element(By.ID, "lv-source-st-1-label-1").click()
                time.sleep(2)

                un_dropdown = self.wait.until(EC.presence_of_element_located((By.ID, "un")))
                Select(un_dropdown).select_by_index(9)
                time.sleep(2)

                Select(self.driver.find_element(By.ID, "earth")).select_by_index(2)

                # Step 5: Click the close or collapse image
                self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()

                self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()
                time.sleep(10)             

                # Step 7: Click the View Report button
                self.driver.find_element(By.CSS_SELECTOR, ".report-card > .row > .col-12 > .btn").click()

                # Step 8: Capture and validate warning message
                warning_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#panelsStayOpen-errorOne-0 > div > div > div:nth-child(3) > span"))
                )
                actual_message = warning_element.text.strip()
                expected_message = (
                "In TT earthing system, it is mandatory to install a RCD device either on each incomer or each outgoer of busbar downstream of source"
                )

                assert actual_message == expected_message, f"Mismatch: Expected '{expected_message}', but got '{actual_message}'"
                print("Warning-TC-55 passed: Circuit breaker combination warning verified.")

        except Exception as e:
                print(f"[ERROR] Test failed due to: {e}")
                self.driver.save_screenshot("warning_tc_55_failure.png")
                raise

        finally:
                comm.logo()


    def test_warning_tc_56(self):

        comm = Common_methods(self.driver)
        Warning = warnings(self.driver)
       

        try:
                # Step 1: Setup framed component via helper function
                comm.test_sample1()
                comm.test_proclick()
                Warning.motor1()              

                # Step 2: Click on the component
                time.sleep(2)
                self.driver.find_element(By.ID, "parent-layout")
                self.driver.find_element(By.ID, "lv-source-1-label-1").click()
                time.sleep(2)

                un_dropdown = self.wait.until(EC.presence_of_element_located((By.ID, "un")))
                Select(un_dropdown).select_by_index(5)
                time.sleep(2)

                self.driver.find_element(By.ID, "motor-load-3-label-3").click()
                time.sleep(2)
                self.driver.find_element(By.CSS_SELECTOR, "img[alt='Lock/Un-Lock']").click()

                self.driver.find_element(By.CSS_SELECTOR, "#parent-layout #motor-load-3-label-3").click()
                time.sleep(2)

                Motor_kw = self.wait.until(EC.presence_of_element_located((By.ID, "op")))
                Select(Motor_kw).select_by_index(31)
                time.sleep(2)

                # Step 5: Click the close or collapse image
                self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .border-0 > img").click()

                self.driver.find_element(By.CSS_SELECTOR, ".pt-4 > div > .btn").click()
                time.sleep(10)             

                # Step 7: Click the View Report button
                self.driver.find_element(By.CSS_SELECTOR, ".report-card > .row > .col-12 > .btn").click()

                # Step 8: Capture and validate warning message
                warning_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#panelsStayOpen-errorOne-0 > div > div > div:nth-child(3) > span"))
                )
                actual_message = warning_element.text.strip()
                expected_message = (
                "The Circuit Breaker QA 3 Rating 4 A is insufficient for the design current (248 A)"
                )

                assert actual_message == expected_message, f"Mismatch: Expected '{expected_message}', but got '{actual_message}'"
                print("Warning-TC-56 passed: Circuit breaker combination warning verified.")

        except Exception as e:
                print(f"[ERROR] Test failed due to: {e}")
                self.driver.save_screenshot("warning_tc_56_failure.png")
                raise

        finally:
                comm.logo()


    def test_warning_tc_56(self):

        comm = Common_methods(self.driver)
        Warning = warnings(self.driver)
       

        try:
                # Step 1: Setup framed component via helper function
                comm.test_proclick()
                Warning.motor1()              

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

    



    
    

    



    

    



    
    
    

   


