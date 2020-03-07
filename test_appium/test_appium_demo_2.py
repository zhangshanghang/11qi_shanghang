# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class Test_xueqiu():

    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["automationName"] = "uiautomator2"
        caps["deviceName"] = "shanghang"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["noReset"] = True
        caps["dontStopAppOnReset"]= True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(15)


    def test_search(self):
        self.driver.find_element(MobileBy.ID,"home_search").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("alibaba")
        self.driver.find_element(MobileBy.ID,  "name").click()
        self.driver.find_element(MobileBy.XPATH ,"//*[contains(@resource-id,'title_container')]/*[@text='股票']").click()
        print(float(self.driver.find_element(MobileBy.XPATH,"//*[@text='09988']/../../..//*[contains(@resource-id,'current_price')]").text))
        assert  float(self.driver.find_element(MobileBy.XPATH,"//*[@text='09988']/../../..//*[contains(@resource-id,'current_price')]").text) < 218
        #assert float(self.driver.find_element(MobileBy.ID,"current_price").text) >200


    def test_tianjia(self):
        self.driver.find_element(MobileBy.ID,"home_search").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("alibaba")
        self.driver.find_element(MobileBy.ID,  "name").click()
        self.driver.find_element(MobileBy.XPATH ,"//*[contains(@resource-id,'title_container')]/*[@text='股票']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='09988']/../../..//*[contains(@resource-id,'add_attention')]").click()
        print(self.driver.find_element(MobileBy.XPATH,"//*[@text='09988']/../../..//*[contains(@resource-id,'followed_btn')]").get_attribute('resource-id'))
        assert(self.driver.find_element(MobileBy.XPATH,"//*[@text='09988']/../../..//*[contains(@resource-id,'followed_btn')]").get_attribute('resource-id') ,"com.xueqiu.android:id/followed_btn")

    def teardown(self):
        pass
        #sleep(5)
        #self.driver.quit()








