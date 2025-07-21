import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains



class Common_methods:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.actions = ActionChains(self.driver)

    def edit_the_data(self,name_of_old_data):
        # Use an f-string to inject the variable into the XPath
        xpath = f"//span[@title='{name_of_old_data}']/ancestor::datatable-body-row//a[@title='Edit']/img"
        time.sleep(3)
        self.wait.until(EC.presence_of_element_located((By.XPATH, xpath))).click()
        # after clicking the edit button edit your data inside the tab

    def delete_the_data(self,name_of_old_data,action="yes"):
        # Use an f-string to inject the variable into the XPath
        xpath = f"//span[@title='{name_of_old_data}']/ancestor::datatable-body-row//a[@title='Delete']/img"
        time.sleep(3)
        self.wait.until(EC.presence_of_element_located((By.XPATH, xpath))).click()
        time.sleep(2)
        # after clicking the delete button your 
        popup_xpath = f"//div[contains(@class, 'modal-body')]//div[contains(text(), '{name_of_old_data}')]"
        self.wait.until(EC.visibility_of_element_located((By.XPATH, popup_xpath)))

        # Click 'Yes' or 'No' based on action
        if action.lower() == "yes":
            yes_button = self.driver.find_element(By.ID, "delete")
            yes_button.click()
            time.sleep(3)
        elif action.lower() == "no":
            no_button = self.driver.find_element(By.ID, "close")
            no_button.click()
            time.sleep(3)
        else:
            raise ValueError("Action must be 'yes' or 'no'")   

    def search_data_in_table(self, target_date):
        # XPath for pagination controls
        next_page_xpath = '//i[contains(@class, "bi-chevron-right")]/parent::a/parent::li'
        first_page_xpath = '//i[contains(@class, "bi-chevron-double-left")]/parent::a/parent::li'
        date_cells_xpath = '//datatable-body//div//datatable-body-cell[*]'  
        while True:
            # Step 1: Wait for table to load on the current page
            time.sleep(3)  # optional slight delay to allow rows to render
            rows = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, date_cells_xpath)))
            # Step 2: Check for target_date in current page rows
            for row in rows:
                if target_date in row.text:
                    print(f"Found date: {target_date}")
                    return True
            # Step 3: Check if 'Next' page is disabled (end of pagination)
            next_button = self.wait.until(EC.presence_of_element_located((By.XPATH, next_page_xpath)))
            if 'disabled' in next_button.get_attribute("class"):
                print("Date not found. Reached end of pagination.")
                break
            # Step 4: Click next page
            next_button.click()
        # Step 5: Return to first page if date wasn't found
        first_button = self.wait.until(EC.presence_of_element_located((By.XPATH, first_page_xpath)))
        if 'disabled' not in first_button.get_attribute("class"):
            first_button.click()
            print("Returned to first page.")
        return False

    def check_box(self,locator):
        self.wait.until(EC.presence_of_element_located(locator)).click()
        if self.wait.until(EC.presence_of_element_located(locator)).is_selected():
            print("check box is selected")
        else:
            print("check box is not selected")
    
    def scroll_to_element(self, by_type, locator):
        try:
            element = self.wait.until(EC.presence_of_element_located((by_type, locator)))
            self.driver.execute_script("""arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});""", element)        
        except:
            raise Exception(f"Element not found: {locator}")
    
    def scroll_down(self, by_type, locator):
        try:
            element = self.wait.until(EC.presence_of_element_located((by_type, locator)))
            self.driver.execute_script("""arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});""", element)        
        except:
            raise Exception(f"Element not found: {locator}")

    def scroll_up(self, by_type, locator):
        try:
            element = self.wait.until(EC.presence_of_element_located((by_type, locator)))
            self.driver.execute_script("window.scrollTo({top: 0, behavior: 'smooth'});", element)        
        except:
            raise Exception(f"Element not found: {locator}")
        
    def move_to_element(self, by_type, locator):
        try:
            element = self.wait.until(EC.presence_of_element_located((by_type, locator)))
            self.actions.move_to_element(element).perform()
        except:
            raise Exception(f"Element not found: {locator}")
            
    def key_down(self,key):
        self.actions.key_down(key).perform()

    def key_up(self,key):
        self.actions.key_up(key).perform()

    def key_press(self,key):
        self.actions.key_press(key).perform()

    def take_screenshot(driver, name="screenshot"):
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        folder = "screenshots"
        if not os.path.exists(folder):
            os.makedirs(folder)
        path = os.path.join(folder, f"{name}_{timestamp}.png")
        driver.save_screenshot(path)
        print(f"Screenshot saved to {path}")
        
    def test_sample1(self):
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#roleCard3"))).click()
        time.sleep(5)
    
    def test_proclick(self):
        project = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > app-root > app-layout > app-dashboard > main > section > div > div > div > div.row.bg-theme-white.p-3.mb-3 > div.col-12.row.px-0.flex-nowrap.overflow-hidden > owl-carousel-o > div > div.owl-stage-outer.ng-star-inserted > owl-stage > div > div > div:nth-child(1) > a > div > div > div.work-card-body.add-new > div > img")))
        ActionChains(self.driver).double_click(project).perform()
        time.sleep(9)