from test_appium.page.app_index import app


class Testwode:

    def setup(self):
        self.wode=app().start().zhuYe().goto_WoDe_page()

    def testwode(self):
        assert  "错误" in self.wode.loginandpassword("17875468159","123456")
