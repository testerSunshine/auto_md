# -*- coding: utf8 -*-
__author__ = 'ALEX.XU'

from common.index_page import Mengtz
from time import sleep
import random
import unittest
from common.base_tuangou import TuanGou
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from PO.warp import testcase

'''
我是萌团长
'''
class IamMTZ(Mengtz):
    s_name = '萌团长'

    @testcase
    def test_zhaomu_tuanyuan(self):
        '''萌团长_我是萌团长_招募更多团员'''
        self.enter_mtz()
        self.myClick(self.find_element('我是萌团长', *self.I_AM_MTZ_ID))
        e = self.swipe_to_up_find_element('招募更多团员', *(By.ID, 'btn1'))
        self.myClick(e)
        self.check_qrcode()

    @testcase
    def test_zhaomu_gotobuy(self):
        '''萌团长_我是萌团长_前往购买'''
        self.enter_mtz()
        self.myClick(self.find_element('我是萌团长', *self.I_AM_MTZ_ID))
        e_qwgm = self.get_qwgm()
        if e_qwgm[0]:
            if '购买礼包' in e_qwgm[0].get_attribute('name'):
                x0, y0, x1, y1 = self.get_bounds(e_qwgm)
                self.driver.tap([(int(x1-(x1-x0)/10), int(y0+(y1-y0)/2))])  #点击f前往购买
                sleep(3)
            else:
                self.myClick(e_qwgm)
        else:
            
            raise NoSuchElementException
        e = self.swipe_to_up_find_element_by_accessibility_id('立即购买', u'立即购买')
        # e = self.swipe_to_down_find_element()
        self.myClick(e)
        sleep(2)
        self.myClick(self.find_element('我要参团', *TuanGou.by_canTuan_id))
        self.check_tvGoodsTips(self.s_name)
        self.check_address_info(self.s_name)
        self.check_order()

    @testcase
    def test_my_QR_code(self):
        '''萌团长_我的二维码'''
        self.enter_mtz()
        self.myClick(self.find_element('我的二维码', *self.MY_QR_CODE_ID))
        self.check_qrcode()

if __name__ == '__main__':
    unittest.main()