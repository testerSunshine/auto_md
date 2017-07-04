# -*- coding: utf8 -*-
__author__ = 'ALEX.XU'

from common.index_page import Mengtz
from time import sleep
import random
import unittest
from common.base_tuangou import TuanGou
from selenium.webdriver.common.by import By
from PO.warp import testcase
'''
我的团员
'''
class MyPartner(Mengtz):
    @testcase
    def test_my_partner(self):
        self.enter_mtz()
        e = self.find_element('我的团员数', *self.MY_PARTNER_NUM_ID)
        partner_num = int(e[0].text)
        self.myClick(e)
        sleep(2)
        #如果团员数为0就进入二维码
        if partner_num > 0:
            self.assertTrue(self.wait_element2(self.MY_PARTNER_NAME_ID))
        else:
            self.myClick(self.find_element('用二维码发展团员', *self.GET_PARTNER_BY_QRCODE_ID))
            self.check_qrcode()

if __name__ == '__main__':
    unittest.main()

