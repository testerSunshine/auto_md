# -*- coding: utf8 -*-
__author__ = 'ALEX.XU'

from common.index_page import Mengtz
from time import sleep
import random
import unittest
from common.base_tuangou import TuanGou
from selenium.webdriver.common.by import By
from PO.warp import testcase

class MyWallet(Mengtz, TuanGou):
    @testcase
    def test_check_all_bill(self):
        '''萌团长_钱包_检查所有账单'''
        self.enter_mtz()
        self.myClick(self.find_element('钱包', *self.WALLET_ID))
        self.myClick(self.find_element('账单', *self.WALLET_BILL_ID))
        self.check_bill_for_wallet()

    @testcase
    def test_check_asset(self):
        '''萌团长_钱包_检查所有资产'''
        self.enter_mtz()
        self.myClick(self.find_element('钱包', *self.WALLET_ID))
        self.check_assert()

if __name__ == '__main__':
    unittest.main()