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


class MessageFriend(Message, TuanGou):
    @testcase
    def test_contact_sendmessage2friend(self):
        '''消息_通讯录_给好友发消息'''
        self.enter_message()
        self.myClick(self.find_element('联系人', *self.by_message_contact_id))
        self.swipe_to_up(1)
        self.myClick(self.find_element('好友', *self.by_message_select_friend_id))
        self.myClick(self.find_element('发消息', *self.by_send_message_btn_id))
        self.send_cs_message()

    @testcase
    def test_check_cs(self):
        '''消息_通讯录_朋友商品客服'''
        self.enter_message()
        temp = 0
        while temp < 5:
            self.myClick(self.find_element('联系人', *self.by_message_contact_id))
            self.swipe_to_up(1)
            self.myClick(self.find_element('好友', *self.by_message_select_friend_id))
            self.myClick(self.find_element('进入店铺', *self.by_enter_store_btn_id))
            e = self.wait_element2(self.by_goodsNums_id)
            if e:
                if not e.text == '0':
                    self.swipe_to_up(1)
                    self.myClick(self.find_element('商品', *self.by_goodsNameTxt_id))
                    self.check_cs()
                    break
                else:
                    self.press_back_by_keycode()
                    self.myClick(self.find_element('菜单', *self.by_moreMenu_id))
                    self.myClick(self.find_element('黑名单', *self.by_set_black_list_id))
                    self.myClick(self.find_uiautomator('确定', 'text'))
                    self.press_back()
                    self.press_back()
                    self.press_back()
                    temp += 1
            else:
                
                raise NoSuchElementException

    @testcase
    def test_friend_collect(self):
        '''消息_通讯录_朋友商品收藏'''
        self.enter_message()
        temp = 0
        while temp < 5:
            self.myClick(self.find_element('联系人', *self.by_message_contact_id))
            self.swipe_to_up(1)
            self.myClick(self.find_element('好友', *self.by_message_select_friend_id))
            self.myClick(self.find_element('进入店铺', *self.by_enter_store_btn_id))
            e = self.wait_element2(self.by_goodsNums_id)
            if e:
                if not e.text == '0':
                    self.swipe_to_up(1)
                    self.myClick(self.find_element('商品', *self.by_goodsNameTxt_id))
                    s_goods_title = self.setCollected('friend')
                    self.press_back_by_keycode()  # 按返回键
                    self.press_back_by_keycode()  # 按返回键
                    self.press_back()
                    self.press_back()
                    self.check_collcet_by_mtz(s_goods_title, isfenxiao=True)
                    break
                else:
                    self.press_back_by_keycode()
                    self.myClick(self.find_element('菜单', *self.by_moreMenu_id))
                    self.myClick(self.find_element('黑名单', *self.by_set_black_list_id))
                    self.myClick(self.find_uiautomator('确定', 'text'))
                    self.press_back()
                    self.press_back()
                    self.press_back()
                    temp += 1
            else:
                
                raise NoSuchElementException

    @testcase
    def test_friend_share_proxy(self):
        '''消息_通讯录_朋友商品代销'''
        self.enter_message()
        temp = 0
        while temp < 5:
            self.myClick(self.find_element('联系人', *self.by_message_contact_id))
            self.swipe_to_up(1)
            self.myClick(self.find_element('好友', *self.by_message_select_friend_id))
            self.myClick(self.find_element('进入店铺', *self.by_enter_store_btn_id))
            e = self.wait_element2(self.by_goodsNums_id)
            if e:
                if not e.text == '0':
                    self.swipe_to_up(1)
                    self.myClick(self.find_element('商品', *self.by_goodsNameTxt_id))
                    sleep(1)
                    # 立即分享
                    self.myClick(self.find_element('立即分享', *self.by_bottomBtn2_id))
                    self.assertTrue(self.find_uiautomator('朋友圈', 'text')[0])
                    self.myClick(self.find_uiautomator('取消', 'text'))
                    # 上架代销
                    self.myClick(self.find_element('上架代销', *self.by_bottomBtn1_id))
                    e_ok = self.wait_element2(self.by_okBtn_id)
                    if e_ok:
                        self.myClick((e_ok, '确定'))
                    e = self.wait_element2(self.by_tvActionTitle_id)
                    sleep(1)
                    self.assertEqual(e.text, '下架')
                    self.myClick((e, '下架'))
                    break
                else:
                    self.press_back_by_keycode()
                    self.myClick(self.find_element('菜单', *self.by_moreMenu_id))
                    self.myClick(self.find_element('黑名单', *self.by_set_black_list_id))
                    self.myClick(self.find_uiautomator('确定', 'text'))
                    self.press_back()
                    self.press_back()
                    self.press_back()
                    temp += 1
            else:
                
                raise NoSuchElementException

if __name__ == '__main__':
    unittest.main()