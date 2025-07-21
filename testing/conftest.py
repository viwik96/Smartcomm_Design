import pytest
import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
import time
from webdriver_manager.chrome import ChromeDriverManager
import json
# Add project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from utils.configuration_data import config_data   # <— import the dict directly


url1 = 'https://happy-rock-0bd606b1e.5.azurestaticapps.net'

@pytest.fixture(scope="class")
def driver(request):
    chrome_options = Options()
    chrome_options.headless = True 
    
    service = Service(ChromeDriverManager().install())  # Uses chromedriver from PATH
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    driver.get(url1)
    request.cls.driver = driver
    request.cls.wait = WebDriverWait(driver, 10)

    time.sleep(5)
    yield driver
    driver.quit()

""" @pytest.fixture(scope="class")
def test_conf_data():
    with open("conf_data.json", "r") as f:
        return json.load(f) """