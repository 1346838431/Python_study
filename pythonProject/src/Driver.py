from appium import webdriver
from pythonProject.src.Input_app_data import Input_phone_data
import time

class Drvier(Input_phone_data):
    """app驱动"""
    input_phone_data = Input_phone_data()
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', input_phone_data.desired_caps)
    driver.close_app()
    time.sleep(2)
    