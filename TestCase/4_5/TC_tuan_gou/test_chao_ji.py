# -*- coding: utf8 -*-
from PO.warp import testcase

__author__ = 'MR.wen'

from PO.basePage import Base
from common.base_login import Login
from common.base_tuangou import TuanGou
from time import sleep
import unittest
from selenium.webdriver.common.by import By

class TChaoJi(TuanGou):
    s_name = "超级团"
    s_customer_service_text = 'chaoji_text123'

    @testcase
    def test_goods_icon(self):
        '''超级团_团购标签验证'''
        self.enterTuangou(self.s_name)
        self.swipe_to_down(1)
        sleep(2)
        self.assertTrue(self.check_icon(self.s_name))

    @testcase
    def test_collect(self):
        '''超级团_收藏功能'''
        self.enterTuangou(self.s_name)
        self.swipe_to_down(1)
        self.enter_fist_goods_datil_page(self.s_name)
        s_goods_title = self.setCollected(self.s_name)
        self.press_back_by_keycode()  # 按返回键
        self.press_back()
        self.check_collcet_by_mtz(s_goods_title)

    @testcase
    def test_customer_service(self):
        '''超级团_发送客服消息验证'''
        self.enterTuangou(self.s_name)
        self.enter_fist_goods_datil_page(self.s_name)  # 进入商详页面成功
        self.myClick(self.find_element('客服', *self.by_costomer_id))
        self.verify_customer_service(self.s_customer_service_text.replace(' ', ''))

    @testcase
    def test_separately_buy(self):
        '''超级团_去参团_'''
        self.enterTuangou(self.s_name)
        self.swipe_to_down(1)
        self.assertTrue(self.enter_goods_datil_page(self.s_name, stock=True))  # 进入商详页面成功
        self.myClick(self.find_element('我要参团', *self.by_canTuan_id))
        self.check_tvGoodsTips(self.s_name)
        self.check_address_info(self.s_name)
        self.check_order()

if __name__ == '__main__':
    unittest.main()