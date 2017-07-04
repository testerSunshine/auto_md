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
累计奖金
'''
class TotalMoney(Mengtz):
    s_name = '萌团长收入'

    @testcase
    def test_mtz_bill(self):
        '''萌团长_累计奖金_账单'''
        self.enter_mtz()
        self.myClick(self.find_element('累计奖金', *self.TOTAL_MONEY_ID))
        self.check_bill()

    @testcase
    def test_mtz_rhz(self):
        '''萌团长_累计奖金_萌团长如何赚'''
        self.enter_mtz()
        self.myClick(self.find_element('累计奖金', *self.TOTAL_MONEY_ID))
        self.check_mtz_rhz()   #检查萌团长如何赚

    @testcase
    def test_tx_buy_gift(self):
        '''萌团长_累计奖金_购买礼包可提现_立即购买'''
        self.enter_mtz()
        self.myClick(self.find_element('累计奖金', *self.TOTAL_MONEY_ID))
        self.myClick(self.swipe_to_up_find_element('购买礼包可提现', *self.TX_BUY_GIFT_ID))
        e = self.swipe_to_up_find_element_by_accessibility_id('立即购买', u'立即购买')
        self.myClick(e)
        sleep(2)
        e_cantuan = self.wait_element2(TuanGou.by_canTuan_id)
        # self.myClick(self.find_element('我要参团', *TuanGou.by_canTuan_id))
        if e_cantuan:
            self.myClick((e_cantuan, '我要参团'))
        else:
            self.myClick(self.find_element('确认', *TuanGou.by_order_ok_id))
            sleep(2)
        if self.wait_element2(TuanGou.by_order_ok_id):
            return
        else:
            self.check_tvGoodsTips(self.s_name)
            self.check_address_info("18912727184")
            self.check_order()

    @testcase
    def test_kd_income(self):
        '''萌团长_[总收入|开店收入|萌团长]_[今日|本月|累计]'''
        D_INCOME_TYPE = {'今日萌团长收入': self.TODAY_INCOME_ID,
                         '本月收入': self.MONTH_INCOME_ID,
                         '累计收入': self.TOTAL_INCOME_ID,
                         '待确认收入': self.WAIT_CONFIRM_INCOME_ID}

        self.enter_mtz()
        self.myClick(self.find_element('累计奖金', *self.TOTAL_MONEY_ID))

        #循环点击1-3(总收入,开店收入,萌团长收入)
        for i in range(1, 4):
            self.myClick(self.find_element('收入类型', *self.MY_INCOME_TYPE_ID))
            e = self.find_element('收入', *(By.ID, self.POP_INCOME_TYPE_ID[1]+str(i)))
            self.myClick(e)

            for k, v in D_INCOME_TYPE.items():
                self.check_recode(k, *v)
            self.myClick(self.find_element('可提现金额', *self.KTX_FUND_ID))
            self.wait_element2(self.KTX_BALANCE_ID)
            self.check_recode('提现记录', *self.TX_RECODE_ID)
            self.myClick(self.find_element('返回', *self.MY_BALANCE_BACK_ID))
            sleep(2)

if __name__ == '__main__':
    unittest.main()