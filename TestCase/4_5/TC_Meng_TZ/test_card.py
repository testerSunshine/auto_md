# -*- coding: utf8 -*-
__author__ = 'ALEX.XU'

from common.index_page import Mengtz
from time import sleep
import random
import unittest
from common.base_tuangou import TuanGou
from selenium.webdriver.common.by import By
from PO.warp import testcase
class MyCard(Mengtz, TuanGou):
    @testcase
    def test_mycard(self):
        '''测试卡卷'''
        self.enter_mtz()
        self.myClick(self.find_element('卡卷', *self.ENTER_CARD_ID))
        if self.wait_element2(self.CARD_ITEM_ID):
            self.myClick(self.find_element('兑换', *self.EXCHANGE_ID))
        else:
            pass

    @testcase
    def test_duihuanjuan(self):
        '''测试兑换券'''
        self.enter_mtz()
        self.myClick(self.find_element('卡卷', *self.ENTER_CARD_ID))
        self.myClick(self.find_element('兑换', *self.BY_DHJ_ID))

if __name__ == '__main__':
    unittest.main()