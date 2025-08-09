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
        pyautogui.moveTo(200, 250)
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
        pyautogui.moveTo(250, 200)
        time.sleep(1)
        layout.click()

    def warning_scenario_4(self):
      
        actions = ActionChains(self.driver)

        # Step 1: LV Substation
        lv_icon = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ':nth-child(1) > #navbarDropdownMenuLink > .theme-svg')))
        actions.move_to_element(lv_icon).perform()
        time.sleep(4)

        lv_option = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='LV Substation']")))
        actions.move_to_element(lv_option).click().perform()

        self.wait.until(EC.element_to_be_clickable((By.ID, "parent-layout"))).click()
        time.sleep(4)

        # Step 2: Distribution Busbar (first time)
        dist_icon = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ':nth-child(2) > #navbarDropdownMenuLink > .theme-svg')))
        actions.move_to_element(dist_icon).perform()

        dist_option = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Distribution Busbar']")))
        actions.move_to_element(dist_option).click().perform()

        busbar_canvas = self.wait.until(EC.presence_of_element_located((By.ID, "LK_DistributionBusbar")))
        actions.move_to_element_with_offset(busbar_canvas, 420, 195).click().perform()

        self.wait.until(EC.element_to_be_clickable((By.ID, "parent-layout"))).click()
        time.sleep(3)

        # Step 3: Circuit Breaker
        cb_icon = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ':nth-child(3) > #navbarDropdownMenuLink > .theme-svg')))
        actions.move_to_element(cb_icon).perform()

        cb_option = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Circuit Breaker']")))
        actions.move_to_element(cb_option).click().perform()

        cb_canvas = self.wait.until(EC.presence_of_element_located((By.ID, "LK_CircuitBreaker")))
        actions.move_to_element_with_offset(cb_canvas, 530, 150).click().perform()

        self.wait.until(EC.element_to_be_clickable((By.ID, "parent-layout"))).click()
        time.sleep(3)

        # Step 4: Distribution Busbar (second time)
        dist_icon = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ':nth-child(2) > #navbarDropdownMenuLink > .theme-svg')))
        actions.move_to_element(dist_icon).perform()

        dist_option = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Distribution Busbar']")))
        actions.move_to_element(dist_option).click().perform()

        busbar_canvas_2 = self.wait.until(EC.presence_of_element_located((By.ID, "LK_DistributionBusbar")))
        actions.move_to_element_with_offset(busbar_canvas_2, 540, 300).click().perform()

        self.wait.until(EC.element_to_be_clickable((By.ID, "parent-layout"))).click()
        time.sleep(3)

        # Step 5: Generic Load
        load_icon = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ':nth-child(5) > #navbarDropdownMenuLink > .theme-svg')))
        actions.move_to_element(load_icon).perform()

        load_option = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Generic Load']")))
        actions.move_to_element(load_option).click().perform()

        load_canvas = self.wait.until(EC.presence_of_element_located((By.ID, "LK_GenericLoad")))
        actions.move_to_element_with_offset(load_canvas, 650, 200).click().perform()

        self.wait.until(EC.element_to_be_clickable((By.ID, "parent-layout"))).click()
        time.sleep(5)

    def switch1(self):
       
        actions = ActionChains(self.driver)

        # Hover and click 'LV Substation Switch'
        lv_substation_icon = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ":nth-child(1) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(lv_substation_icon).perform()
        time.sleep(4)
        lv_switch = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='LV Substation Switch']")))
        actions.move_to_element(lv_switch).click().perform()
        self.driver.find_element(By.ID, "parent-layout").click()
        time.sleep(4)

        # Hover and click 'Distribution Busbar'
        busbar_icon = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ":nth-child(2) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(busbar_icon).perform()
        dist_busbar = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Distribution Busbar']")))
        actions.move_to_element(dist_busbar).click().perform()

        # Simulate dragging/mouse move to (420, 195) on element
        canvas = self.driver.find_element(By.ID, "LK_DistributionBusbar")
        actions.move_to_element_with_offset(canvas, 420, 195).click().perform()
        self.driver.find_element(By.ID, "parent-layout").click()
        time.sleep(3)

        # Hover and click 'Generic Load'
        load_icon = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ":nth-child(5) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(load_icon).perform()
        generic_load = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Generic Load']")))
        actions.move_to_element(generic_load).click().perform()

        # Simulate placing Generic Load at (600, 300)
        load_canvas = self.driver.find_element(By.ID, "LK_GenericLoad")
        actions.move_to_element_with_offset(load_canvas, 600, 300).click().perform()
        self.driver.find_element(By.ID, "parent-layout").click()
        time.sleep(5)

    def switch2(self):
       
        actions = ActionChains(self.driver)

        # Hover and click 'LV Substation CB'
        lv_cb_icon = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ":nth-child(1) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(lv_cb_icon).perform()
        time.sleep(4)
        lv_cb_option = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='LV Substation CB']")))
        actions.move_to_element(lv_cb_option).click().perform()
        self.driver.find_element(By.ID, "parent-layout").click()

        # Hover and click 'Distribution Busbar'
        dist_icon = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ":nth-child(2) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(dist_icon).perform()
        dist_busbar_option = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Distribution Busbar']")))
        actions.move_to_element(dist_busbar_option).click().perform()
        dist_canvas = self.driver.find_element(By.ID, "LK_DistributionBusbar")
        actions.move_to_element_with_offset(dist_canvas, 420, 195).click().perform()
        self.driver.find_element(By.ID, "parent-layout").click()
        time.sleep(3)

        # Hover and click 'Switch'
        switch_icon = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ":nth-child(3) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(switch_icon).perform()
        switch_option = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Switch']")))
        actions.move_to_element(switch_option).click().perform()
        switch_canvas = self.driver.find_element(By.ID, "LK_Switch")
        actions.move_to_element_with_offset(switch_canvas, 500, 200).click().perform()
        self.driver.find_element(By.ID, "parent-layout").click()
        time.sleep(3)

        # Add another Distribution Busbar
        actions.move_to_element(dist_icon).perform()
        dist_busbar_option = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Distribution Busbar']")))
        actions.move_to_element(dist_busbar_option).click().perform()
        dist_canvas = self.driver.find_element(By.ID, "LK_DistributionBusbar")
        actions.move_to_element_with_offset(dist_canvas, 500, 300).click().perform()
        self.driver.find_element(By.ID, "parent-layout").click()
        time.sleep(3)

        # Hover and place 'Generic Load'
        load_icon = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ":nth-child(5) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(load_icon).perform()
        generic_load = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Generic Load']")))
        actions.move_to_element(generic_load).click().perform()
        load_canvas = self.driver.find_element(By.ID, "LK_GenericLoad")
        actions.move_to_element_with_offset(load_canvas, 600, 170).click().perform()
        self.driver.find_element(By.ID, "parent-layout").click()
        time.sleep(5)

    def motor1(self):
      
        actions = ActionChains(self.driver)

        # Step 1: Hover on 'LV Substation' icon
        lv_icon = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ":nth-child(1) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(lv_icon).perform()
        time.sleep(4)

        # Verify 'LV Substation' visible
        lvsubstation = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='LV Substation']")))
        actions.move_to_element(lvsubstation).click().perform()
        self.driver.find_element(By.ID, "parent-layout").click()

        # Step 2: Hover on 'Distribution Busbar' icon
        dist_icon = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ":nth-child(2) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(dist_icon).perform()

        # Click 'Distribution Busbar'
        dist_option = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Distribution Busbar']")))
        actions.move_to_element(dist_option).click().perform()

        # Move to position and click on canvas
        canvas_busbar = self.wait.until(EC.visibility_of_element_located((By.ID, "LK_DistributionBusbar")))
        actions.move_to_element_with_offset(canvas_busbar, 420, 195).click().perform()
        time.sleep(3)
        self.driver.find_element(By.ID, "parent-layout").click()

        # Step 3: Hover on 'Motor Load' icon
        motor_icon = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ":nth-child(5) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(motor_icon).perform()
        time.sleep(2)

        # Click 'Motor Load'
        motor_option = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Motor Load']")))
        actions.move_to_element(motor_option).click().perform()

        # Move to position and click on canvas
        canvas_motor = self.wait.until(EC.visibility_of_element_located((By.ID, "LK_MotorLoad")))
        actions.move_to_element_with_offset(canvas_motor, 550, 95).click().perform()

        # Click on parent layout
        self.driver.find_element(By.ID, "parent-layout").click()
        time.sleep(5)

    def complex_circuit_flow(self):

        actions = ActionChains(self.driver)

        # 1. Hover on LV Substation
        lv_icon = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ":nth-child(1) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(lv_icon).perform()
        time.sleep(4)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='LV Substation']")))
        self.driver.find_element(By.ID, "parent-layout").click()
        time.sleep(4)

        # 2. Hover and click Distribution Busbar
        dist_icon = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ":nth-child(2) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(dist_icon).perform()
        dist_busbar = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Distribution Busbar']")))
        actions.move_to_element(dist_busbar).click().perform()
        canvas_busbar = self.driver.find_element(By.ID, "LK_DistributionBusbar")
        actions.move_to_element_with_offset(canvas_busbar, 420, 195).click().perform()
        time.sleep(5)
        self.driver.find_element(By.ID, "parent-layout").click()

        # 3. Generic Load 1
        generic_icon = self.driver.find_element(By.CSS_SELECTOR, ":nth-child(5) > #navbarDropdownMenuLink > .theme-svg")
        actions.move_to_element(generic_icon).perform()
        time.sleep(2)
        generic_load = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Generic Load']")))
        actions.move_to_element(generic_load).click().perform()
        canvas_generic = self.driver.find_element(By.ID, "LK_GenericLoad")
        actions.move_to_element_with_offset(canvas_generic, 210, 205).click().perform()
        self.driver.find_element(By.ID, "parent-layout").click()

        # 4. Coupling CB
        coupling_icon = self.driver.find_element(By.CSS_SELECTOR, ":nth-child(4) > #navbarDropdownMenuLink > .theme-svg")
        actions.move_to_element(coupling_icon).perform()
        time.sleep(2)
        coupling_cb = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Coupling CB']")))
        actions.move_to_element(coupling_cb).click().perform()
        canvas_cb = self.driver.find_element(By.ID, "LK_Coupling_CB")
        actions.move_to_element_with_offset(canvas_cb, 562, 170).click().perform()
        self.driver.find_element(By.ID, "parent-layout").click()

        # 5. Distribution Busbar again
        actions.move_to_element(dist_icon).perform()
        dist_busbar = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Distribution Busbar']")))
        actions.move_to_element(dist_busbar).click().perform()
        canvas_busbar = self.driver.find_element(By.ID, "LK_DistributionBusbar")
        actions.move_to_element_with_offset(canvas_busbar, 810, 195).click().perform()
        time.sleep(3)
        self.driver.find_element(By.ID, "parent-layout").click()

        # 6. Generic Load 2
        actions.move_to_element(generic_icon).perform()
        time.sleep(2)
        generic_load = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Generic Load']")))
        actions.move_to_element(generic_load).click().perform()
        canvas_generic = self.driver.find_element(By.ID, "LK_GenericLoad")
        actions.move_to_element_with_offset(canvas_generic, 850, 205).click().perform()
        self.driver.find_element(By.ID, "parent-layout").click()

        # 7. Final LV Substation connection
        actions.move_to_element(lv_icon).perform()
        time.sleep(4)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='LV Substation']")))
        lv_canvas = self.driver.find_element(By.ID, "LV_Substation")
        actions.move_to_element_with_offset(lv_canvas, 750, 170).click().perform()
        self.driver.find_element(By.ID, "parent-layout").click()
        time.sleep(10)

    def coupling2(self):
        
        actions = ActionChains(self.driver)

        # 1. LV Substation hover and click
        lv_icon = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ":nth-child(1) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(lv_icon).perform()
        time.sleep(4)
        # Verify 'LV Substation' visible
        lvsubstation = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='LV Substation']")))
        actions.move_to_element(lvsubstation).click().perform()
        self.driver.find_element(By.ID, "parent-layout").click()
        time.sleep(4)

        # 2. Distribution Busbar
        dist_icon = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ":nth-child(2) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(dist_icon).perform()
        dist_span = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Distribution Busbar']")))
        actions.move_to_element(dist_span).click().perform()
        canvas_busbar = self.driver.find_element(By.ID, "LK_DistributionBusbar")
        actions.move_to_element_with_offset(canvas_busbar, 420, 195).click().perform()
        time.sleep(5)
        self.driver.find_element(By.ID, "parent-layout").click()

        # 3. Generic Load
        generic_icon = self.driver.find_element(By.CSS_SELECTOR, ":nth-child(5) > #navbarDropdownMenuLink > .theme-svg")
        actions.move_to_element(generic_icon).perform()
        time.sleep(2)
        generic_span = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Generic Load']")))
        actions.move_to_element(generic_span).click().perform()
        canvas_generic = self.driver.find_element(By.ID, "LK_GenericLoad")
        actions.move_to_element_with_offset(canvas_generic, 330, 55).click().perform()
        self.driver.find_element(By.ID, "parent-layout").click()

        # 4. Coupling Switch
        coupling_icon = self.driver.find_element(By.CSS_SELECTOR, ":nth-child(4) > #navbarDropdownMenuLink > .theme-svg")
        actions.move_to_element(coupling_icon).perform()
        time.sleep(2)
        coupling_span = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Coupling Switch']")))
        actions.move_to_element(coupling_span).click().perform()
        canvas_coupling = self.driver.find_element(By.ID, "LK_Coupling_Switch")
        actions.move_to_element_with_offset(canvas_coupling, 550, 200).click().perform()
        self.driver.find_element(By.ID, "parent-layout").click()

        # 5. Second Distribution Busbar
        actions.move_to_element(dist_icon).perform()
        dist_span = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Distribution Busbar']")))
        actions.move_to_element(dist_span).click().perform()
        canvas_busbar = self.driver.find_element(By.ID, "LK_DistributionBusbar")
        actions.move_to_element_with_offset(canvas_busbar, 750, 195).click().perform()
        time.sleep(3)
        self.driver.find_element(By.ID, "parent-layout").click()

        # 6. Second Generic Load
        actions.move_to_element(generic_icon).perform()
        time.sleep(2)
        generic_span = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Generic Load']")))
        actions.move_to_element(generic_span).click().perform()
        canvas_generic = self.driver.find_element(By.ID, "LK_GenericLoad")
        actions.move_to_element_with_offset(canvas_generic, 850, 95).click().perform()
        self.driver.find_element(By.ID, "parent-layout").click()

        # 7. Final LV Substation Move
        actions.move_to_element(lv_icon).perform()
        time.sleep(4)
        lvsubstation = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='LV Substation']")))
        actions.move_to_element(lvsubstation).click().perform()
        actions.move_to_element_with_offset(lvsubstation, 1000, 200).click().perform()
        self.driver.find_element(By.ID, "parent-layout").click()
        time.sleep(10)

    def ahfwarning(self):
        
        actions = ActionChains(self.driver)

        # 1. Hover LV Substation
        lv_icon = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ":nth-child(1) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(lv_icon).perform()
        time.sleep(4)
        lvsubstation = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='LV Substation']")))
        actions.move_to_element(lvsubstation).click().perform()
        self.driver.find_element(By.ID, "parent-layout").click()
        time.sleep(4)

        # 2. Distribution Busbar
        dist_icon = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ":nth-child(2) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(dist_icon).perform()
        dist_span = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Distribution Busbar']")))
        actions.move_to_element(dist_span).click().perform()
        canvas_busbar = self.driver.find_element(By.ID, "LK_DistributionBusbar")
        actions.move_to_element_with_offset(canvas_busbar, 420, 195).click().perform()
        time.sleep(3)
        self.driver.find_element(By.ID, "parent-layout").click()

        # 3. Generic Load
        generic_icon = self.driver.find_element(By.CSS_SELECTOR, ":nth-child(5) > #navbarDropdownMenuLink > .theme-svg")
        actions.move_to_element(generic_icon).perform()
        time.sleep(2)
        generic_span = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Generic Load']")))
        actions.move_to_element(generic_span).click().perform()
        canvas_generic = self.driver.find_element(By.ID, "LK_GenericLoad")
        actions.move_to_element_with_offset(canvas_generic, 330, 55).click().perform()
        self.driver.find_element(By.ID, "parent-layout").click()

        # 4. Active Harmonic Filter
        ahf_icon = self.driver.find_element(By.CSS_SELECTOR, ":nth-child(6) > #navbarDropdownMenuLink > .theme-svg")
        actions.move_to_element(ahf_icon).perform()
        time.sleep(2)
        ahf_span = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Active Harmonic Filter']")))
        actions.move_to_element(ahf_span).click().perform()
        canvas_ahf = self.driver.find_element(By.ID, "LK_AHF")
        actions.move_to_element_with_offset(canvas_ahf, 500, 95).click().perform()
        self.driver.find_element(By.ID, "parent-layout").click()
        time.sleep(5)


    def ahfwarning2(self):
        
        actions = ActionChains(self.driver)

        # 1. Hover LV Substation
        lv_icon = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ":nth-child(1) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(lv_icon).perform()
        time.sleep(4)
        lvsubstation = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='MV/LV Substation']")))
        actions.move_to_element(lvsubstation).click().perform()
        self.driver.find_element(By.ID, "parent-layout").click()
        time.sleep(4)

        # 2. Distribution Busbar
        dist_icon = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ":nth-child(2) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(dist_icon).perform()
        dist_span = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Distribution Busbar']")))
        actions.move_to_element(dist_span).click().perform()
        canvas_busbar = self.driver.find_element(By.ID, "LK_DistributionBusbar")
        actions.move_to_element_with_offset(canvas_busbar, 420, 195).click().perform()
        time.sleep(3)
        self.driver.find_element(By.ID, "parent-layout").click()

        # 3. Generic Load
        generic_icon = self.driver.find_element(By.CSS_SELECTOR, ":nth-child(5) > #navbarDropdownMenuLink > .theme-svg")
        actions.move_to_element(generic_icon).perform()
        time.sleep(2)
        generic_span = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Generic Load']")))
        actions.move_to_element(generic_span).click().perform()
        canvas_generic = self.driver.find_element(By.ID, "LK_GenericLoad")
        actions.move_to_element_with_offset(canvas_generic, 330, 55).click().perform()
        self.driver.find_element(By.ID, "parent-layout").click()

        # 4. Active Harmonic Filter
        ahf_icon = self.driver.find_element(By.CSS_SELECTOR, ":nth-child(6) > #navbarDropdownMenuLink > .theme-svg")
        actions.move_to_element(ahf_icon).perform()
        time.sleep(2)
        ahf_span = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Active Harmonic Filter']")))
        actions.move_to_element(ahf_span).click().perform()
        canvas_ahf = self.driver.find_element(By.ID, "LK_AHF")
        actions.move_to_element_with_offset(canvas_ahf, 500, 95).click().perform()
        self.driver.find_element(By.ID, "parent-layout").click()
        time.sleep(5)

    def earthingsys(self):
       
        actions = ActionChains(self.driver)

        # 1. LV Substation Hover + Click
        lv_icon = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ":nth-child(1) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(lv_icon).perform()
        lvsubstation = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='LV Substation']")))
        actions.move_to_element(lvsubstation).click().perform()
        self.driver.find_element(By.ID, "parent-layout").click()
        time.sleep(4)

        # 2. Distribution Busbar Hover + Draw
        dist_icon = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ":nth-child(2) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(dist_icon).perform()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Distribution Busbar']")))
        dist_span = self.driver.find_element(By.XPATH, "//span[text()='Distribution Busbar']")
        actions.move_to_element(dist_span).click().perform()
        canvas_busbar = self.driver.find_element(By.ID, "LK_DistributionBusbar")
        actions.move_to_element_with_offset(canvas_busbar, 420, 195).click().perform()
        time.sleep(3)
        self.driver.find_element(By.ID, "parent-layout").click()

        # 3. Double-click Busbar Connector
        busbar_connector = self.driver.find_element(By.ID, "busbar-connector-2-2")
        actions.move_to_element(busbar_connector).double_click().perform()

        # 4. LV Substation (again)
        lv_icon_2 = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ":nth-child(1) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(lv_icon_2).perform()
        time.sleep(4)
        lvsubstation = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='LV Substation']")))
        actions.move_to_element(lvsubstation).click().perform()
        actions.move_to_element_with_offset(lvsubstation, 900, 220).click().perform()
        self.driver.find_element(By.ID, "parent-layout").click()
        time.sleep(4)

        # 5. Generic Load
        generic_icon = self.driver.find_element(By.CSS_SELECTOR, ":nth-child(5) > #navbarDropdownMenuLink > .theme-svg")
        actions.move_to_element(generic_icon).perform()
        time.sleep(2)
        generic_span = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Generic Load']")))
        actions.move_to_element(generic_span).click().perform()
        canvas_generic = self.driver.find_element(By.ID, "LK_GenericLoad")
        actions.move_to_element_with_offset(canvas_generic, 330, 55).click().perform()
        self.driver.find_element(By.ID, "parent-layout").click()
        time.sleep(8)

    def cable(self):
       
        actions = ActionChains(self.driver)

        # 1. Hover on LV Substation and click on canvas
        lv_icon = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ":nth-child(1) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(lv_icon).perform()
        lvsubstation = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='LV Substation']")))
        actions.move_to_element(lvsubstation).click().perform()
        self.driver.find_element(By.ID, "parent-layout").click()
        time.sleep(4)

        # 2. Hover and click Distribution Busbar
        dist_icon = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ":nth-child(2) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(dist_icon).perform()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Distribution Busbar']"))).click()
        canvas_busbar = self.driver.find_element(By.ID, "LK_DistributionBusbar")
        actions.move_to_element_with_offset(canvas_busbar, 420, 195).click().perform()
        time.sleep(3)
        self.driver.find_element(By.ID, "parent-layout").click()

        # 3. Hover and click Generic Load
        generic_icon = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ":nth-child(5) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(generic_icon).perform()
        time.sleep(2)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Generic Load']"))).click()
        canvas_generic = self.driver.find_element(By.ID, "LK_GenericLoad")
        actions.move_to_element_with_offset(canvas_generic, 330, 60).click().perform()
        self.driver.find_element(By.ID, "parent-layout").click()
        time.sleep(3)

    def capacitor(self):
        
        actions = ActionChains(self.driver)

        # Step 1: LV Substation
        lv_icon = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ":nth-child(1) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(lv_icon).perform()
        lvsubstation = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='LV Substation']")))
        actions.move_to_element(lvsubstation).click().perform()
        self.driver.find_element(By.ID, "parent-layout").click()
        time.sleep(4)

        # Step 2: Distribution Busbar
        dist_icon = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ":nth-child(2) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(dist_icon).perform()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Distribution Busbar']"))).click()
        dist_canvas = self.driver.find_element(By.ID, "LK_DistributionBusbar")
        actions.move_to_element_with_offset(dist_canvas, 420, 195).click().perform()
        time.sleep(3)
        self.driver.find_element(By.ID, "parent-layout").click()

        # Step 3: Generic Load
        generic_icon = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ":nth-child(5) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(generic_icon).perform()
        time.sleep(2)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Generic Load']"))).click()
        generic_canvas = self.driver.find_element(By.ID, "LK_GenericLoad")
        actions.move_to_element_with_offset(generic_canvas, 320, 90).click().perform()
        self.driver.find_element(By.ID, "parent-layout").click()

        # Step 4: Capacitor Bank
        capacitor_icon = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ":nth-child(6) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(capacitor_icon).perform()
        time.sleep(2)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Capacitor Bank']"))).click()
        capacitor_canvas = self.driver.find_element(By.ID, "LK_Capacitor_Bank")
        actions.move_to_element_with_offset(capacitor_canvas, 500, 95).click().perform()
        self.driver.find_element(By.ID, "parent-layout").click()
        time.sleep(5)


    def ibcal(self):
        
        actions = ActionChains(self.driver)

        # Step 1: MV/LV Substation
        mv_lv_icon = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ":nth-child(1) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(mv_lv_icon).perform()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='MV/LV Substation']"))).click()
        self.driver.find_element(By.ID, "parent-layout").click()
        time.sleep(4)

        # Step 2: Distribution Busbar
        dist_icon = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ":nth-child(2) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(dist_icon).perform()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Distribution Busbar']"))).click()
        dist_canvas = self.driver.find_element(By.ID, "LK_DistributionBusbar")
        actions.move_to_element_with_offset(dist_canvas, 450, 120).click().perform()
        time.sleep(3)
        self.driver.find_element(By.ID, "parent-layout").click()

        # Step 3: Generic Load
        generic_icon = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ":nth-child(5) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(generic_icon).perform()
        time.sleep(2)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Generic Load']"))).click()
        generic_canvas = self.driver.find_element(By.ID, "LK_GenericLoad")
        actions.move_to_element_with_offset(generic_canvas, 370, 10).click().perform()
        self.driver.find_element(By.ID, "parent-layout").click()
        time.sleep(3)

    def ibcal1(self):
        
        actions = ActionChains(self.driver)

        # Step 1: Emergency Generator
        emergency_icon = self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ":nth-child(1) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(emergency_icon).perform()
        self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[text()='Emegency Generator']"))).click()
        self.driver.find_element(By.ID, "parent-layout").click()
        time.sleep(4)

        # Step 2: Distribution Busbar
        dist_icon = self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ":nth-child(2) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(dist_icon).perform()
        self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[text()='Distribution Busbar']"))).click()
        dist_canvas = self.driver.find_element(By.ID, "LK_DistributionBusbar")
        actions.move_to_element_with_offset(dist_canvas, 450, 50).click().perform()
        self.driver.find_element(By.ID, "parent-layout").click()
        time.sleep(3)

        # Step 3: Generic Load
        generic_icon = self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ":nth-child(5) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(generic_icon).perform()
        time.sleep(2)
        self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[text()='Generic Load']"))).click()
        generic_canvas = self.driver.find_element(By.ID, "LK_GenericLoad")
        actions.move_to_element_with_offset(generic_canvas, 550, -50).click().perform()
        self.driver.find_element(By.ID, "parent-layout").click()
        time.sleep(3)

    def ibcal2(self):
    
        actions = ActionChains(self.driver)

        # Step 1: Emergency Generator
        emergency_icon = self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ":nth-child(1) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(emergency_icon).perform()
        self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[text()='Emegency Generator']"))).click()
        self.driver.find_element(By.ID, "parent-layout").click()
        time.sleep(4)

        # Step 2: Distribution Busbar
        dist_icon = self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ":nth-child(2) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(dist_icon).perform()
        self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[text()='Distribution Busbar']"))).click()
        dist_canvas = self.driver.find_element(By.ID, "LK_DistributionBusbar")
        actions.move_to_element_with_offset(dist_canvas, 450, 50).click().perform()
        self.driver.find_element(By.ID, "parent-layout").click()
        time.sleep(3)

    def ibcal3(self):

        actions = ActionChains(self.driver)

        # Step 1: Emergency Generator
        emergency_icon = self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ":nth-child(1) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(emergency_icon).perform()
        self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[text()='Emegency Generator']"))).click()
        self.driver.find_element(By.ID, "parent-layout").click()
        time.sleep(4)

        # Step 2: Distribution Busbar
        dist_icon = self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ":nth-child(2) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(dist_icon).perform()
        self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[text()='Distribution Busbar']"))).click()
        dist_canvas = self.driver.find_element(By.ID, "LK_DistributionBusbar")
        actions.move_to_element_with_offset(dist_canvas, 450, 50).click().perform()
        self.driver.find_element(By.ID, "parent-layout").click()
        time.sleep(3)

        # Step 3: Circuit Breaker
        cb_icon = self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ":nth-child(3) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(cb_icon).perform()
        self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[text()='Circuit Breaker']"))).click()
        cb_canvas = self.driver.find_element(By.ID, "LK_CircuitBreaker")
        actions.move_to_element_with_offset(cb_canvas, 550, -50).click().perform()
        time.sleep(2)
        self.driver.find_element(By.ID, "parent-layout").click()


    def warning_scenario_58(self):
      
        actions = ActionChains(self.driver)

        # Step 1: LV Substation
        lv_icon = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ':nth-child(1) > #navbarDropdownMenuLink > .theme-svg')))
        actions.move_to_element(lv_icon).perform()
        time.sleep(4)

        lv_option = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='LV Substation']")))
        actions.move_to_element(lv_option).click().perform()

        self.wait.until(EC.element_to_be_clickable((By.ID, "parent-layout"))).click()
        time.sleep(4)

        # Step 2: Distribution Busbar (first time)
        dist_icon = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ':nth-child(2) > #navbarDropdownMenuLink > .theme-svg')))
        actions.move_to_element(dist_icon).perform()

        dist_option = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Distribution Busbar']")))
        actions.move_to_element(dist_option).click().perform()

        busbar_canvas = self.wait.until(EC.presence_of_element_located((By.ID, "LK_DistributionBusbar")))
        actions.move_to_element_with_offset(busbar_canvas, 420, 195).click().perform()

        self.wait.until(EC.element_to_be_clickable((By.ID, "parent-layout"))).click()
        time.sleep(3)

        # Step 3: Circuit Breaker
        cb_icon = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ':nth-child(3) > #navbarDropdownMenuLink > .theme-svg')))
        actions.move_to_element(cb_icon).perform()

        cb_option = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='RCD']")))
        actions.move_to_element(cb_option).click().perform()

        cb_canvas = self.wait.until(EC.presence_of_element_located((By.ID, "LK_CircuitBreaker")))
        actions.move_to_element_with_offset(cb_canvas, 530, 150).click().perform()

        self.wait.until(EC.element_to_be_clickable((By.ID, "parent-layout"))).click()
        time.sleep(3)

        # Step 4: Distribution Busbar (second time)
        dist_icon = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ':nth-child(2) > #navbarDropdownMenuLink > .theme-svg')))
        actions.move_to_element(dist_icon).perform()

        dist_option = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Distribution Busbar']")))
        actions.move_to_element(dist_option).click().perform()

        busbar_canvas_2 = self.wait.until(EC.presence_of_element_located((By.ID, "LK_DistributionBusbar")))
        actions.move_to_element_with_offset(busbar_canvas_2, 540, 300).click().perform()

        self.wait.until(EC.element_to_be_clickable((By.ID, "parent-layout"))).click()
        time.sleep(3)

        # Step 5: Generic Load
        load_icon = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ':nth-child(5) > #navbarDropdownMenuLink > .theme-svg')))
        actions.move_to_element(load_icon).perform()

        load_option = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Generic Load']")))
        actions.move_to_element(load_option).click().perform()

        load_canvas = self.wait.until(EC.presence_of_element_located((By.ID, "LK_GenericLoad")))
        actions.move_to_element_with_offset(load_canvas, 650, 200).click().perform()

        self.wait.until(EC.element_to_be_clickable((By.ID, "parent-layout"))).click()
        time.sleep(5)



    def earthingsys2(self):
       
        actions = ActionChains(self.driver)

        # 1. LV Substation Hover + Click
        lv_icon = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ":nth-child(1) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(lv_icon).perform()
        lvsubstation = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='LV Substation']")))
        actions.move_to_element(lvsubstation).click().perform()
        self.driver.find_element(By.ID, "parent-layout").click()
        time.sleep(4)

        # 2. Distribution Busbar Hover + Draw
        dist_icon = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ":nth-child(2) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(dist_icon).perform()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Distribution Busbar']")))
        dist_span = self.driver.find_element(By.XPATH, "//span[text()='Distribution Busbar']")
        actions.move_to_element(dist_span).click().perform()
        canvas_busbar = self.driver.find_element(By.ID, "LK_DistributionBusbar")
        actions.move_to_element_with_offset(canvas_busbar, 420, 195).click().perform()
        time.sleep(3)
        self.driver.find_element(By.ID, "parent-layout").click()

        # 3. Double-click Busbar Connector
        busbar_connector = self.driver.find_element(By.ID, "busbar-connector-2-2")
        actions.move_to_element(busbar_connector).double_click().perform()

        # 4. LV Substation (again)
        lv_icon_2 = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ":nth-child(1) > #navbarDropdownMenuLink > .theme-svg")))
        actions.move_to_element(lv_icon_2).perform()
        time.sleep(4)
        lvsubstation = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='LV Substation']")))
        actions.move_to_element(lvsubstation).click().perform()

        self.driver.find_element(By.ID, "lv-source-5-label-1").click()
        earthchange = self.driver.find_element(By.ID, "lv-source-5-label-1")
        earthchange.select_by_index(0)

        actions.move_to_element_with_offset(lvsubstation, 900, 220).click().perform()
        self.driver.find_element(By.ID, "parent-layout").click()
        time.sleep(4)

        # 5. Generic Load
        generic_icon = self.driver.find_element(By.CSS_SELECTOR, ":nth-child(5) > #navbarDropdownMenuLink > .theme-svg")
        actions.move_to_element(generic_icon).perform()
        time.sleep(2)
        generic_span = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Generic Load']")))
        actions.move_to_element(generic_span).click().perform()
        canvas_generic = self.driver.find_element(By.ID, "LK_GenericLoad")
        actions.move_to_element_with_offset(canvas_generic, 330, 55).click().perform()
        self.driver.find_element(By.ID, "parent-layout").click()
        time.sleep(8)