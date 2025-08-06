from argparse import Action
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from Pages_pack1.sign_in_page import Sign_in_page
from Pages_pack1.sldscreenpage import sldscreentest
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

    #To verify the simulate button functionalit
    def test_scd_tc_145(self):

        comm = Common_methods(self.driver)
        comm.test_sample1()
        time.sleep(5)
        comm.test_proclick()

        sldscreen = sldscreentest(self.driver)
        sldscreen.sld_framed_component()

        generate_btn = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pt-4 > div > .btn")))
        generate_btn.click()       
        time.sleep(6)

        reports_tab = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "Reports-tab")))
        reports_tab.click()

        assert reports_tab.is_displayed(), "Reports tab is not displayed"

    #Verify all the components on SLD is interactive.
    def test_scd_tc_133(self):

        sldscreen = sldscreentest(self.driver)
        
        expected = '4'

        time.sleep(3)  # Equivalent of cy.wait(3000)

        sldscreen.test_add_components()  # Call your method to set up the screen

        feeder_element = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#projectDetailCollapse > div > div > div.col-4.client_values.ms-2.rounded-start-0 > div > div:nth-child(2) > div > span.value"))
        )
        
        feeder_text = feeder_element.text.strip()
        print("Feeder text:", feeder_text)

        assert feeder_text == expected, f"Expected '{expected}' but got '{feeder_text}'"


    #Verify Component Position by mouse Performance.    
    def test_scd_tc_135(self):

       
        actions = ActionChains(self.driver)

        # Hover over second component menu item
        theme_svg = self.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, ":nth-child(2) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(theme_svg).perform()

        busbar = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#sld_menu_section > div > div:nth-child(1) > ul > li:nth-child(2) > ul > li:nth-child(1) > a > span")))
        actions.move_to_element(busbar).perform()


        # Click on the Distribution Busbar image
        busbar_img = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#LK_DistributionBusbar")))
        actions.click_and_hold(busbar_img).release().perform()

        # Move to (420, 195) offset from current element
        actions.move_to_element_with_offset(busbar_img, 420, 195).perform()
        time.sleep(3)

        # Click on parent layout
        parent_layout = self.wait.until(EC.element_to_be_clickable((By.ID, "parent-layout")))
        parent_layout.click()

        # Validate the component text
        component = self.wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".col-4 > .row > :nth-child(1)")))
        assert '2' in component.text, f"Expected text '2' not found in component. Got: '{component.text}'"

        print("SCD-TC-135: Component value contains '1'.")

   #Test the visibility of the component default values 
    def test_scd_tc_137(self):

        actions = ActionChains(self.driver)

        sldscreen = sldscreentest(self.driver)
        sldscreen.single_component()

        # Find and click the component on the layout
        parent_layout = self.wait.until(EC.presence_of_element_located((By.ID, "parent-layout")))
        lv_feeder = parent_layout.find_element(By.ID, "lv-source-1-label-1")
        actions.move_to_element(lv_feeder).click().perform()

        # Verify 'LV Feeder' appears in the properties pane
        label = self.wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#properties-tab-pane > .justify-content-between > #offcanvasRightLabel")
        ))

        assert "LV Feeder" in label.text, f"Expected 'LV Feeder' in label text, but got: {label.text}"
        print("SCD-TC-137: 'LV Feeder' label is visible in properties pane.")

    #Validating the deletion functionality of the components
    def test_scd_tc_138(self):

       
        sldscreen = sldscreentest(self.driver)
        sldscreen.single_component()

        # Step 2: Click on the component
        lv_label = self.wait.until(EC.element_to_be_clickable((By.ID, "lv-source-1-label-1")))
        lv_label.click()

        # Step 3: Verify the component label panel shows "LV Feeder"
        label_panel = self.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#properties-tab-pane > .justify-content-between > #offcanvasRightLabel")
        ))
        assert "LV Feeder" in label_panel.text, "Component label mismatch"

        # Step 4: Get the feeder label before deletion
        feeder_label_element = self.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".col-4 > .row > :nth-child(2)")
        ))
        before_del = feeder_label_element.text.strip()
        print("Before Deletion:", before_del)

        # Step 5: Click the delete button
        time.sleep(2)
        delete_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".col > .btn")))
        delete_button.click()

        # Step 6: Get the feeder label after deletion
        time.sleep(2)
        feeder_label_element = self.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".col-4 > .row > :nth-child(2)")
        ))
        after_del = feeder_label_element.text.strip()
        print("After Deletion:", after_del)

        # Step 7: Validate deletion success
        if before_del != after_del:
                print("Delete Successful")
        else:
                print("Delete Unsuccessful")

    #Test the component properties by updating default value with valid data.
    def test_scd_tc_139(self):
        

        # Step 1: Add single component (LV Substation)
        sldscreen = sldscreentest(self.driver)
        sldscreen.delete_all_components()
        sldscreen.sld_framed_component()

        # Step 2: Click on the component inside #parent-layout
        component = self.wait.until(EC.element_to_be_clickable((By.ID, "lv-source-9-label-1")))
        component.click()

        time.sleep(2)

        # Step 3: Get default value from input
        input_locator = (By.CSS_SELECTOR, ":nth-child(8) > .container-fluid > .row > .p-0 > .input-group > .form-control")
        input_field = self.wait.until(EC.presence_of_element_located(input_locator))
        default_value = input_field.get_attribute("value")
        print(f"Default Value: {default_value}")

        # Step 4: Clear and enter new value
        input_field.clear()
        input_field.send_keys("555")

        # Step 5: Click somewhere else to trigger blur/save
        blur_target =self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".justify-content-between > .border-0")))
        blur_target.click()

        # Step 6: Get updated value
        updated_value = self.wait.until(EC.presence_of_element_located(input_locator)).get_attribute("value")
        print(f"Updated Value: {updated_value}")

        # Step 7: Assertion
        assert default_value != updated_value, "Value was not updated"
        print("Value updated successfully")


    #Verify count of the used component particulars visibility
    def test_scd_tc_140(self):

        sldscreen = sldscreentest(self.driver)
        sldscreen.delete_all_components()
        sldscreen.sld_framed_component()

        # Wait until the element is visible and contains expected text
        value_element = self.wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".col-4 > .row > :nth-child(2) > .d-grid > .value")
        ))

        # Assert the text content contains '3'
        actual_text = value_element.text
        assert '9' in actual_text, f"Expected '3' in the component value, but got '{actual_text}'"

    #To verify the add new scenario functionallity.
    def test_scd_tc_144(self):

        sldscreen = sldscreentest(self.driver)
        sldscreen.delete_all_components()
        sldscreen.add_scenario('GL1')
        time.sleep(2)

        # You can validate the scenario was added by checking its presence in the dropdown or in the DOM
        # Example (update selector based on app behavior):
        try:
                scenario_name = 'GL1'
                scenario_element = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "body > modal-container > div.modal-dialog.modal-dialog-centered.new-popup-xs > div > app-scenario > div.modal-body.text-center.p-1 > div > div:nth-child(2)"))
                )
                assert scenario_element.is_displayed(), f"Scenario '{scenario_name}' was not displayed."
        except:
                assert False, f"Scenario '{scenario_name}' not found in UI after adding."

        parent = self.driver.find_element(By.CSS_SELECTOR, "body > modal-container > div.modal-dialog.modal-dialog-centered.new-popup-xs > div")
        cancel_button = parent.find_element(By.CSS_SELECTOR, "#close")
        cancel_button.click()

        comm = Common_methods(self.driver)
        comm.logo()
        time.sleep(2)

    #Validation of upload SLD icon functionality
    def test_scd_tc_146(self):
       
        comm = Common_methods(self.driver)
        comm.test_proclick()
        
        # Step 1: Add single component (assumes singlecomponent() logic exists)
        sldscreen = sldscreentest(self.driver)
        sldscreen.single_component()       

        # Step 2: Click Export SLD
        export_button = self.wait.until(EC.presence_of_element_located((By.ID, "exportSLD")))
        export_button.click()

        # Step 3: Validate export success message
        success_msg = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".ms-3 > .fw-bold")))
        assert "Success" in success_msg.text, "Export SLD failed (first attempt)"

        # Step 4: Select component and delete
        layout = self.wait.until(EC.presence_of_element_located((By.ID, "parent-layout")))
        lv_source = layout.find_element(By.ID, "lv-source-1-label-1")
        lv_source.click()

        time.sleep(2)

        delete_button = self.driver.find_element(By.CSS_SELECTOR, ".col > .btn")
        delete_button.click()

        time.sleep(2)

        # Step 5: Click Export SLD again
        export_button = self.wait.until(EC.element_to_be_clickable((By.ID, "exportSLD")))
        export_button.click()

        # Step 6: Validate export success again
        success_msg = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".ms-3 > .fw-bold")))
        assert "Success" in success_msg.text, "Export SLD failed (after delete)"

        comm = Common_methods(self.driver)
        comm.logo()

    def Test_scd_tc_148(self):
        
        comm = Common_methods(self.driver)
        comm.test_proclick()
        
        sldscreen = sldscreentest(self.driver)
        sldscreen.delete_all_components()
        sldscreen.sld_framed_component()

        labels = self.driver.find_elements(By.CSS_SELECTOR, "label[for='integration']")

        if len(labels) > 1:

                labels[1].click()
        else:
                print("Second integration label not found.")


        

    #Verify the user logout functionality 
    def Test_scd_tc_149(self):
          
        comm = Common_methods(self.driver)
        comm.logout()

        


   


    







    

    