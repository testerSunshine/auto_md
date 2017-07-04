# -*- coding: utf8 -*-
from PO.warp import testcase

__author__ = 'MR.wen'

from common.base_login import Login
from common.base_tuangou import TuanGou
from selenium.webdriver.common.by import By

from time import sleep
import unittest

class TMiaoSha(TuanGou):
    s_name = "秒杀团"
    s_customer_service_text = 'miaos_text_123'

    @testcase
    def test_goods_icon(self):
        '''秒杀团_购标签验证'''
        self.enterTuangou(self.s_name)
        self.swipe_to_down(1)
        sleep(2)
        self.assertTrue(self.check_icon(self.s_name))

    @testcase
    def test_collect(self):
        '''秒杀团_收藏功能'''
        self.enterTuangou(self.s_name)
        self.swipe_to_down(1)
        self.enter_fist_goods_datil_page(self.s_name)
        s_goods_title = self.setCollected(self.s_name)
        self.press_back_by_keycode()  # 按返回键
        self.press_back()
        self.check_collcet_by_mtz(s_goods_title)

    @testcase
    def test_customer_service(self):
        '''秒杀团_发送客服消息验证'''
        self.enterTuangou(self.s_name)
        self.enter_fist_goods_datil_page(self.s_name)  # 进入商详页面成功
        self.myClick(self.find_element('客服', *self.by_costomer_id))
        self.verify_customer_service(self.s_customer_service_text.replace(' ', ''))

    @testcase
    def test_t_separately_buy(self):
        '''秒杀团_马上抢_单独购买'''
        self.enterTuangou(self.s_name)
        temp = self.enter_goods_datil_page(self.s_name)
        if temp:
            self.myClick(self.find_element('单独购买', *self.by_DDGM_id))
            self.check_tvGoodsTips(self.s_name, buyType=False)
            self.check_address_info(self.s_name)
            self.check_order()

    @testcase
    def test_group_buying(self):
        '''秒杀团_去开团_团购'''
        self.enterTuangou(self.s_name)
        temp = self.enter_goods_datil_page(self.s_name)
        if temp:
            self.myClick(self.find_element('团购', *self.by_canTuan_id))
            self.check_tvGoodsTips(self.s_name)
            self.check_address_info(self.s_name)
            self.check_order()

    @testcase
    def test_more_pintuan(self):
        '''秒杀团_已售罄_更多拼团'''
        self.enterTuangou(self.s_name)
        if self.enter_goods_datil_page(self.s_name, stock=False):
            self.myClick(self.find_element('更多拼团', *self.by_canTuan_id))
            sleep(2)
        es_enter_goods = self.find_elements('商品按钮', *self.by_getGoods_id)
        self.assertTrue(es_enter_goods[0] >= 2)

    @testcase
    def test_separately_buy(self):
        '''秒杀团_已售罄_单独购买'''
        self.enterTuangou(self.s_name)
        if self.enter_goods_datil_page(self.s_name, stock=False):  # 进入商详页面成功
            self.myClick(self.find_element('单独购买', *self.by_DDGM_id))
            self.check_tvGoodsTips(self.s_name, buyType=False)
            self.check_address_info(self.s_name)
            self.check_order()

    @testcase
    def test_remind_my(self):
        '''秒杀团_提醒功能'''
        self.enterTuangou(self.s_name)
        self.__check_remaid_me()

    def __check_remaid_me(self):
        '''
        实现提醒功能
        :return:
        '''
        temp = 0
        while temp < 3:
            # es = self.find_elements_for_bounds('按钮', 0, *(By.CLASS_NAME, 'android.widget.Button'))
            es = self.find_elements_for_bounds('按钮', 0, *self.by_btn_xpath)
            isVerified = False
            if es[0] == False:
                es = self.find_elements_for_bounds('按钮', 0, *self.by_getGoods_id)
            try:
                for e in es:
                    if '提醒我' == e[1]:
                        self.myClick(e)
                        if self.find_element('登录', *(By.ID, 'com.hs.yjseller:id/login_commit'))[0]:
                            self.login_by_pwd(self.localReadConfig().getMobileInfo('mobile1'),
                                              self.localReadConfig().getMobileInfo('pwd'))
                            print "登录成功，点击..."
                            sleep(3)
                            self.myClick(e)
                            sleep(3)
                        self.assertTrue(e[0].get_attribute('name') == '取消提醒')
                        self.myClick(e)
                        isVerified = True
                        break
                    elif '取消提醒' == e[1]:
                        self.myClick(e)
                        sleep(3)
                        self.assertTrue(e[0].get_attribute('name') == '提醒我')
                        isVerified = True
                        break
            except:
                
                raise NoSuchElementException

            if isVerified:
                break
            self.swipe_to_up(1)
            temp += 1

if __name__ == '__main__':
    unittest.main()
