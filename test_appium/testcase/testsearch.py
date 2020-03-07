import pytest

from test_appium.page.app_index import app


class Testsearch:

    def setup(self):
        self.zhuye = app().start().zhuYe()

    def test_search(self):
         assert self.zhuye.goto_search_page().search("alibaba").get_price("BABA") > 200




    @pytest.mark.parametrize("key ,type , price",[
        ("alibaba","BABA",200),
        ("JD","JD",20)
    ])
    def test_search_parametrize(self, key, type, price):
         assert self.zhuye.goto_search_page().search(key).get_price(type) > price
