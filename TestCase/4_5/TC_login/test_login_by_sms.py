# -*- coding: utf8 -*-
import unittest

from PO.basePage import Base
from PO.warp import testcase


class Test_login_by_sms(Base):
    @testcase
    def test_sms(self):
        '''使用验证码登录并且退出登录'''
        self.myClick(self.find_uiautomator(self.get_mtz_name(), 'text'))
        self.boolean_login_state()
        self.login_by_sms(self.localReadConfig().getMobileInfo('mobile1'))
        self.swipe_to_down(2) #滑动屏幕防止myicon被遮住
        #sleep(2)
        self.myClick(self.find_element('个人中心',*self.iv_my_icon_id))
        self.assertEqual(self.find_element('个人中心title',*self.personal_info)[0].text.strip(), '个人信息')
        self.myClick(self.find_element('退出',*self.common_toplayout_left)) #从个人信息退出
        self.login_out()
        self.myClick(self.find_uiautomator(self.get_mtz_name(), 'text'))
        self.assertEqual(self.find_element('登录title',*self.login_title)[0].text.strip(), '登录')

    @testcase
    def test_sms_error(self):
        '''验证码输入错误'''
        self.myClick(self.find_uiautomator(self.get_mtz_name(), 'text'))
        self.boolean_login_state()
        self.login_by_sms(self.localReadConfig().getMobileInfo('mobile1'), type=1111)
        self.assertEqual(self.find_element('登录title',*self.login_title)[0].text.strip(), '登录')
if __name__ == '__main__':
    unittest.main()
