# -*- coding: utf8 -*-
from PO.warp import testcase

__author__ = 'MR.wen'

from PO.basePage import Base
from common.base_login import Login
from common.base_tuangou import TuanGou
from time import sleep
import unittest
from selenium.webdriver.common.by import By

class TShiYong(TuanGou):
    s_name = "试用团"
    s_customer_service_text = 'shiyong_text123'

    @testcase
    def test_goods_icon(self):
        '''试用团_团购标签验证'''
        self.enterTuangou(self.s_name)
        self.swipe_to_down(1)

        sleep(2)
        self.assertTrue(self.check_icon(self.s_name))

    @testcase
    def test_collect(self):
        '''试用团_收藏功能'''
        self.enterTuangou(self.s_name)
        self.swipe_to_down(1)
        self.enter_fist_goods_datil_page(self.s_name)
        s_goods_title = self.setCollected(self.s_name)
        self.press_back_by_keycode()  # 按返回键
        self.press_back()
        self.check_collcet_by_mtz(s_goods_title)

    @testcase
    def test_customer_service(self):
        '''试用团_发送客服消息验证'''
        self.enterTuangou(self.s_name)
        self.enter_fist_goods_datil_page(self.s_name)  # 进入商详页面成功
        self.myClick(self.find_element('客服', *self.by_costomer_id))
        self.verify_customer_service(self.s_customer_service_text.replace(' ', ''))

    @testcase
    def test_t_separately_buy(self):
        '''试用团_申请试用_单独购买'''
        self.enterTuangou(self.s_name)
        temp = self.enter_goods_datil_page(self.s_name) # 进入商详页面
        if temp:
            self.myClick(self.find_element('单独购买', *self.by_DDGM_id))
            self.check_tvGoodsTips(self.s_name, buyType=False)
            self.check_address_info(self.s_name)
            self.check_order()

    @testcase
    def test_group_buying(self):
        '''试用团_申请试用_申请试用'''
        self.enterTuangou(self.s_name)
        temp = self.enter_goods_datil_page(self.s_name)  # 进入商详页面
        if temp:
            self.myClick(self.find_element('申请试用', *self.by_canTuan_id))
            self.check_tvGoodsTips(self.s_name)
            self.check_address_info(self.s_name)
            self.check_order()

    @testcase
    def test_check_list(self):
        '''试用团_查看名单'''
        self.enterTuangou(self.s_name)
        self.assertTrue(self.enter_goods_datil_page(self.s_name, stock=False))  # 进入商详页面成功
        self.myClick(self.find_element('查看名单', *self.by_gdpt_id))
        sleep(2)
        self.assertTrue(self.find_element('订单号', *self.by_order_num_id))
        self.myClick(self.find_element('更多试用团', *self.by_more_choujiang_id))
        # self.assertTrue(self.check_enter_tuangou(self.s_name))
        es_enter_goods = self.find_elements('商品按钮', *self.by_shiyong_btn_id)
        self.assertTrue(es_enter_goods[0] >= 1)

if __name__ == '__main__':
    unittest.main()