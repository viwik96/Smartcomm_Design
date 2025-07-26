from argparse import Action
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from Pages_pack1.sign_in_page import Sign_in_page
from Pages_pack1.settingpage import settingpage
from Pages_pack1.dashboardpage import Dashboardpage
from Pages_pack1.addnewprojectpage import AddNewProjectPage
from utils.common_methods import Common_methods
from selenium.webdriver.support.ui import Select
from utils.configuration_data import config_data
from selenium.webdriver.common.action_chains import ActionChains


@pytest.mark.usefixtures("driver")
class Test_settingpage:

    @pytest.fixture(autouse=True)       
    def wait_for_element(self,driver):
            self.driver = driver
            self.wait = WebDriverWait(self.driver, 10)
            self.common_methods = Common_methods(self.driver)


    def test_get_started(self): # clicking on get started button
            signin = Sign_in_page(self.driver)
            signin.get_started()
            time.sleep(40)


    # Verify Successful Save with Default Data 
    def test_save_settings_success(self):
   
        comm = Common_methods(self.driver)
        comm.test_sample1()
        time.sleep(5)

        comm.test_proclick()
        try:
            
            popup = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > modal-container > div.logout-modal.modal-dialog.modal-dialog-centered > div")))

            # If popup is shown, click 'No' button
            no_button = self.wait.until(EC.element_to_be_clickable((By.ID, "close")))
            no_button.click()

            print("Simulation popup appeared, clicked 'No'.")

            # Then go to Settings tab
            settings_tab = self.wait.until(EC.element_to_be_clickable((By.ID, "settings-tab")))
            settings_tab.click()
            print("Navigated to Settings tab after dismissing popup.")

        except TimeoutException:

            setting = settingpage(self.driver)
            setting.settings_tab()

            # If popup does not appear, click Save Settings button
            print("Simulation popup not found, clicking Save button.")
            save_button = self.wait.until(EC.element_to_be_clickable((By.ID, "saveSettings")))
            save_button.click()

            # Validate success alert is displayed
            alert_elem = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "alert")))
            assert "Success" in alert_elem.text, f"Expected 'Success' in alert, but got: {alert_elem.text}"

            # Validate SLD tab is visible and has correct text
            sld_tab = self.wait.until(EC.visibility_of_element_located((By.ID, "sld-tab")))
            assert "SLD" in sld_tab.text, f"Expected 'SLD' in tab text, but got: {sld_tab.text}"



    # Validate the setting functionality all required fields blank .
    def test_scd_tc_120(self):
        
            setting = settingpage(self.driver)
            setting.settings_tab()
            time.sleep(2)

            # Step 2: Clear all input fields
            self.wait.until(EC.element_to_be_clickable((By.ID, "bbtAmbientTemp"))).clear()
            self.wait.until(EC.element_to_be_clickable((By.ID, "maxPermissibleU"))).clear()
            self.wait.until(EC.element_to_be_clickable((By.ID, "generalAmbientTempAir"))).clear()
            self.wait.until(EC.element_to_be_clickable((By.ID, "lighteningLoad"))).clear()
            time.sleep(5)

            # Step 3: Click on the Save button
            self.wait.until(EC.element_to_be_clickable((By.ID, "saveSettings"))).click()

            # Step 4: Verify the alert message
            alert_message = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "alert"))).text

            if "Success" in alert_message:

                tab = self.wait.until(EC.visibility_of_element_located((By.ID, "sld-tab")))
                assert "SLD" in tab.text
                print("Navigated to SLD tab after Save.")
                
            else:
               
                print("Did not navigate to SLD tab after Save.")


    #Validate the minimum and maximum field length Constraints
    def test_scd_tc_121(self):
        
        setting = settingpage(self.driver)
        setting.settings_tab()
        time.sleep(2)

        # Wait for the page to load
        self.wait.until(EC.presence_of_element_located((By.ID, "bbtAmbientTemp")))

        # Input large values into the fields
        self.driver.find_element(By.ID, "bbtAmbientTemp").clear()
        self.driver.find_element(By.ID, "bbtAmbientTemp").send_keys("1000")

        self.driver.find_element(By.ID, "maxPermissibleU").clear()
        self.driver.find_element(By.ID, "maxPermissibleU").send_keys("1000")

        self.driver.find_element(By.ID, "generalAmbientTempAir").clear()
        self.driver.find_element(By.ID, "generalAmbientTempAir").send_keys("1000")

        # Click Save
        self.driver.find_element(By.ID, "saveSettings").click()

        # Verify error message is displayed
        error_msg = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".error-message")))
        assert error_msg.is_displayed(), "Error message should be visible"

        # Check SLD tab text presence
        sld_tab = self.wait.until(EC.visibility_of_element_located((By.ID, "sld-tab")))
        assert "SLD" in sld_tab.text, "SLD tab should be present"


    #Verify the Existence of the default Units for the required field 
    def test_scd_tc_122(self):
         
        setting = settingpage(self.driver)
        setting.settings_tab()
        time.sleep(2)

        # Step 2: Wait for labels to appear
        labels = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "label[for='generalAmbientTempAir']")))
        
        # Step 3: Get text from second label
        if len(labels) > 1:
            label_text = labels[1].text.strip()
            print(f"Label text: {label_text}")
            assert '°C' in label_text, "Expected '°C' in label"
        else:
            raise AssertionError("Second label with for='generalAmbientTempAir' not found")

        # Step 4: Click save
        save_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "saveSettings")))
        save_btn.click()

        # Step 5: Confirm navigation to SLD tab
        sld_tab = self.wait.until(EC.visibility_of_element_located((By.ID, "sld-tab")))
        assert 'SLD' in sld_tab.text, "SLD tab text not found"  

    #Verify save with some mandatory fields are left blank.
    def test_scd_tc_123(self):

        setting = settingpage(self.driver)
        setting.settings_tab()
        time.sleep(2)

        # Step 2: Clear input fields
        self.wait.until(EC.presence_of_element_located((By.ID, "bbtAmbientTemp"))).clear()
        self.wait.until(EC.presence_of_element_located((By.ID, "maxPermissibleU"))).clear()
        self.wait.until(EC.presence_of_element_located((By.ID, "generalAmbientTempAir"))).clear()
        
        # Step 3: Enter value in 'lighteningLoad' field
        lightning_elem = self.wait.until(EC.presence_of_element_located((By.ID, "lighteningLoad")))
        lightning_elem.clear()

        # Step 4: Click Save
        self.wait.until(EC.element_to_be_clickable((By.ID, "saveSettings"))).click()

        # Step 5: Assert error message is displayed
        error_msg = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".error-message")))
        assert error_msg.is_displayed(), "Error message should be visible"

        # Step 6: Confirm still on SLD tab (didn't navigate away)
        sld_tab = self.wait.until(EC.visibility_of_element_located((By.ID, "sld-tab")))
        assert 'SLD' in sld_tab.text, "Expected 'SLD' in tab text"
        sld_tab.click()


    #Validate the successful save setting functionality by valid inputs. 
    """ def test_scd_tc_124(self):
    

        setting = settingpage(self.driver)
        setting.settings_tab()
        time.sleep(2)

        # Step 2: Enter valid values into form fields
        b1 = self.wait.until(EC.presence_of_element_located((By.ID, "bbtAmbientTemp")))
        b1.clear()
        self.driver.find_element(By.ID, "bbtAmbientTemp").send_keys("35")

        b2 = self.wait.until(EC.presence_of_element_located((By.ID, "maxPermissibleU")))
        b2.clear()
        self.driver.find_element(By.ID, "maxPermissibleU").send_keys("2")

        b3 = self.wait.until(EC.presence_of_element_located((By.ID, "generalAmbientTempAir")))
        b3.clear()
        self.driver.find_element(By.ID, "generalAmbientTempAir").send_keys("40")

        b4 = self.wait.until(EC.presence_of_element_located((By.ID, "lighteningLoad")))
        b4.clear()
        self.driver.find_element(By.ID, "lighteningLoad").send_keys("4")

        # Step 3: Click Save button
        self.wait.until(EC.element_to_be_clickable((By.ID, "saveSettings"))).click()
        time.sleep(5)

        # Step 4: Verify success alert
        success_alert = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert")))
        assert "Success" in success_alert.text, "Expected 'Success' in alert message"

        # Step 5: Verify still on SLD tab
        sld_tab = self.wait.until(EC.visibility_of_element_located((By.ID, "sld-tab")))
        assert "SLD" in sld_tab.text, "Expected 'SLD' tab to be visible" """


    #Verify The Dropdown Field Interaction with Keyboard 
    def test_scd_tc_125(self):
               
        setting = settingpage(self.driver)
        setting.settings_tab()
        time.sleep(2)

        # Step 2: Wait for frequency dropdown and select '60'
        frequency_dropdown = self.wait.until(EC.presence_of_element_located((By.ID, "frequency")))
        Select(frequency_dropdown).select_by_visible_text("60")

        # Step 3: Verify SLD tab is visible and contains correct text
        sld_tab = self.wait.until(EC.visibility_of_element_located((By.ID, "sld-tab")))
        assert "SLD" in sld_tab.text, "Expected 'SLD' in SLD tab text"

        # Step 4: Confirm '60' is selected in the frequency dropdown
        selected_option = Select(self.driver.find_element(By.ID, "frequency")).first_selected_option
        assert "60" in selected_option.text, "Expected '60' to be selected in frequency dropdown" 



    #Verifying the selected option in dropdown field
    def test_scd_tc_126(self):
         
        setting = settingpage(self.driver)
        setting.settings_tab()
        time.sleep(2)

        self.wait.until(EC.presence_of_element_located((By.ID, "frequency")))

        # Select '60' from the frequency dropdown
        frequency_dropdown = Select(self.driver.find_element(By.ID, "frequency"))
        frequency_dropdown.select_by_visible_text("60")

        # Assert that SLD tab is visible and contains correct text
        sld_tab = self.wait.until(EC.visibility_of_element_located((By.ID, "sld-tab")))
        assert "SLD" in sld_tab.text

        # Verify the selected value is still '60'
        selected_value = frequency_dropdown.first_selected_option.text
        assert "60" in selected_value
        

    #To ensure the slider movement intractability by clicking.
    def test_scd_tc_128(self):

        # Navigate to the settings page
        setting = settingpage(self.driver)
        setting.settings_tab()
        time.sleep(2)

        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".ms-4 > .form-switch > .switchToggle > label")))

        # Click the toggle switch
        toggle_label = self.driver.find_element(By.CSS_SELECTOR, ".ms-4 > .form-switch > .switchToggle > label")
        toggle_label.click()

        # Verify that the SLD tab contains the text "SLD"
        sld_tab = self.wait.until(EC.visibility_of_element_located((By.ID, "sld-tab")))
        assert "SLD" in sld_tab.text, "Expected 'SLD' in SLD tab text"


    #To verify the simulate button functionality in setting phase.
    def test_scd_tc_129_simulation_disabled(self):

        # Navigate to the settings page
        setting = settingpage(self.driver)
        setting.settings_tab()
        time.sleep(2)

        sim_btn = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#simulate-tab-pane > div > div > button")))

        # Check both HTML attribute and CSS class
        is_disabled_attr = sim_btn.get_attribute("disabled")
        class_list = sim_btn.get_attribute("class").lower()

        assert is_disabled_attr is not None or "disabled" in class_list or "btn-disabled" in class_list, \
            "Simulation button should be disabled"

        sld_tab = self.wait.until(EC.visibility_of_element_located((By.ID, "sld-tab")))
        assert "SLD" in sld_tab.text, "Expected 'SLD' in tab label"

        print("Simulation button is disabled and SLD tab is present - test passed.")


    #Verify the user logout functionality
    def test_scd_tc_132(self):

        # Step 2: Hover over the icon (".ms-auto > .bi")
        hover_icon = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > app-root > app-layout > app-project > app-header-layout > header > nav > div > div > div:nth-child(2) > div > div.header-dropdown > div.h-100.d-flex.align-items-center.drop-on > span.ms-3.user-name")))
        ActionChains(self.driver).move_to_element(hover_icon).perform()

        # Step 3: Click on the "a.d-flex" link
        link = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-layout > app-project > app-header-layout > header > nav > div > div > div:nth-child(2) > div > div.header-dropdown > div.p-2 > div > a > img")))
        link.click()
        logout = self.wait.until(EC.element_to_be_clickable((By.ID, "delete")))
        logout.click()
        time.sleep(2)


        