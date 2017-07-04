# -*- coding: utf8 -*-
from PO.warp import testcase

__author__ = 'MR.wen'

from PO.basePage import Base
from common.base_login import Login
from common.base_tuangou import TuanGou
from selenium.webdriver.common.by import By
from time import sleep
import unittest

class TPuTong(TuanGou):
    s_name = "普通团"
    s_customer_service_text = 'general_text_123'

    @testcase
    def test_collect(self):
        '''普通团_收藏功能'''
        self.enter_general_tuangou()
        s_goods_title = self.setCollected(self.s_name)
        self.press_back_by_keycode()  # 按返回键
        self.check_collcet_by_mtz(s_goods_title)

    @testcase
    def test_customer_service(self):
        '''普通团_发送客服消息验证'''
        self.enter_general_tuangou()
        self.myClick(self.find_element('客服', *self.by_costomer_id))
        self.verify_customer_service(self.s_customer_service_text.replace(' ', ''))

    @testcase
    def test_t_separately_buying(self):
        '''普通团_去开团_单独购买'''
        self.enter_general_tuangou()
        self.myClick(self.find_element('单独购买', *self.by_DDGM_id))
        self.check_tvGoodsTips(self.s_name, buyType=False)
        self.check_address_info(self.s_name)
        self.check_order()

    @testcase
    def test_group_buying(self):
        '''普通团_去开团_团购'''
        self.enter_general_tuangou()
        self.myClick(self.find_element('团购', *self.by_canTuan_id))
        self.check_tvGoodsTips(self.s_name)
        self.check_address_info(self.s_name)
        self.check_order()

if __name__ == '__main__':
    unittest.main()