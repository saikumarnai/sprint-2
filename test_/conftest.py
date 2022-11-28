import time

import pytest
from selenium import webdriver
from Library.config import Config
from selenium.webdriver.firefox.options import Options

# @pytest.fixture(params=["Chrome","Firefox","Edge"])

@pytest.fixture(params=["Chrome"])
def init_driver(request):

    global driver
    browser = request.param
    print(browser)
    if browser.lower() == "chrome":
        driver = webdriver.Chrome(Config.Chrome_driver_path)

    # elif request.param=="Firefox":
    #     options=Options()
    #     options.binary_location=""
    #     driver=webdriver.Firefox(executable_path=Config.Firefox_Driver_path,options=options)
    # elif browser.lower() == "Firefox":
    #     driver = webdriver.Firefox(Config.Firefox_Driver_path)
    # elif request.param=="Edge":
    #     driver=webdriver.Edge(Config.Edge_Driver_path)

    driver.get(Config.URL)
    driver.maximize_window()
    driver.implicitly_wait(50)
    yield driver
    print(driver.title)
    # driver.save_screenshot("")
    driver.close()




