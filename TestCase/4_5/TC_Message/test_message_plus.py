# -*- coding: utf8 -*-
from PO.warp import testcase

__author__ = 'MR.wen'

from PO.basePage import Base
from common.base_message import Message
from common.base_tuangou import TuanGou
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import unittest

class MessagePlus(Message):
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
    #添加好友
    by_message_add_contact_id = (By.ID, 'com.hs.yjseller:id/layout_contact')  # 添加通讯录好友
    by_message_add_friend_id = (By.ID, 'com.hs.yjseller:id/layout_friend')  # 添加社交好友
    by_message_add_face2face_id = (By.ID, 'com.hs.yjseller:id/layout_face2face')  # 面对面群聊
    by_message_add_scan_id = (By.ID, 'com.hs.yjseller:id/layout_scan')  # 扫一扫

    by_contact_title_id = (By.ID, 'com.hs.yjseller:id/titleTxtView')  # title
    by_nviteBtn_id = (By.ID, 'com.hs.yjseller:id/inviteBtn')  # 添加好友
    by_et_message_id = (By.ID, 'com.hs.yjseller:id/et_message')  # edit_text
    by_commit_id = (By.ID, 'com.hs.yjseller:id/tv_commit')  # 提交

    by_add_weichat_id = (By.ID, 'com.hs.yjseller:id/layout_weixin')  # 添加微信好友

    by_myqrcode_id = (By.ID, 'com.hs.yjseller:id/myQrcodeTxtView')  # 我的二维码

    by_group_chatname_id = (By.ID, 'com.hs.yjseller:id/groupNameTxtView')
    by_partner_name_id = (By.ID, 'com.hs.yjseller:id/partner_adapter_item_name')  #合伙人

    by_add_master_id = (By.ID, 'com.hs.yjseller:id/tv_add_master')  # 添加师傅

    @testcase
    def test_message_add_friend(self):
        '''消息_添加好友'''
        self.enter_message()
        self.myClick(self.find_element('加号', *self.by_message_moreDrop_id))
        es = self.find_elements_for_bounds('menuPop', 0, *self.by_message_menuTxt_id)
        for e in es:
            if '添加好友' == e[1]:
                self.myClick(e)
                bylist = [self.by_message_add_contact_id,
                          self.by_message_add_friend_id,
                          self.by_message_add_face2face_id,
                          self.by_message_add_scan_id]

                es = self.find_elements_for_by_list("four", bylist)

                for e in es[0]:
                    self.myClick((e, '1111'))
                    if "手机通讯录好友" == self.wait_element2(self.by_contact_title_id).text:
                        # e_add = self.find_element('添加', *self.by_nviteBtn_id)
                        e_add = self.wait_element2(self.by_nviteBtn_id)
                        if e_add:
                            if '添加' == e_add.text:
                                self.myClick((e_add, '添加'))
                                self.input_info(self.find_element('编辑',*self.by_et_message_id), 'hello testing!!!')
                                self.myClick(self.find_element('提交', *self.by_commit_id))
                    elif "添加社交好友" == self.wait_element2(self.by_contact_title_id).text:
                        self.assertTrue(self.wait_element2(self.by_add_weichat_id))
                    elif "面对面建群" == self.wait_element2(self.by_contact_title_id).text:
                        self.face2face()
                    elif "二维码" == self.wait_element2(self.by_contact_title_id).text:
                        self.assertTrue(self.wait_element2(self.by_myqrcode_id))
                    self.press_back()

    @testcase
    def test_message_group_chat(self):
        '''消息_发起群聊'''
        self.enter_message()
        self.myClick(self.find_element('加号', *self.by_message_moreDrop_id))
        es = self.find_elements_for_bounds('menuPop', 0, *self.by_message_menuTxt_id)
        for element in es:
            if '发起群聊' == element[1]:
                self.myClick(element)

                bylist = [self.by_message_select_group_id,  #选择一个群聊
                          self.by_message_select_face2face_id,  # 面对面建群
                          self.by_message_select_partner_id]    # 选择合伙人

                les = self.find_elements_for_by_list("3temp", bylist)
                les[0][0], les[0][1] = les[0][1], les[0][0] #交换位置
                for e in les[0]:
                    self.myClick((e, '1111'))
                    etitle = self.wait_element2(self.by_contact_title_id)
                    if etitle:
                        if "面对面建群" == etitle.text:
                            self.face2face()
                        elif "选择一个群" == etitle.text:
                            self.myClick(self.find_element('第一个群聊', *self.by_group_chatname_id))
                            self.input_message("test_message")
                    elif "选择合伙人" == self.wait_element2(self.by_top_title_id).text:
                        pnames = self.find_elements('合伙人', *self.by_partner_name_id)
                        for i, pname in enumerate(pnames[0][:3]):
                            # print '合伙人%d' %i
                            self.myClick((pname, '合伙人%d' %i))
                        self.myClick(self.find_element('确定', *self.by_confirm_id))
                        self.input_message("test_message")
                        break
                    self.press_back()
                    self.myClick(self.find_element('加号', *self.by_message_moreDrop_id))
                    self.myClick(element)

    @testcase
    def test_message_qrcode(self):
        '''消息_扫一扫'''
        self.enter_message()
        self.myClick(self.find_element('加号', *self.by_message_moreDrop_id))
        es = self.find_elements_for_bounds('menuPop', 0, *self.by_message_menuTxt_id)
        for e in es:
            if '扫一扫' == e[1]:
                self.myClick(e)
                self.assertTrue(self.wait_element2(self.by_myqrcode_id))

    @testcase
    def test_message_get_master(self):
        '''消息_找师傅_拜师'''
        self.enter_message()
        self.myClick(self.find_element('加号', *self.by_message_moreDrop_id))
        es = self.find_elements_for_bounds('menuPop', 0, *self.by_message_menuTxt_id)
        for e in es:
            if '找师傅' == e[1]:
                self.myClick(e)
                self.myClick(self.find_element('拜师', *self.by_add_master_id))
                if self.wait_element2('message', self.by_pop_message_id):
                    self.myClick(self.find_element('知道了', *self.by_button1_id))

if __name__ == '__main__':
    unittest.main()