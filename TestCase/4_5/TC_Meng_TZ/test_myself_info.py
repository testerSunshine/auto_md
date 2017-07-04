# -*- coding: utf8 -*-
__author__ = 'MR.wen'

from common.index_page import Mengtz
from time import sleep
import random
import unittest
from common.base_tuangou import TuanGou
from selenium.webdriver.common.by import By
from PO.warp import testcase

class MyInfo(Mengtz):
    @testcase
    def test_change_portrait(self):
        '''萌团长_个人中心_更改萌团长头像'''
        self.enter_mtz()
        self.myClick(self.find_element('我的信息入口', *self.MY_ICON_ID))
        self.myClick(self.find_element('头像', *self.HEAD_IMG_ID))

        e = self.driver.find_elements_by_class_name('android.widget.TextView')[1]
        self.myClick((e, '相册选择'))
        self.swipe_to_left(1)
        # e = self.find_element("第一张照片", *self.FIRST_IMG_XPATH)
        # self.myClick(e)
        self.click(795, 469)
        onceBtn = self.wait_element2(self.ONCEBTN_ID)
        if onceBtn:
            self.myClick((onceBtn, '仅此一次'))
        #从中间滑到上面
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width / 2, height / 2, width / 2, height * 1 / 4, 250)
        sleep(2)
        e_done = self.wait_element2(self.DONE_HTC_ID)
        if e_done:
            self.myClick((e_done, '完成'))
        elif self.wait_element2(self.DONE_HUAWEI_ID):
            self.myClick((self.wait_element2(self.DONE_HUAWEI_ID), '完成'))

        temp = self.wait_element2(self.ALER_TITLE_ID, is_screenshot=False)
        if temp is not None:
            raise Exception

    @testcase
    def test_change_nickname(self):
        '''萌团长_个人中心_更改萌团长昵称'''
        self.enter_mtz()
        self.myClick(self.find_element('我的信息入口', *self.MY_ICON_ID))
        self.myClick(self.find_element('昵称', *self.NICKNAME_TEXT_ID))
        s_text = 'xzhacker' + str(random.randint(0,9))
        e_editTex = self.find_element('昵称输入框', *self.NICKNAME_ID)[0]
        e_editTex.clear()
        self.mySend_keys(e_editTex, s_text)
        self.myClick(self.find_element('保存', *self.SAVE_ID))
        e = self.wait_element2(self.ALER_TITLE_ID)
        self.assertEqual(e.text, '成功')
        self.myClick(self.find_element('确定', *self.COMFIRM_ID))
        e_nickName = self.wait_element2(self.NICKNAME_TEXT_ID)
        self.assertEqual(e_nickName.text, s_text)

    @testcase
    def test_introduction_self(self):
        '''萌团长_个人中心_修改个人介绍'''
        self.enter_mtz()
        self.myClick(self.find_element('我的信息入口', *self.MY_ICON_ID))
        e_my_info = self.find_element('个人介绍', *self.INTRODUCE_TEXT_ID)
        self.myClick(e_my_info)

        s_text = 'xzhacker_my_info' + str(random.randint(0, 9))
        e_editTex = self.find_element('昵称输入框', *self.EDIT_INTRODUCE_ID)[0]
        e_editTex.clear()
        self.mySend_keys(e_editTex, s_text)
        self.myClick(self.find_element('保存', *self.SAVE_ID))
        e = self.wait_element2(self.ALER_TITLE_ID)
        self.assertEqual(e.text, '成功')
        self.myClick(self.find_element('确定', *self.COMFIRM_ID))
        self.assertEqual(e_my_info[0].text, s_text)

    @testcase
    def test_change_address(self):
        '''萌团长_个人中心_修改收货地址'''
        self.enter_mtz()
        self.myClick(self.find_element('我的信息入口', *self.MY_ICON_ID))
        self.myClick(self.find_element('收货地址入口', *self.RECEIVE_ADDR_ID))
        #判读有无收货地址
        # com.hs.yjseller:id / address_list
        # e = self.find_element("收货地址", *self.RECEIVE_ADDR_XPATH)
        e = self.wait_element2(self.RECEIVE_ADDR_XPATH)
        if e:
            self.myClick((e, '收货地址'))
            s_phone_number = self.add_address_info()
            self.check_address_info(s_phone_number)
        else:
            self.myClick(self.find_element('添加地址', *self.APPEND_ADDR_ID))
            s_phone_number = self.add_address_info()
            self.check_address_info(s_phone_number)

if __name__ == '__main__':
    unittest.main()