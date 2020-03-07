from appium import webdriver
from test_appium.page.base_page import Basepage
from test_appium.page.zhuye import ZhuYe


class app(Basepage):

    _Package="com.xueqiu.android"
    _Activity=".view.WelcomeActivityAlias"
    def start(self):
        if self._driver is None:
           caps = {}
           caps["platformName"] = "android"
           caps["automationName"] = "uiautomator2"
           caps["deviceName"] = "shanghang"
           caps["appPackage"] = self._Package
           caps["appActivity"] = self._Activity
           caps["noReset"] = True
           #caps["dontStopAppOnReset"] = True
           self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
           self._driver.implicitly_wait(15)
           return  self

        else:
            print(self._driver)
            self._driver.start_activity(self._Package,self._Activity)

        return self


    def restasrt(self):
        pass

    def stop(self):
        pass

    def zhuYe(self) -> ZhuYe:
        return ZhuYe(self._driver)