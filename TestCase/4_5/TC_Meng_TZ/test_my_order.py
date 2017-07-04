# -*- coding: utf8 -*-
__author__ = 'ALEX.XU'

from common.index_page import Mengtz
from time import sleep
import random
import unittest
from common.base_tuangou import TuanGou
from selenium.webdriver.common.by import By
from PO.warp import testcase

class MyOrder(Mengtz, TuanGou):
    @testcase
    def test_all_order(self):
        '''萌团长_我的订单_所有订单'''
        self.enter_mtz()
        self.myClick(self.find_element('所有订单', *self.ALL_ORDER_ID))
        self.del_order()

    @testcase
    def test_wait_payment(self):
        '''萌团长_我的订单_待付款'''
        self.enter_mtz()
        self.myClick(self.find_element('待付款', *self.WAIT_PAYMENT_ID))
        e = self.wait_element2(self.EMPTY_BTN_ID)
        sleep(2)
        if e:
            self.myClick((e, '去逛逛'))
            self.enter_general_tuangou()
            self.myClick(self.find_element('单独购买', *self.by_DDGM_id))
            self.check_tvGoodsTips(buyType=False)
            self.check_address_info('普通团')
            self.check_order()  #进入到订单详情页
            self.press_back()
            self.press_back_by_keycode()
            self.enter_mtz()
            self.myClick(self.find_element('待付款', *self.WAIT_PAYMENT_ID))
            self.my_cancel_order()
        else:
            self.my_cancel_order()

    @testcase
    def test_wait_send(self):
        '''萌团长_我的订单_待发货'''
        self.enter_mtz()
        self.check_recode('待发货', *self.WAIT_SEND_ID)

    @testcase
    def test_wait_receive(self):
        '''萌团长_我的订单_待收货'''
        self.enter_mtz()
        self.check_recode('待收货', *self.WAIT_RECEIVE_ID)

    @testcase
    def test_wait_comment(self):
        '''萌团长_我的订单_待评价'''
        self.enter_mtz()
        self.check_recode('待评价', *self.WAIT_COMMENT_ID)

    @testcase
    def test_wait_cash_back(self):
        '''萌团长_我的订单_退款维权'''
        self.enter_mtz()
        self.check_recode('退款维权', *self.CASH_BACK_ID)

if __name__ == '__main__':
    unittest.main()