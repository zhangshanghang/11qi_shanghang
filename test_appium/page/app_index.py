from appium import webdriver

from test_appium.page.zhuye import ZhuYe


class app:
    def start(self):
        caps = {}
        caps["platformName"] = "android"
        caps["automationName"] = "uiautomator2"
        caps["deviceName"] = "shanghang"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["noReset"] = True
        caps["dontStopAppOnReset"] = True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(15)
        return  self

    def restasrt(self):
        pass

    def stop(self):
        pass

    def zhuYe(self) -> ZhuYe:
        return ZhuYe(self.driver)