# -*- coding: utf8 -*-
__author__ = 'ALEX.XU'

from common.index_page import Mengtz
from time import sleep
import random
import unittest
from common.base_tuangou import TuanGou
from PO.warp import testcase

class MyCollect(Mengtz, TuanGou):
    @testcase
    def test_buy_collect(self):
        '''萌团长_购买商品_收藏切换'''
        self.enter_mtz()
        self.swipe_to_up(1)
        self.enter_collect()
        #购买商品 切换收藏
        self.myClick(self.find_element('第一个商品', *self.by_first_collected_goods_id))
        self.assertTrue(self.is_collected("普通团"))
        self.myClick(self.find_element('收藏',*self.by_collect_id))
        self.assertTrue(not self.is_collected("普通团"))

    @testcase
    def test_distribution_collect(self):
        '''萌团长_分销商品_收藏切换'''
        self.enter_mtz()
        self.swipe_to_up(1)
        self.enter_collect()
        #点击分销商品 切换收藏
        self.myClick(self.find_element('分销', *self.by_fenXiao_id))
        if not self.wait_element2(self.by_go_where_id):
            self.myClick(self.find_element('第一个商品', *self.by_first_collected_goods_id))
            self.assertTrue(self.is_collected("普通团"))
            self.myClick(self.find_element('收藏',*self.by_collect_id))
            self.assertTrue(not self.is_collected("普通团"))

if __name__ == '__main__':
    unittest.main()