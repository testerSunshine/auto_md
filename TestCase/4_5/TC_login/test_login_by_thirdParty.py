#coding=utf-8
from time import sleep

from PO.warp import testcase

__author__ = 'MR.wen'
import unittest
from PO.basePage import Base


class Test_login_by_thirdPart(Base):
    @testcase
    def test_long_by_qq(self):
        '''使用QQ登录'''
        self.myClick(self.find_uiautomator(self.get_mtz_name(), 'text'))
        self.boolean_login_state()
        self.login_by_thirdParty('qq')
        self.swipe_to_down(2)
        #sleep(2)#滑动屏幕防止myicon被遮住
        self.myClick(self.find_element('个人中心',*self.iv_my_icon_id))
        self.assertEqual(self.find_element('个人中心title',*self.personal_info)[0].text.strip(), '个人信息')
        self.myClick(self.find_element('退出',*self.common_toplayout_left)) #从个人信息退出
        self.login_out()

    @testcase
    def test_long_by_weixin(self):
        '''使用微信登录'''
        self.myClick(self.find_uiautomator(self.get_mtz_name(), 'text'))
        self.boolean_login_state()
        self.login_by_thirdParty('weixin')
        self.swipe_to_down(2) #滑动屏幕防止myicon被遮住
        #sleep(2)
        self.myClick(self.find_element('个人中心',*self.iv_my_icon_id))
        self.assertEqual(self.find_element('个人中心title',*self.personal_info)[0].text.strip(), '个人信息')
        self.myClick(self.find_element('退出',*self.common_toplayout_left)) #从个人信息退出
        self.login_out()

if __name__ == '__main__':
    unittest.main()