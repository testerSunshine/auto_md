# -*- coding: utf8 -*-
from PO.warp import testcase

__author__ = 'MR.wen'
from common.base_kaidian import Kaidian
import unittest

class Add_goods(Kaidian):
    @testcase
    def test_add_ziying_goods(self):
        '''添加自营直销商品'''
        add_result = '商品上架成功'
        self.boolean_login()
        self.add_ziying_goods()
        self.add_proprietar_goods()
        self.assertEqual(self.get_add_goods_result(), add_result)
        self.myClick(self.find_element('添加完成，确认', *self.add_wancheng_id))
        self.goods_operation()

    @testcase
    def test_add_ziyingdaixiao_goods(self):
        '''添加自营直销+代销商品'''
        add_result = '商品上架成功'
        self.boolean_login()
        self.add_ziying_goods()
        self.add_proprietar_goods(type=2)
        self.assertEqual(self.get_add_goods_result(), add_result)
        self.myClick(self.find_element('添加完成，确认', *self.add_wancheng_id))
        self.goods_operation()

    @testcase
    def test_add_daixiao_goods(self):
        '''添加代销商品'''
        xiajia = '下架'
        self.boolean_login()
        self.add_ziying_goods(type=2)
        self.assertEqual(self.add_daixiao_goods(), xiajia)

    @testcase
    def test_management_goods(self):
        '''商品管理分类'''
        self.boolean_login()
        self.management_goods()

    @testcase
    def test_order_list(self):
        '''订单列表'''
        self.boolean_login()
        self.order_manger()

if __name__ == '__main__':
    unittest.main()
