from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy




from test_appium.page.search import Search


class ZhuYe:
    _driver : webdriver
    def __init__(self,driver):
        self._driver=driver

    def goto_search_page(self):
        self._driver.find_element(MobileBy.ID, "home_search").click()
        return Search(self._driver)

    def goto_Hangqing_page(self):
        pass

    def goto_JiaoYi_page(self):
        pass

    def goto_WoDe_page(self):
        pass

    def goto_Xiaoxi_page(self):
        pass