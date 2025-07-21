import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.common_methods import Common_methods

# user = 'smartcommims@yopmail.com'
# password = 'Imsaqua@123'

class Sign_in_page:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.methods = Common_methods(self.driver)

    def get_started(self):
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.circle-log"))).click()
        time.sleep(1)
        


    