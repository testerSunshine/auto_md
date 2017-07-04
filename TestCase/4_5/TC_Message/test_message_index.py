# -*- coding: utf8 -*-
from selenium.common.exceptions import NoSuchElementException

__author__ = 'MR.wen'

from PO.basePage import Base
from common.base_message import Message
from common.base_tuangou import TuanGou
from selenium.webdriver.common.by import By
from PO.warp import testcase
from time import sleep
import unittest

class MessageIndex(Message):
    by_oder_message_item_id = (By.ID, 'com.hs.yjseller:id/pushmsg_order_listitem_nextinfo')
    by_mtz_message_date_id = (By.ID, 'com.hs.yjseller:id/pushmsg_colonel_listitem_date')
    by_push_message_title_id = (By.ID, 'com.hs.yjseller:id/pushmsg_weimob_news_single_layout_title')
    by_share_message_id = (By.ID, 'com.hs.yjseller:id/rightTxtView')   #分享
    by_message_text_class = (By.CLASS_NAME, 'android.webkit.WebView')  # 分享
    by_share_cancel_btn_class = (By.CLASS_NAME, 'android.widget.Button')  # 取消
    by_message_search_id = (By.ID, 'com.hs.yjseller:id/search_hint_txt')  # 搜索
    by_message_search_edit_id = (By.ID, 'com.hs.yjseller:id/meesage_search_edit_view')  # 搜索输入
    by_message_moreDrop_id = (By.ID, 'com.hs.yjseller:id/moreDropDownView')  # 搜索输入
    by_message_menuTxt_id = (By.ID, 'com.hs.yjseller:id/menuTxtView')  # 菜单

    by_message_contact_id = (By.ID, 'com.hs.yjseller:id/common_toplayout_left')  # 菜单

    @testcase
    def test_oder_message(self):
        '''消息_订单消息'''
        self.enter_message()
        self.myClick(self.find_message_item_by_name("订单消息"))
        self.swipe_to_down(1)
        self.assertTrue(self.wait_element2(self.by_oder_message_item_id))

    @testcase
    def test_mtz_message(self):
        '''消息_萌团长消息'''
        self.enter_message()
        self.myClick(self.find_message_item_by_name("萌团长通知"))
        self.assertTrue(self.wait_element2(self.by_mtz_message_date_id))


    @testcase
    def test_push_message(self):
        '''消息_每日推荐消息'''
        self.enter_message()
        self.myClick(self.find_message_item_by_name("每日推荐"))
        self.myClick(self.find_element('消息名', *self.by_push_message_title_id))
        sleep(3)

    @testcase
    def test_md_team_message(self):
        '''消息_萌店团队消息'''
        self.enter_message()
        self.myClick(self.find_message_item_by_name("萌店团队"))
        self.myClick(self.find_element('消息名', *self.by_push_message_title_id))
        self.wait_element2(self.by_message_text_class)
        self.myClick(self.find_element('分享', *self.by_share_message_id))
        self.wait_element2(self.by_share_cancel_btn_class)

    @testcase
    def test_message_search(self):
        '''消息_搜索消息'''
        self.enter_message()
        self.myClick(self.find_element('搜索', *self.by_message_search_id))
        self.input_info(self.find_element('搜索edit', *self.by_message_search_edit_id), u"消息")

if __name__ == '__main__':
    unittest.main()