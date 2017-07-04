# -*- coding: utf8 -*-
from PO.warp import testcase

__author__ = 'MR.wen'

from PO.basePage import Base
import unittest


class Test_login_by_pwd(Base):
    @testcase
    def test_pwd(self):
        '''使用密码登录'''
        self.myClick(self.find_uiautomator(self.get_mtz_name(), 'text'))
        self.boolean_login_state()
        self.login_by_pwd(self.localReadConfig().getMobileInfo('mobile1'),
                          self.localReadConfig().getMobileInfo('pwd'))
        self.swipe_to_down(2) #滑动屏幕防止myicon被遮住
        self.myClick(self.find_element('个人中心',*self.iv_my_icon_id))
        self.assertEqual(self.find_element('个人中心title',*self.personal_info)[0].text.strip(), '个人信息')
        self.myClick(self.find_element('退出',*self.common_toplayout_left)) #从个人信息退出
        self.login_out()

    @testcase
    def test_pwd_null(self):
        '''登录密码错误'''
        self.myClick(self.find_uiautomator(self.get_mtz_name(), 'text'))
        self.boolean_login_state()
        self.login_by_pwd(self.localReadConfig().getMobileInfo('mobile1'),'12345666')
        self.assertEqual(self.find_element('登录title',*self.login_title)[0].text.strip(), '登录')

if __name__ == '__main__':
    unittest.main()
