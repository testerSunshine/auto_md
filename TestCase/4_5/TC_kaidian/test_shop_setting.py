# -*- coding: utf8 -*-
from PO.warp import testcase

__author__ = 'MR.wen'
from common.base_kaidian import Kaidian
import unittest

class MyTestCase(Kaidian):
    @testcase
    def test_up_header_image(self):
        '''设置店铺头像-名称-地址'''
        self.boolean_login()
        self.assertTrue(self.shop_setting_header())
        self.assertEqual(self.shop_setting_shop_name(), self.shop_name)
        in_address, out_address = self.shop_setting_address()
        self.assertEqual(in_address, out_address)
    @testcase
    def test_shop_setting(self):
        '''设置店铺封面，店招，列表，导航'''
        self.boolean_login()
        self._enter_shop_setting(type=2)
        self.shop_decorate(type=1)#封面
        self.shop_decorate(type=2)#店招
        self.shop_decorate(type=3)#列表
        self.shop_decorate(type=4)#导航

    @testcase
    def test_shop_QC_share(self):
        '''店铺二维码，分享店铺'''
        self.boolean_login()
        self.shop_QC_share()

    @testcase
    def test_customer_friend_collection(self):
        '''客户管理，直接收款'''
        self.boolean_login()
        self.check_customer_management()
        self.friend_collection()

    @testcase
    def test_shop_help(self):
        '''新手帮助，萌店大学'''
        self.boolean_login()
        s_help_name = '新手指南'
        name = self.tool_box()
        self.assertEqual(name, s_help_name)

if __name__ == '__main__':
    unittest.main()
