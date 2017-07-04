# -*- coding: utf8 -*-
from PO.warp import testcase

from PO.basePage import Base
from common.base_message import Message
from common.base_tuangou import TuanGou
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import unittest

class MessageMaster(Message, TuanGou):
    @testcase
    def test_contact_sendmessage2master(self):
        '''消息_通讯录_给师傅发消息'''
        self.enter_message()
        self.myClick(self.find_element('联系人', *self.by_message_contact_id))
        self.myClick(self.find_element('师傅', *self.by_message_select_master_id))
        self.myClick(self.find_element('发消息', *self.by_send_message_btn_id))
        self.send_cs_message()

    @testcase
    def test_enter_master_store(self):
        '''消息_通讯录_上架师傅商品'''
        #全部上架师傅商品，然后去代销商品管理那里删除第一个代销商品
        self.enter_message()
        self.myClick(self.find_element('联系人', *self.by_message_contact_id))
        self.myClick(self.find_element('师傅', *self.by_message_select_master_id))
        self.myClick(self.find_element('进入店铺', *self.by_enter_store_btn_id))
        self.swipe_to_up(1)
        self.assertTrue(self.wait_element2(self.by_goodsNameTxtView_id))
        self.myClick(self.find_element('一键上架师傅商品', *self.by_bottomTxtView_id))
        e = self.wait_element2(self.by_messageTxtView_id)
        if e:
            if '上架成功' in e.text:
                self.myClick(self.find_element('商品管理', *self.by_button2_id))
                self.myClick(self.find_element('筛选', *self.by_goods_sort_right_id))
                self.myClick(self.find_element('代销商品', *self.by_proxy_goods_id))
                self.myClick(self.find_element('确定', *self.by_filter_btn_id))
                sleep(2)
                self.swipe_to_left_del_item(self.find_element('第一个代销商品', *self.by_productNameTxtView_id))

    @testcase
    def test_check_cs(self):
        '''消息_通讯录_师傅商品客服'''
        self.enter_message()
        self.myClick(self.find_element('联系人', *self.by_message_contact_id))
        self.myClick(self.find_element('师傅', *self.by_message_select_master_id))
        self.myClick(self.find_element('进入店铺', *self.by_enter_store_btn_id))
        self.swipe_to_up(1)
        self.myClick(self.find_element('商品', *self.by_goodsNameTxt_id))
        self.check_cs()

    @testcase
    def test_master_collect(self):
        '''消息_通讯录_朋友商品收藏'''
        self.enter_message()
        self.myClick(self.find_element('联系人', *self.by_message_contact_id))
        self.myClick(self.find_element('师傅', *self.by_message_select_master_id))
        self.myClick(self.find_element('进入店铺', *self.by_enter_store_btn_id))
        self.swipe_to_up(1)
        self.myClick(self.find_element('商品', *self.by_goodsNameTxt_id))

        s_goods_title = self.setCollected('master')
        self.press_back_by_keycode()  # 按返回键
        self.press_back_by_keycode()  # 按返回键
        self.press_back()
        self.press_back()
        self.check_collcet_by_mtz(s_goods_title, isfenxiao=True)

if __name__ == '__main__':
    unittest.main()