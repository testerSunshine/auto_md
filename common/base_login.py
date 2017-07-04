# -*- coding: utf8 -*-
from selenium.common.exceptions import NoSuchElementException

from PO import apkBase

__author__ = 'MR.wen'
from time import sleep
from selenium.webdriver.common.by import By
from PO.dashPage import AppUI
from PO.mdInterface import MD_inteface as GetInterface
from PO.readConfig import ReadConfig

class Login(AppUI):
    #----引导页面数据----
    closeBtn = (By.ID,'launch_views_close')
    guideView = (By.ID,'launch_views_page_indicator')
    tiyanBtn = (By.ID,'launch_item_next')

    #----首页弹窗数据----
    syDailog = (By.ID, 'dialogLinLay')
    syDailog_quan = (By.ID, 'com.hs.yjseller:id / iv_teach_layout_content')
    syCloseBtn = (By.ID, 'com.hs.yjseller:id/iv_remind_close') #首页弹窗关闭标签
    mobileEdit = (By.ID, 'speedy_register_phone_edittext')
    moblileReceive = (By.ID, 'speedy_register_phone_button')
    confirmBtn = (By.ID, 'button2')
    ReGetBtn = (By.ID, 'get_valid_sms')

    #----登录页数据----
    login_title = (By.ID, 'titleTxtView')
    kaidianBtn = (By.ID, 'main_text_earn')
    msgBtn = (By.ID, 'main_text_message')
    myBtn = (By.XPATH, '//android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout[4]')   #萌团长
    # myBtn = (By.XPATH, '//android.widget.RelativeLayout[1]/android.widget.LinearLayout//android.widget.TextView[4]')  # 萌团长
    logPhone = (By.ID,'login_phone')
    logPwd = (By.ID,'login_password')
    getsms = (By.ID,'get_valid_sms')
    querenBtn = (By.ID,'button2')
    sendsms = (By.ID,'valid_number')
    login_commit = (By.ID,'login_commit')
    log_by_psd = (By.ID,'login_by_psd')
    login_tel = (By.ID,'login_tel')
    login_password = (By.ID,'login_password')
    login_by_QQ = (By.ID,'entry_by_qq')
    login_by_wechat = (By.ID,'entry_by_wechat')
    login_by_sina = (By.ID,'entry_by_sina')

    # ----萌团长页数据----
    common_toplayout_left = (By.ID,'common_toplayout_left')
    iv_my_setting = (By.ID,'iv_my_setting')
    login_exit = (By.ID,'tv_account_exit')
    personal_info = (By.ID, 'common_toplayout_title')
    iv_my_icon_id = (By.ID, 'iv_my_icon')
    pending_pay_id = (By.ID, 'com.hs.yjseller:id/tv_pending_pay')

    def click_permission(self,times):
        '''
        点击系统权限
        :param times:等待多少秒
        :return:
        '''
        for i in range(times): #等待15S出现的权限内容框
            sleep(1)
            if self.find_uiautomator('允许', 'text'):
                self.find_uiautomator('允许', 'text').click()
            else:
                break

    def swipeGuideView(self):
        '''
        滑动引导并点击'立即体验'
        :return:None
        '''
        if self.find_element('引导图关闭',*self.closeBtn):
            self.swipe_to_right(4)
            self.myClick(self.find_element('点击引导图关闭',*self.tiyanBtn), is_screenshot=False)
        else:
            pass

    def start_app(self):
        '''
        判断app启动时候是否有特殊元素可点击，如果有则点击
        :return:None
        '''
        temp = 0
        while temp<3:
            if self.wait_element2(self.myBtn, is_screenshot = False, times=2):  # 首先判断是否出现萌团长按钮
                temp += 2
            if self.wait_element2(self.syDailog, is_screenshot=False, times=2) or self.wait_element2(self.syDailog_quan, is_screenshot=False, times=2):  # 然后判断是否出现首页弹窗，出现则点击
                temp += 1
                self.myClick((self.wait_element2(self.syCloseBtn, is_screenshot = False, times=2), '关闭按钮'))
            elif self.wait_element2(self.closeBtn):  # 判断是否出现滑动引导图
                temp += 1
                self.myClick((self.wait_element2(self.closeBtn, is_screenshot = False, times=2), '首页滑动图点击'))
                self.myClick((self.wait_element2(self.syCloseBtn, is_screenshot = False, times=2), '首页滑动图'))
            temp += 1

    def swipe_by_adb(self,swipe=1):
        '''调用adb滑动'''
        ADB = apkBase.ADB()
        if swipe==1:
            ADB.swipe_to_up()
        if swipe==2:
            ADB.swipe_to_down()

    def get_mtz_name(self):
        return '萌团长'

    def login_by_sms(self, phone, type=0):
        '''
        通过短信验证码登录
        :param phone:手机号码
        :param type: 默认为1
        :return:
        '''
        self.myClick(self.find_element('手机号',*self.logPhone))
        while True:
            self.myKeyEvent(phone)
            if self.find_element('手机号',*self.logPhone)[0].text.replace(' ', '') == phone:
                break
            self.find_element('手机号',*self.logPhone)[0].clear()
        self.myClick(self.find_element('短信', *self.getsms))
        self.myClick(self.find_element('确认', *self.querenBtn))
        if type == 0:
            #默认使用验证码正确登录
            code = GetInterface.getLoginCode(phone)
            sleep(3)
            self.mySend_keys(self.find_element('验证码',*self.sendsms)[0], code)
        else:
            #测试验证码输入错误的情况下使用
            self.mySend_keys(self.find_element('验证码',*self.sendsms)[0], type)
        self.myClick(self.find_element('提交',*self.login_commit))

    def login_by_pwd(self,phone,pwd):
        '''
        通过手机密码登录
        :param phone:手机号码
        :param pwd: 手机密码
        :return:
        '''
        self.myClick(self.find_element('密码登录',*self.log_by_psd))
        self.myClick(self.find_element('手机',*self.login_tel))

        while True:
            self.myKeyEvent(phone)
            if self.find_element('手机',*self.login_tel)[0].text.replace(' ', '') == phone:
                break
            self.find_element('手机',*self.login_tel)[0].clear()

        self.mySend_keys(self.find_element('密码',*self.login_password)[0], pwd)
        self.myClick(self.find_element('提交',*self.login_commit))

    def login_by_thirdParty(self,login_type):
        '''
        使用第三方登录
        :param login_type:第三方登录类型
        '''
        if login_type == 'QQ' or login_type =='qq':
            self.myClick(self.find_element('qq登录', *self.login_by_QQ))
            self.wait(30)
            text = "登录"
            try:
                self.myClick(self.find_uiautomator(text, 'text'))
            except:
                pass
        elif login_type =='微博' or login_type =='weibo':
            self.myClick(self.find_element('微博',*self.login_by_sina))
            self.wait(30)
            text = "确定"
            try:
                self.find_uiautomator(text,'text').click()
            except:
                pass
        elif login_type =='微信' or login_type =='weixin':
            self.myClick(self.find_element('微信',*self.login_by_wechat))
            sleep(10)
            size = self.get_size()
            self.driver.tap([(size.get('width')*0.5,size.get('height')*0.66)])
            self.wait(5)
        else:
            print '类型错误...'

    def boolean_login_state(self):
        '''判断登录状态'''
        if self.find_element('登录首页',*self.login_title)[0]:
            print '未登录...'
            return True
        elif self.find_uiautomator(self.get_mtz_name(), 'text'):
            print '已登录，正在尝试退出...'
            self.login_out()
            self.myClick(self.find_uiautomator(self.get_mtz_name(), 'text'))
        else:
            print '啥都没找到...'

    def login_out(self):
        self.myClick(self.find_uiautomator(self.get_mtz_name(), 'text'))
        self.swipe_to_up(2)
        self.myClick(self.find_element('设置',*self.iv_my_setting))
        self.swipe_to_up(2)
        self.myClick(self.find_element('退出',*self.login_exit))
        self.myClick(self.find_element('确认',*self.querenBtn))

    def localReadConfig(self):
        localReadConfig = ReadConfig()
        return localReadConfig
