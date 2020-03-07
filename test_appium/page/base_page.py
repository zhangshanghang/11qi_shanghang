from appium.webdriver.webdriver import WebDriver


class Basepage:
    _driver: WebDriver

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, locator, value: str = None):
        if isinstance(locator, tuple):  # 如果isinstance是元组
            return self._driver.find_element(*locator)
        else:
            return self._driver.find_element(locator, value)
