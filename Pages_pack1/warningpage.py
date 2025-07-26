import time
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.common_methods import Common_methods
from selenium.webdriver.common.action_chains import ActionChains


class warnings:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.methods = Common_methods(self.driver)

    def sld_framed_component(self):

        actions = ActionChains(self.driver)

        """ view= self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#LK_Expand")))
        view.click() """

        # Hover on LV Substation
        lv_icon = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ":nth-child(1) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(lv_icon).perform()
        time.sleep(1)

        component = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#sld_menu_section > div > div:nth-child(1) > ul > li:nth-child(1) > ul > li:nth-child(1) > a > span")))
        actions.move_to_element(component).perform()

        # Click LV Substation image
        lv_image = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#LV_Substation")))
        actions.click(lv_image).perform()


        # Click on parent layout
        layout = self.wait.until(EC.element_to_be_clickable((By.ID, "parent-layout")))
        pyautogui.moveTo(400, 190)
        layout.click()
        time.sleep(4)


        # Hover on Distribution Busbar
        db_icon = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ":nth-child(2) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(db_icon).perform()
        time.sleep(1)

        busbar = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#sld_menu_section > div > div:nth-child(1) > ul > li:nth-child(2) > ul > li:nth-child(1) > a > span")))
        actions.move_to_element(busbar).perform()

        # Click Distribution Busbar image
        db_image = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#LK_DistributionBusbar")))
        actions.click(db_image).perform()

        # Move to position (420, 195) on screen (mock for .realMouseMove)
        pyautogui.moveTo(420, 195)
        time.sleep(1)
        layout.click()
        time.sleep(3)


        # Hover on Generic Load
        gl_icon = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ":nth-child(5) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(gl_icon).perform()
        time.sleep(2)

        load = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#sld_menu_section > div > div:nth-child(1) > ul > li:nth-child(5) > ul > li:nth-child(1) > a > span")))
        actions.move_to_element(load).perform()

        # Click Generic Load image
        gl_image = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#LK_GenericLoad")))
        actions.click(gl_image).perform()

        # Move Generic Load to (215, 200) using pyautogui
        pyautogui.moveTo(215, 200)
        time.sleep(1)
        layout.click()

    def add_scenario(self,scenario_name):

        # Click on the scenario input field
        scenario_input_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#sld_menu_section > div > div:nth-child(6) > ul > li > button"))
        )
        scenario_input_button.click()

        # Type the scenario name
        scenario_input = self.wait.until(
            EC.visibility_of_element_located((By.ID, "scenarioName"))
        )
        scenario_input.send_keys(scenario_name)

        # Wait and click the save/submit button
        time.sleep(3)
        save_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#delete"))
        )
        save_button.click()


    def test_add_components(self):
        
        actions = ActionChains(self.driver)

        # Hover on 3rd component icon
        third_icon = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ":nth-child(3) > #navbarDropdownMenuLink")))
        actions.move_to_element(third_icon).perform()
        time.sleep(4)

        feeder = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#sld_menu_section > div > div:nth-child(1) > ul > li:nth-child(3) > ul > li:nth-child(1) > a > span")))
        actions.move_to_element(feeder).perform()

        # Click Protection/Conductor/BBT image
        bbt_image = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#LK_ProtectionConductor")))
        actions.click(bbt_image).perform()

        # Click on parent layout
        parent_layout = self.wait.until(EC.element_to_be_clickable((By.ID, "parent-layout")))
        parent_layout.click()
        time.sleep(3)

        # Hover on 5th component icon
        fifth_icon = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ":nth-child(5) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(fifth_icon).perform()
        time.sleep(2)

        load = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#sld_menu_section > div > div:nth-child(1) > ul > li:nth-child(5) > ul > li:nth-child(1) > a > span")))
        actions.move_to_element(load).perform()

        # Click Generic Load image
        gl_image = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#LK_GenericLoad")))
        actions.click(gl_image).perform()

        # Move the component to a target location (e.g., 455, 170)
        actions.move_by_offset(455, 170).release().perform()
        time.sleep(3)

        # Click to drop on parent layout
        parent_layout.click()



    def single_component(self):

        actions = ActionChains(self.driver)

        # Hover over the first menu icon
        menu_icon = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ":nth-child(1) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(menu_icon).perform()
        time.sleep(4) 

        component = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#sld_menu_section > div > div:nth-child(1) > ul > li:nth-child(1) > ul > li:nth-child(1) > a > span")))
        actions.move_to_element(component).perform()

        # Click LV Substation image
        lv_image = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#LV_Substation")))
        actions.click(lv_image).perform()

        # Click to drop on canvas
        parent_layout = self.wait.until(EC.element_to_be_clickable((By.ID, "parent-layout")))
        parent_layout.click()
        time.sleep(4)



    def delete_all_components(self):
        
        # Loop until no more components left
        while True:
            # Find all component labels inside parent-layout
            components = self.driver.find_elements(By.CSS_SELECTOR, "#parent-layout [id*='-label-']")
            
            if not components:
                print("All components deleted.")
                break

            print(f"Deleting {len(components)} components...")

            # Click the first available component
            try:
                component = components[0]
                self.driver.execute_script("arguments[0].scrollIntoView();", component)
                component.click()
                time.sleep(1)

                # Click the delete button
                delete_btn = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".col > .btn")))
                delete_btn.click()
                print("Deleted a component.")
                time.sleep(1)  # Allow layout to update

            except Exception as e:
                print(f"Error during deletion: {e}")
                break



    def sld_framed1_component(self):

        actions = ActionChains(self.driver)

        """ view= self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#LK_Expand")))
        view.click() """

        # Hover on LV Substation
        lv_icon = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ":nth-child(1) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(lv_icon).perform()
        time.sleep(1)

        component = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#sld_menu_section > div > div:nth-child(1) > ul > li:nth-child(1) > ul > li:nth-child(1) > a > span")))
        actions.move_to_element(component).perform()

        # Click LV Substation image
        lv_image = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#LV_Substation")))
        actions.click(lv_image).perform()


        # Click on parent layout
        layout = self.wait.until(EC.element_to_be_clickable((By.ID, "parent-layout")))
        pyautogui.moveTo(400, 190)
        layout.click()
        time.sleep(4)


        # Hover on Distribution Busbar
        db_icon = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ":nth-child(2) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(db_icon).perform()
        time.sleep(1)

        busbar = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#sld_menu_section > div > div:nth-child(1) > ul > li:nth-child(2) > ul > li:nth-child(1) > a > span")))
        actions.move_to_element(busbar).perform()

        # Click Distribution Busbar image
        db_image = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#LK_DistributionBusbar")))
        actions.click(db_image).perform()

        # Move to position (420, 195) on screen (mock for .realMouseMove)
        pyautogui.moveTo(420, 195)
        time.sleep(1)
        layout.click()
        time.sleep(3)


        # Hover on Generic Load
        gl_icon = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ":nth-child(5) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(gl_icon).perform()
        time.sleep(2)

        load = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#sld_menu_section > div > div:nth-child(1) > ul > li:nth-child(5) > ul > li:nth-child(1) > a > span")))
        actions.move_to_element(load).perform()

        # Click Generic Load image
        gl_image = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#LK_GenericLoad")))
        actions.click(gl_image).perform()

        # Move Generic Load to (215, 200) using pyautogui
        pyautogui.moveTo(300, 250)
        time.sleep(1)
        layout.click()



    def warning_scenario_3(self):

        actions = ActionChains(self.driver)

        # Step 1: Hover on "LV Substation"
        lv_substation_icon = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ':nth-child(1) > #navbarDropdownMenuLink > .theme-svg')
        ))
        actions.move_to_element(lv_substation_icon).perform()
        time.sleep(4)

        lv_substation_option = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[text()='LV Substation']")
        ))
        actions.move_to_element(lv_substation_option).click().perform()

        self.wait.until(EC.element_to_be_clickable((By.ID, "parent-layout"))).click()
        time.sleep(4)

        # Step 2: Hover on "Distribution Busbar"
        distribution_busbar_icon = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ':nth-child(2) > #navbarDropdownMenuLink > .theme-svg')
        ))
        actions.move_to_element(distribution_busbar_icon).perform()

        distribution_busbar_option = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[text()='Distribution Busbar']")
        ))
        actions.move_to_element(distribution_busbar_option).click().perform()

        # Simulate drawing on canvas (LK_DistributionBusbar)
        canvas = self.wait.until(EC.presence_of_element_located((By.ID, "LK_DistributionBusbar")))
        actions.move_to_element_with_offset(canvas, 420, 195).click().perform()
        self.wait.until(EC.element_to_be_clickable((By.ID, "parent-layout"))).click()
        time.sleep(3)

        # Step 3: Hover on "Generic Load"
        generic_load_icon = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ':nth-child(5) > #navbarDropdownMenuLink > .theme-svg')
        ))
        actions.move_to_element(generic_load_icon).perform()
        time.sleep(2)

        generic_load_option = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[text()='Generic Load']")
        ))
        actions.move_to_element(generic_load_option).click().perform()

        canvas_load = self.wait.until(EC.presence_of_element_located((By.ID, "LK_GenericLoad")))
        actions.move_to_element_with_offset(canvas_load, 220, 200).click().perform()

        self.wait.until(EC.element_to_be_clickable((By.ID, "parent-layout"))).click()
        time.sleep(5)
