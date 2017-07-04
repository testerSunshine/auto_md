# -*- coding: utf8 -*-
__author__ = 'ALEX.XU'

from common.index_page import Mengtz
from time import sleep
import random
import unittest
from common.base_tuangou import TuanGou
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from PO.warp import testcase

class MySetting(Mengtz, TuanGou):

    SETTING_ID = (By.ID, 'com.hs.yjseller:id/iv_my_setting')
    MESSAGE_ID = (By.ID, 'com.hs.yjseller:id/layout_new_msg')
    SOUND_ID = (By.ID, 'com.hs.yjseller:id/layout_sound')
    COMPOUND_BTN_CLASS = (By.CLASS_NAME, 'android.widget.CompoundButton')
    CLEAR_CHAT_ID = (By.ID, 'com.hs.yjseller:id/tv_clear_chat_data') #清空聊天记录
    SETTING_BACK_ID = (By.ID, 'com.hs.yjseller:id/common_toplayout_left')  # 返回
    SETTING_OK_ID = (By.ID, 'com.hs.yjseller:id/common_toplayout_right')  # 确定

    KCY_ID = (By.ID, 'com.hs.yjseller:id/tz_kcy_layout')
    KCY_EDIT_ID = (By.ID, 'com.hs.yjseller:id/kcy_setting_edit')

    CYY_ID = (By.ID, 'com.hs.yjseller:id/tz_cyy_layout')
    ADD_CYY_ID = (By.ID, 'com.hs.yjseller:id/single_cyy_foot_layout')  # 添加常用语
    EDIT_CYY_ID = (By.ID, 'com.hs.yjseller:id/kcy_setting_edit')  # 编辑
    EDIT_ALL_CYY_ID = (By.ID, 'com.hs.yjseller:id/rightBtn')  # 编辑所有常用语

    CYY_ITEM_ID = (By.ID, 'com.hs.yjseller:id/cyy_message_adapter_item_name')  # 编辑所有常用语
    OVER_ID = (By.ID, 'com.hs.yjseller:id/rightBtn')  # 完成

    SMRZ_ID = (By.ID, 'com.hs.yjseller:id/center_setting_name_auth')
    JYDB_ID = (By.ID, 'com.hs.yjseller:id/layout_insure_exchange')
    ZHAQ_ID = (By.ID, 'com.hs.yjseller:id/tv_account_safe')
    MOBILE_CHANGE_ID = (By.ID, 'com.hs.yjseller:id/tv_mobile_change_title')
    CHANGE_BTN_ID = (By.ID, 'com.hs.yjseller:id/btn_change')    #按钮
    PAY_PWD_CHANGE_ID = (By.ID, 'com.hs.yjseller:id/tv_pay_pwd_title')
    PWD_FORGET_ID = (By.ID, 'com.hs.yjseller:id/payPasswordForget')
    CLEAR_CACHE_ID = (By.ID, 'com.hs.yjseller:id/layout_clear_cache')
    COMFIRM_CLEAR_CACHE_ID = (By.ID, 'com.hs.yjseller:id/common_confirm_second')
    CLEAR_CACHE_OK_ID = (By.ID, 'android:id/button2')
    LAUNCH_VIEWS_CLOSE_ID = (By.ID, 'com.hs.yjseller:id/launch_views_close')

    ABOUTUS_FUNC_ID = (By.ID, 'com.hs.yjseller:id/aboutus_function')

    ADVICE_ID = (By.ID, 'com.hs.yjseller:id/aboutus_jianyifankui')
    EDIT_ADVICE_ID = (By.ID, 'com.hs.yjseller:id/feedback_content')
    EDIT_CONTACT_ID = (By.ID, 'com.hs.yjseller:id/feedback_contact')

    COMMIT_ID = (By.ID, 'com.hs.yjseller:id/feedback_submit')


    # _ID = (By.ID, '')
    GYMD_ID = (By.ID, 'com.hs.yjseller:id/tv_meng_dian')
    LXKF_ID = (By.ID, 'com.hs.yjseller:id/tv_custom_service')
    BY_CCS_ID = (By.ID, 'com.hs.yjseller:id/tv_custom_service')   #联系客服
    BY_DIAL_INPUT_ID = (By.ID, 'android:id/input') #htc拨号
    BY_DIAL_INPUT_HUAWEI_ID = (By.ID, 'com.android.contacts:id/dialButton')  # huawei拨号
    BY_LOGOUT_ID = (By.ID, 'com.hs.yjseller:id/tv_account_exit')  # 登出
    BY_MENU_ID = (By.ID, 'com.hs.yjseller:id/menuView')  # 菜单

    @testcase
    def test_mtz_message(self):
        '''萌团长_设置_测试消息'''
        self.enter_mtz()
        self.swipe_to_up(1)
        self.swipe_to_up(1)
        self.myClick(self.find_element('设置', *self.SETTING_ID))
        self.myClick(self.find_element('消息设置', *self.MESSAGE_ID))
        self.myClick(self.find_element('声音震动', *self.SOUND_ID))
        es = self.find_elements('切换按钮', *self.COMPOUND_BTN_CLASS)
        for e in es[0]:
            self.myClick((e, '切换按钮'))
            self.myClick((e, '切换按钮'))

        self.myClick(self.find_element('返回', *self.SETTING_BACK_ID))

        es = self.find_elements('切换按钮', *self.COMPOUND_BTN_CLASS)
        for e in es[0]:
            self.myClick((e, '切换按钮'))
            self.myClick((e, '切换按钮'))

        #清空聊天记录
        self.myClick(self.find_element('清空聊天记录', *self.CLEAR_CHAT_ID))
        self.myClick(self.find_element('清空', *(By.CLASS_NAME, 'android.widget.TextView')))

    @testcase
    def test_mtz_kcy(self):
        '''萌团长_设置_开场语'''
        self.enter_mtz()
        self.swipe_to_up(1)
        self.swipe_to_up(1)
        self.myClick(self.find_element('设置', *self.SETTING_ID))
        self.myClick(self.find_element('开场语', *self.KCY_ID))
        self.input_info(self.find_element('开场语编辑', *self.KCY_EDIT_ID), 'Hello world!!!')
        self.myClick(self.find_element('确定', *self.SETTING_OK_ID))

    @testcase
    def test_mtz_cyy(self):
        '''萌团长_设置_常用语'''
        self.enter_mtz()
        self.swipe_to_up(1)
        self.swipe_to_up(1)
        self.myClick(self.find_element('设置', *self.SETTING_ID))
        self.myClick(self.find_element('常用语', *self.CYY_ID))
        self.myClick(self.find_element('添加常用语', *self.ADD_CYY_ID))
        self.input_info(self.find_element('常用语编辑', *self.EDIT_CYY_ID), 'Hello world!!!')
        sleep(1)
        self.myClick(self.find_element('保存', *self.SETTING_OK_ID))
        self.myClick(self.find_element('编辑所有常用语', *self.EDIT_ALL_CYY_ID))
        item_num = 0
        try:
            es = self.find_elements('所有常用语', *self.CYY_ITEM_ID)
            item_num = len(es[0])
            e = es[0][-1]
            sx, sy, ex, ey = self.get_bounds((e, '最后一个常用语'))
            x = int(sx / 2)
            y = int(sy + (ey - sy) / 2)
            # self.driver.tap([(x, y)])
            self.click(x, y)
            sleep(1)
        except:
            raise NoSuchElementException
        self.myClick(self.find_element('完成', *self.OVER_ID))
        item_num2 = len(self.find_elements('所有常用语', *self.CYY_ITEM_ID)[0])
        self.assertEqual(item_num, item_num2)

    @testcase
    def test_mtz_zhaq(self):
        '''萌团长_设置_账号安全'''
        self.enter_mtz()
        self.swipe_to_up(1)
        self.swipe_to_up(1)
        self.myClick(self.find_element('设置', *self.SETTING_ID))
        self.myClick(self.find_element('账号安全', *self.ZHAQ_ID))
        self.myClick(self.find_element('绑定手机号', *self.MOBILE_CHANGE_ID))
        self.assertTrue(self.wait_element2(self.CHANGE_BTN_ID))
        self.press_back()
        self.myClick(self.find_element('支付密码', *self.PAY_PWD_CHANGE_ID))
        self.assertTrue(self.wait_element2(self.PWD_FORGET_ID))

    @testcase
    def test_mtz_cleal_cache(self):
        '''萌团长_设置_清空缓存数据'''
        self.enter_mtz()
        self.swipe_to_up(1)
        self.swipe_to_up(1)
        self.myClick(self.find_element('设置', *self.SETTING_ID))
        self.myClick(self.find_element('进入清空缓存数据', *self.CLEAR_CACHE_ID))
        self.myClick(self.find_element('清空缓存数据', *self.COMFIRM_CLEAR_CACHE_ID))
        self.myClick(self.find_element('确定', *self.CLEAR_CACHE_OK_ID))

    @testcase
    def test_mtz_about_md(self):
        '''萌团长_设置_关于萌店'''
        self.enter_mtz()
        self.swipe_to_up(1)
        self.swipe_to_up(1)
        self.myClick(self.find_element('设置', *self.SETTING_ID))
        self.myClick(self.find_element('关于萌店', *self.GYMD_ID))
        self.myClick(self.find_element('功能介绍', *self.ABOUTUS_FUNC_ID))
        temp = 0

        self.swipe_to_left(4)
        e = self.wait_element2(self.LAUNCH_VIEWS_CLOSE_ID)
        if e:
            self.myClick((e, '关闭'))

        #建议反馈
        self.myClick(self.find_element('建议反馈', *self.ADVICE_ID))
        self.input_info(self.find_element('编辑框', *self.EDIT_ADVICE_ID), '1111 advice!')
        self.input_info(self.find_element('联系方式', *self.EDIT_CONTACT_ID), 'xzhacker@163.com')
        self.myClick(self.find_element('提交', *self.COMMIT_ID))
        self.myClick(self.find_element('提交', *self.COMFIRM_ID))

    @testcase
    def test_mtz_contact_cs(self):
        '''萌团长_设置_联系客服'''
        self.enter_mtz()
        self.swipe_to_up(1)
        self.myClick(self.find_element('设置', *self.SETTING_ID))
        self.swipe_to_up(1)
        self.myClick(self.find_element('联系客服', *self.BY_CCS_ID))
        dial_list = [self.BY_DIAL_INPUT_ID, self.BY_DIAL_INPUT_HUAWEI_ID]
        e = self.find_element_for_by_list("拨号盘", dial_list)
        self.assertTrue(e[0])

    @testcase
    def test_mtz_setting_logout(self):
        '''萌团长_设置_退出登录'''
        self.enter_mtz()
        self.swipe_to_up(1)
        self.swipe_to_up(1)
        self.myClick(self.find_element('设置', *self.SETTING_ID))
        self.swipe_to_up(1)
        self.myClick(self.find_element('退出登录', *self.BY_LOGOUT_ID))
        self.myClick(self.find_element('提交', *self.COMFIRM_ID))
        self.wait_element(self.find_element('菜单列表', *self.BY_MENU_ID))

if __name__ == '__main__':
    unittest.main()