from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from test_appium.page.base_page import Basepage
from test_appium.page.search import Search
from test_appium.page.wode import Wode


class ZhuYe(Basepage):

    def goto_search_page(self):
        self.find(MobileBy.ID, "tv_search").click()
        return Search(self._driver)

    def goto_Hangqing_page(self):
        pass

    def goto_JiaoYi_page(self):
        pass

    def goto_WoDe_page(self):
        self.find(By.XPATH, "//*[@text= '我的' ]").click()
        return Wode(self._driver)



    def goto_Xiaoxi_page(self):
        pass