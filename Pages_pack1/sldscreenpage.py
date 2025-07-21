import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.common_methods import Common_methods
from selenium.webdriver.common.action_chains import ActionChains


class sldscreentest:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.methods = Common_methods(self.driver)

    def sld_framed_component(self):

        actions = ActionChains(self.driver)

        # Hover on first menu (LV Substation)
        lv_substation_menu = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ":nth-child(1) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(lv_substation_menu).perform()
        time.sleep(4)

        # Click on LV Substation image
        lv_image = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#LV_Substation")))
        actions.click_and_hold(lv_image).click().perform()

        # Click on canvas/parent-layout
        canvas = self.wait.until(EC.element_to_be_clickable((By.ID, "parent-layout")))
        canvas.click()
        time.sleep(4)

        # Hover on second menu (Distribution Busbar)
        dist_menu = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ":nth-child(2) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(dist_menu).perform()

        # Click and move Distribution Busbar image
        dist_img = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "img[alt='Distribution Busbar']")))
        actions.click_and_hold(dist_img).move_by_offset(420, 195).release().perform()
        time.sleep(3)

        canvas.click()

        # Hover on fifth menu (Generic Load)
        generic_menu = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ":nth-child(5) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(generic_menu).perform()
        time.sleep(2)

        # Click and move Generic Load image
        generic_img = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "img[alt='Generic Load']")))
        actions.click_and_hold(generic_img).move_by_offset(215, 200).release().perform()

        canvas.click()


    def place_protection_and_load(driver, wait):

        actions = ActionChains(driver)

        # Hover on 3rd navbar menu (Protection/Conductor/BBT)
        protection_menu = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ":nth-child(3) > #navbarDropdownMenuLink")))
        actions.move_to_element(protection_menu).perform()
        time.sleep(4)

        # Click on Protection/Conductor/BBT image
        protection_img = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "img[alt='Protection/Conductor/BBT']")))
        actions.click_and_hold(protection_img).click().perform()

        # Click on layout canvas
        layout = wait.until(EC.element_to_be_clickable((By.ID, "parent-layout")))
        layout.click()
        time.sleep(3)

        # Hover on 5th navbar menu (Generic Load)
        load_menu = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ":nth-child(5) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(load_menu).perform()
        time.sleep(2)

        # Click and move Generic Load image
        generic_img = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "img[alt='Generic Load']")))
        actions.click_and_hold(generic_img).move_by_offset(455, 170).release().perform()

        layout.click()


    def single_component(driver, wait):

        actions = ActionChains(driver)

        # Hover over the first navbar icon
        substation_menu = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ":nth-child(1) > #navbarDropdownMenuLink > .theme-svg")
        ))
        actions.move_to_element(substation_menu).perform()
        time.sleep(4)

        # Click the LV Substation icon
        lv_substation = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "img[alt='LV Substation']")))
        actions.click_and_hold(lv_substation).click().perform()

        # Click on the layout area to place it
        layout_area = wait.until(EC.element_to_be_clickable((By.ID, "parent-layout")))
        layout_area.click()
        time.sleep(4)


    def add_scenario(driver, wait, scenario_name):

        # Click on the scenario input field
        scenario_input_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".input-group > .py-0"))
        )
        scenario_input_button.click()

        # Type the scenario name
        scenario_input = wait.until(
            EC.visibility_of_element_located((By.ID, "scenarioName"))
        )
        scenario_input.clear()
        scenario_input.send_keys(scenario_name)

        # Wait and click the save/submit button
        time.sleep(3)
        save_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-blue-theme.btn-sm"))
        )
        save_button.click()
