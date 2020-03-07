from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class Search:
    _driver: webdriver

    def __init__(self, driver):
        self._driver = driver

    def search(self , key : str):
        self._driver.find_element(MobileBy.ID, "search_input_text").send_keys(key)
        self._driver.find_element(MobileBy.ID, "name").click()
        return self

    def get_price(self, key:str) -> float:
        return float(self._driver.find_element(MobileBy.XPATH,"//*[@text='09988']/../../..//*[contains(@resource-id,'current_price')]").text)
