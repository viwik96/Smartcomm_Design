from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.common_methods import Common_methods
import time


class Dashboardpage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.methods = Common_methods(self.driver)

    
    def delete_icon(self):
        # Clicks the first delete icon
        self.driver.find_elements(By.CSS_SELECTOR, "img[alt='Delete']")[0].click()

    
    def edit_icon(self):
        # Clicks the first edit icon
        self.driver.find_elements(By.CSS_SELECTOR, "img[alt='Edit']")[0].click()

    def specific_page(self):
        # Clicks the 6th page link in pagination
        self.driver.find_element(By.CSS_SELECTOR, ".pager > :nth-child(6) > a").click()
        time.sleep(4)


    def lst_page_icon(self):
        # Clicks the last page icon (double-right chevron)
        self.driver.find_element(By.CSS_SELECTOR, "#dashboard-table > div > ngx-datatable > div > datatable-footer > div > app-pagination > ul > li:nth-child(9) > a > img").click()


    def first_page_icon(self):
        # Clicks the first page icon (double-left chevron)
        self.driver.find_element(By.CSS_SELECTOR, "#dashboard-table > div > ngx-datatable > div > datatable-footer > div > app-pagination > ul > li:nth-child(1) > a > img").click()


    def project_search(self, project_name):
        # Enters the project name in the search input
        search_input = self.driver.find_element(By.CSS_SELECTOR, "#projectSearch")
        search_input.clear()
        search_input.send_keys(project_name)