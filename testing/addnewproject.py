import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from Pages_pack1.sign_in_page import Sign_in_page
from Pages_pack1.addnewprojectpage import AddNewProjectPage
from utils.common_methods import Common_methods
from selenium.webdriver.support.ui import Select
from utils.configuration_data import config_data
from selenium.webdriver.common.action_chains import ActionChains

@pytest.mark.usefixtures("driver")
class Test_Addnewproject:

    @pytest.fixture(autouse=True)   
    def wait_for_element(self,driver):
            self.driver = driver
            self.wait = WebDriverWait(self.driver, 10)
            self.common_methods = Common_methods(self.driver)


    def test_get_started(self): # clicking on get started button
            signin = Sign_in_page(self.driver)
            signin.get_started()
            time.sleep(40)

    def test_scd_tc_99(self):
            
        comm = Common_methods(self.driver)
        comm.test_sample1()     
        # Step 1: Click Add New Project
        addproject = AddNewProjectPage(self.driver)
        addproject.add_new_project()

        # Step 2: Assert modal label contains "New Project"
        modal_label = self.wait.until(EC.visibility_of_element_located((By.ID, "new-project-modal-label")))
        assert "New Project" in modal_label.text

        # Close the alert
        close_btn = self.driver.find_element(By.CSS_SELECTOR, "#modalDismiss")
        close_btn.click()
        time.sleep(3)


    def test_existing_project_alert(self):
        # Simulate existing project input
        project_data = {
                
            "ClientName": "jul4-14-25",
            "ProjectName": "jul4-14-25"
        }

        addproject = AddNewProjectPage(self.driver)
        addproject.add_new_project() 
        addproject.enter_project_details(project_data)

        # Wait 2 seconds (as in cy.wait)
        time.sleep(2)
        # Click Save Button
        save_btn = self.driver.find_element(By.CSS_SELECTOR, "button.btn.btn-blue-theme.btn-sm.position-relative.me-2")
        save_btn.click()

        # Wait for alert and validate text
        alert = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "alert")))
        alert_text = alert.text.strip()

        print("Captured alert:", alert_text)

        # Assert the alert contains the expected error message
        assert "jul4-14-25 is already exists." in alert_text

        # Close the alert
        close_btn = self.driver.find_element(By.CSS_SELECTOR, "#modalDismiss")
        close_btn.click()
        time.sleep(3)


    def test_scd_tc_102(self):
        # Test data
        project_details = {
            "ClientName": "Test Client 3",
            "ProjectName": "Test Project 3"
        }

        location_details = {
            "city": "Chennai",
            "address": "123 Beach Road",
            "pincode": "600001",
            "landmark": "Near Marina Beach"
        }

        # Step 1: Add New Project
        addproject = AddNewProjectPage(self.driver)
        addproject.add_new_project()
        addproject.enter_project_details(project_details)
        addproject.enter_work_site_location(location_details)
        time.sleep(2)  
        save_button = self.driver.find_element(
            By.CSS_SELECTOR, "button.btn.btn-blue-theme.btn-sm.position-relative.me-2"
        )
        save_button.click()
        time.sleep(5)


    def test_scd_tc_101(self):
        # Test data
        project_details = {
              "ClientName":"Te",
              "ProjectName":"Kg"
        }

        location_details = {
            "city": "",
            "address": "",
            "pincode": "",
            "landmark": ""
        }

        # Step 1: Click 'Add New Project'
        addproject = AddNewProjectPage(self.driver)
        addproject.add_new_project()

        addproject.enter_project_details(project_details)
        addproject.enter_work_site_location(location_details)

        # Step 4: Wait for error message and capture it
        error_element = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".error-message"))
        )
        error_text = error_element.text.strip()
        print("Captured error message:", error_text)   

        # Close the alert
        close_btn = self.driver.find_element(By.CSS_SELECTOR, "#modalDismiss")
        close_btn.click()
        time.sleep(3)

    

    def test_scd_tc_133(self):
        # Test data
        project_details = {
            "ClientName": "Client Name 4",
            "ProjectName": "Project Name 4"
        }

        location_details = {
            "city": "Chennai",
            "address": "Street Address",
            "pincode": "600001",
            "landmark": "Near Main Road"
        }

    
        addproject = AddNewProjectPage(self.driver)
        addproject.add_new_project()
        addproject.enter_project_details(project_details)
        addproject.enter_work_site_location(location_details)
        dismiss_btn = self.driver.find_element(By.CSS_SELECTOR, "#modalDismiss")
        dismiss_btn.click()
        time.sleep(3)

        # Step 5: Verify that Add Project button is visible again
        try:
            button = EC.visibility_of_element_located((By.CSS_SELECTOR, "div.col-auto.sticky-first-card"))
            print("Button is visible")
        except:
            print("Button is not visible or not found")



    def test_scd_tc_104(self):
        # Step 1: Capture text of first project row before adding
        before_element = self.wait.until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR,
                ":nth-child(1) > .datatable-body-row > .datatable-row-center > :nth-child(2)"
            ))
        )

        before_text = before_element.text.strip()
        print("Before Add:", before_text)

        # Step 2: Open "Add New Project" and fill details
        project_data = {
            "ClientName": "Client ABC",
            "ProjectName": "Project XYZ"
        }

        location_data = {
            "city": "Chennai",
            "address": "Sample Address",
            "pincode": "600001",
            "landmark": "Near Library"
        }

        addproject = AddNewProjectPage(self.driver)
        addproject.add_new_project()
        addproject.enter_project_details(project_data)
        addproject.enter_work_site_location(location_data)

        # Step 3: Click on modal dismiss (cancel button)
        dismiss_btn = self.driver.find_element(By.CSS_SELECTOR, "#modalDismiss")
        dismiss_btn.click()

        # Step 4: Capture the same project row text after dismiss
        after_element = self.wait.until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR,
                ":nth-child(1) > .datatable-body-row > .datatable-row-center > :nth-child(2)"
            ))
        )
        after_text = after_element.text.strip()
        print("After Add (Dismissed):", after_text)

        # Step 5: Compare before and after values
        if before_text == after_text:
            print("Validation Success: Project not added.")
        else:
            print("Validation Failed: Project was added unexpectedly.")

        # Step 6: Click delete icon (row 0)
        delete_icon = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#deleteProject-0 > .icon-blue-theme"))
        )
        delete_icon.click()

        # Step 7: Confirm delete
        confirm_delete = self.wait.until(EC.element_to_be_clickable((By.ID, "delete")))
        confirm_delete.click()


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
