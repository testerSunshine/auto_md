# -*- coding: utf8 -*-
from PO.warp import testcase

__author__ = 'MR.wen'
from common.base_kaidian import Kaidian
import unittest


class Kaidain_zhandan(Kaidian):
    @testcase
    def test_bill(self):
        '''测试账单页面'''
        self.boolean_login()
        self.myClick(self.find_element('点击账单', *self.kd_bill_id))
        len = 0
        for i in self.get_ball_status():
            i.click()
            len += 1
            if len == 6:
                break
            self.myClick(self.find_element('点击账单', *self.bill_title))

            #if empty ,pass
            if self.wait_element2('com.hs.yjseller:id/empty_text'):
                self.assertTrue(self.find_element('账单列表', *self.bill_list)[0])

        len1 = 0
        for j in self.get_ball_status(tpye=2): #测试累计账单筛选功能
            j.click()
            len1 += 1
            if len1 == 3:
                break
            self.myClick(self.find_element('累计', *self.bill_leiji))
        text = self.find_element('累计',*self.bill_leiji)[0].text.strip()
        print text
        self.assertEqual('累计', text)

    @testcase
    def test_store_statistics(self):
        '''店铺统计，今日、本月、本月交易额'''
        s_name='店铺统计'
        self.boolean_login()
        #今日
        self.assertEqual(self.store_statistics(1),s_name)
        self.store_bank()
        # 本月
        self.assertEqual(self.store_statistics(2),s_name)
        self.store_bank()
        #交易额
        self.assertEqual(self.store_statistics(3),s_name)
        self.store_bank()

    @testcase
    def test_shop_details(self):
        '''自营店铺详情'''
        self.boolean_login()
        shop_name, shop_details_name = self.my_shop()
        self.assertEqual(shop_name, shop_details_name)
        self.myClick(self.find_element('店铺返回', *self.store_details_bank_id))

if __name__ == '__main__':
    unittest.main()