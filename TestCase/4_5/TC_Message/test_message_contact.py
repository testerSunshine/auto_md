# -*- coding: utf8 -*-
__author__ = 'MR.wen'

from PO.basePage import Base
from common.base_message import Message
from common.base_tuangou import TuanGou
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from PO.warp import testcase
import unittest

class MessageContact(Message):
    @testcase
    def test_message_del_groupchat(self):
        '''消息_删除_群聊message'''
        self.enter_message()
        es = self.find_elements('message_items', *self.by_message_item_id)
        for i, e in enumerate(es[0]):
            if '群聊' in e.text:
                self.swipe_to_left_del_item((e, '群聊%d' %i))

    @testcase
    def test_message_contact_partner(self):
        '''消息_通讯录_合伙人'''
        self.enter_message()
        self.myClick(self.find_element('联系人', *self.by_message_contact_id))
        self.myClick(self.find_element('合伙人', *self.by_message_select_partner_id))
        self.assertTrue(self.wait_element2(self.by_message_partner_name_id))
        self.myClick(self.find_element('排行', *self.by_right_id))
        es = self.find_elements('贡献榜,团队榜', *self.by_radioBtn_class)
        for e in es[0]:
            self.assertTrue(self.wait_element2(self.by_itemName_id))
        self.myClick(self.find_element('Top10', *self.by_right_id))
        es = self.find_elements('Top', *self.by_slidelist_title_id)
        for e in es[0]:
            self.myClick((e, 'top'))
            self.assertTrue(self.wait_element2(self.by_itemName_id))
            self.myClick(self.find_element('Top', *self.by_right_id))
        self.myClick((e, 'top'))
        self.myClick(self.find_element('item', *self.by_itemName_id))
        by_list = {'贡献值': self.by_contributionNum_id,
                   '合伙人':self.by_partnerNum_id,'卖出':self.by_sellNum_id}
        for k, v in by_list.items():
            self.myClick(self.find_element(k, *v))
            self.assertTrue(self.wait_element2(self.by_explanationTxt_id))

        self.swipe_to_up(1)
        self.assertTrue(self.wait_element2(self.by_goodsNameTxt_id))

    @testcase
    def test_message_account_contact_cs(self):
        '''消息_通讯录_购物号_联系客服'''
        s_text = "testing"
        self.enter_message()
        self.myClick(self.find_element('联系人', *self.by_message_contact_id))
        self.myClick(self.find_element('购物号', *self.by_buy_account_id))

        es = self.find_elements('购物号店铺列表', *self.by_first_store_id)
        if es[0]:
            for e in es[0]:
                self.myClick((e, e.get_attribute('name')))
                self.myClick(self.find_element('联系客服', *self.by_contact_customer_xpath))
                e_contact_phone = self.wait_element2(self.by_contact_phone_id,is_screenshot=False)
                if e_contact_phone:
                    self.myClick(self.find_element('电话联系', *self.by_contact_phone_id))
                    self.myClick(self.find_element('电话号码', *self.by_phone_number_id))
                    e_phone_number = self.find_element_for_by_list('拨号盘', self.by_phone_number_ids)
                    self.assertTrue(e_phone_number[0])
                    self.press_back_by_keycode()
                    self.press_back_by_keycode()
                else:
                    self.send_cs_message()
                    break
        else:
            raise NoSuchElementException(msg="购物号店铺列表未找到")

    @testcase
    def test_message_account_enter_store(self):
        '''消息_通讯录_购物号_进入店铺'''
        s_text = "testing"
        self.enter_message()
        self.myClick(self.find_element('联系人', *self.by_message_contact_id))
        self.myClick(self.find_element('购物号', *self.by_buy_account_id))
        self.myClick(self.find_element('第一个店铺', *self.by_first_store_id))
        self.myClick(self.find_element('进入店铺', *self.by_enter_store_xpath))

if __name__ == '__main__':
    unittest.main()