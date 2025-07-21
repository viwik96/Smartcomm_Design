from argparse import Action
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from Pages_pack1.sign_in_page import Sign_in_page
from Pages_pack1.dashboardpage import Dashboardpage
from Pages_pack1.addnewprojectpage import AddNewProjectPage
from utils.common_methods import Common_methods
from selenium.webdriver.support.ui import Select
from utils.configuration_data import config_data
from selenium.webdriver.common.action_chains import ActionChains


@pytest.mark.usefixtures("driver")
class Test_dashboardpage:

    @pytest.fixture(autouse=True)   
    def wait_for_element(self,driver):
            self.driver = driver
            self.wait = WebDriverWait(self.driver, 10)
            self.common_methods = Common_methods(self.driver)


    def test_get_started(self): # clicking on get started button
            signin = Sign_in_page(self.driver)
            signin.get_started()
            time.sleep(40)

    #Attempting to navigate first and last page of the project details.
    def test_scd_tc_113(self):
               
        comm = Common_methods(self.driver)
        comm.test_sample1()
        time.sleep(5)

        dashboard = Dashboardpage(self.driver)
        dashboard.lst_page_icon() 
        time.sleep(2)               
        # Step 2: Check that the next page icon is disabled
        next_icon = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#dashboard-table > div > ngx-datatable > div > datatable-footer > div > app-pagination > ul > li:nth-child(8)")))
        #assert not next_icon.is_enabled(), "Next icon should be disabled on the last page"

        dashboard.first_page_icon()
        # Step 4: Check that page 1 is active
        active_page = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#dashboard-table > div > ngx-datatable > div > datatable-footer > div > app-pagination > ul > li.pages.active.ng-star-inserted")))
        assert "1" in active_page.text, "Page 1 should be active"
        time.sleep(9)


    #//Verify the navigation to the specific page  
    def test_scd_tc_114(self):
        
        dashboard = Dashboardpage(self.driver)
        dashboard.specific_page()

        # Wait and get the text from footer
        footer_text_element = self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".datatable-footer-inner > .fw-bold")
        ))

        footer_text = footer_text_element.text.strip()
        print("Footer text:", footer_text)

        # Assert that the footer text contains "20"
        assert "20" in footer_text, f"Expected '20' in footer, but got: {footer_text}"


    #//Verify the Clickability of Edit icon
    def test_scd_tc_111(self):

        dashboard = Dashboardpage(self.driver)
        dashboard.edit_icon()

        # Wait and fetch the text of the settings tab
        setting_tab = self.wait.until(EC.visibility_of_element_located((By.ID, "settings-tab")))
        setting_text = setting_tab.text.strip()
        print(f"Settings tab text: {setting_text}")
        time.sleep(20)


    #To Check the Delete Icon Existence and Confirmation Dialog box
    def test_scd_tc_109(self):
        
        dashboard = Dashboardpage(self.driver)
        dashboard.delete_icon()
        time.sleep(2)  
        modal_text_element = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.modal-body.text-center")))
        modal_text = modal_text_element.text.strip()
        print(f"Delete modal message: {modal_text}")
        close_button = self.driver.find_element(By.ID, "close")
        close_button.click()
        assert "No" in close_button.text


    #Verify the Project Opens on Double Click
    def test_scd_tc_115(self):

        # Step 1: Get the project name from the card
        project_elem = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,":nth-child(1) > .ng-star-inserted > .col-auto > .work-card > .row > .col-12 > .d-block")))
        project = project_elem.text.strip()
        print(f"Project name from card: {project}")

        # Step 2: Double-click on the first work card
        card_elem = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"body > app-root > app-layout > app-dashboard > main > section > div > div > div > div.row.bg-theme-white.p-3.mb-3 > div.col-12.row.px-0.flex-nowrap.overflow-hidden > owl-carousel-o > div > div.owl-stage-outer.ng-star-inserted > owl-stage > div > div > div:nth-child(1) > a > div > div > div.work-card-body.add-new")))    
        action = ActionChains(self.driver)
        action.double_click( card_elem).perform()
        projectval_elem = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#projectDetailCollapse > div > div > div.col.client_info.rounded-end-0 > div > div.col > div > div:nth-child(2) > div > span.value.dotted-text")))
        projectval = projectval_elem.text.strip()
        print(f"Project name from detail: {projectval}")

        if project == projectval:
            print("Project names match.")
        else:
            print("Project names are different.")

        logo = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > app-root > app-layout > app-project > app-header-layout > header > nav > div > div > div.col.d-flex.align-items-center.px-2.ms-1 > a > img")))  
        logo.click()
        time.sleep(9)


    #Attempting to check the Performance of Dropdown Filtering
    def test_scd_tc_108(self):

        data1 = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#dashboard-table > div > ngx-datatable > div > datatable-footer > div > div > small"))).text

        # Step 1: Click the filter dropdown
        project_filter = self.wait.until(EC.element_to_be_clickable((By.ID, "projectFilter")))
        project_filter.click()

        # Step 2: Click the third dropdown item
        third_item = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ":nth-child(3) > .dropdown-item")))
        third_item.click()

        # Step 3: Get the selected text and log it
        selected_filter = self.wait.until(EC.visibility_of_element_located((By.ID, "projectFilter")))
        filter_text = selected_filter.text.strip()
        print("Selected Filter:", filter_text)

        # Step 4: Assert the selected filter contains "Last 6 Months"
        assert "Last 6 Months" in filter_text
        time.sleep(3)

        # Step 5: Get the data from the footer
        data2 = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#dashboard-table > div > ngx-datatable > div > datatable-footer > div > div > small"))).text

        if data1 == data2:
            print("Data is same")
        else:
            print("Data is different")


    # Search functionality scenario(validcase)
    def test_scd_tc_105(self):

        dashboard = Dashboardpage(self.driver)     

        # Step 1: Get the text before search
        before_elem = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".datatable-footer-inner > .fw-bold")))
        beforeserch = before_elem.text.strip()
        print(f"Before Search: {beforeserch}")

        # Step 2: Perform search using project name
        dashboard.project_search("jul4-14-25")
        time.sleep(4)

        # Step 3: Get the text after search
        after_elem = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".datatable-footer-inner > .fw-bold")))
        afterserch = after_elem.text.strip()
        print(f"After Search: {afterserch}")

        # Step 4: Compare before and after search
        if beforeserch != afterserch:
            print("correct")
        else:
            print("incorrect")


    # Search functionality scenario(invalidcase)
    def test_scd_tc_106(self):

        dashboard = Dashboardpage(self.driver)    
        expected_message = "No data to display"

        # Step 2: Perform search using project name
        dashboard.project_search("Project ABC")
        time.sleep(4)

        empty_row = self.wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "div.empty-row.ng-star-inserted")))

        actual_text = empty_row.text.strip()
        print(f"Displayed message: {actual_text}")

        assert actual_text == expected_message, f"Expected '{expected_message}' but got '{actual_text}'"


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

