from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.common_methods import Common_methods
import time



class settingpage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.methods = Common_methods(self.driver)


    
    def settings_tab(self):
        # Clicks the settings tab
        settings_tab = self.wait.until(EC.element_to_be_clickable((By.ID, "settings-tab")))
        settings_tab.click()
        