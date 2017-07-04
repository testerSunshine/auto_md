# -*- coding: utf8 -*-
__author__ = 'ALEX.XU'

import unittest

from selenium.webdriver.common.by import By
from common.base_tuangou import TuanGou
from common.index_page import Mengtz
from PO.warp import testcase

class MyCollectStore(Mengtz, TuanGou):
    @testcase
    def test_collect_store(self):
        '''萌团长_收藏店铺'''
        self.search_shop(u'女装')
        shop_name = self.shop_set_collect()
        self.press_back()
        self.press_back()
        self.enter_mtz()
        self.swipe_to_up(1)
        self.swipe_to_up(1)
        self.myClick(self.find_element('关注的店铺数量', *self.SHOPNAME_NUM_ID))
        e_shop = self.find_element('第一个店铺名', *self.MTZ_SHOPNAME_ID)
        self.assertTrue(e_shop[0].text == shop_name)
        self.myClick(e_shop)
        self.myClick(self.find_element('取消关注', *self.SHOP_COLLECT_ID))
        self.assertTrue(not self.shop_is_collect())

if __name__ == '__main__':
    unittest.main()