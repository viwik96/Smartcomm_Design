from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.common_methods import Common_methods

class AddNewProjectPage:
        

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.methods = Common_methods(self.driver)


    def add_new_project(self):
        # Click "Add New Project" card
        self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.col-auto.sticky-first-card"))
        ).click()


    def enter_project_details(self, newproject):
        # Fill client name
        self.driver.find_element(By.NAME, "clientName").send_keys(newproject["ClientName"])
        # Fill project name
        self.driver.find_element(By.ID, "projectName").send_keys(newproject["ProjectName"])


    def enter_work_site_location(self, locationdetails):
        # Clear and type city
        city_input = self.driver.find_element(By.ID, "city")
        city_input.clear()
        city_input.send_keys(locationdetails["city"])

        # Fill address
        self.driver.find_element(By.ID, "address").send_keys(locationdetails["address"])
        # Fill pincode
        self.driver.find_element(By.ID, "pincode").send_keys(locationdetails["pincode"])
        # Fill landmark
        self.driver.find_element(By.ID, "landMark").send_keys(locationdetails["landmark"])


