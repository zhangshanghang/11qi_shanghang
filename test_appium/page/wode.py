from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.base_page import Basepage


class Wode(Basepage):
    def loginandpassword(self, phone,password):
        self.find(MobileBy.XPATH, "//*[@text='帐号密码登录']").click()
        self.find(MobileBy.ID, "login_account").send_keys(phone)
        self.find(MobileBy.ID, "login_password").send_keys(password)
        self.find(MobileBy.ID, "button_next").click()
        err = self.find(MobileBy.ID, "md_content").text
        self.find(MobileBy.ID, "md_buttonDefaultPositive").click()
        return  err