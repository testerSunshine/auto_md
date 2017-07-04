# -*- coding: utf8 -*-
import threading

__author__ = 'MR.wen'
from urllib2 import URLError
from twisted.internet.error import ConnectionRefusedError
import sys, time, os
import unittest

from PO import devices_info
from public import HTMLTestRunner
from PO.appiumServer import myAppiumServer
from PO.installAPP import Ia
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append("public")
case_path = os.path.normpath("./TestCase/")
result = os.path.normpath('./Result/') #结果存放路径

class AllTest(object):
    def __init__(self):
        self.myServer = myAppiumServer()

    def Creatsuite(self):
        '''
        定义单元测试容器
        '''
        testunit = unittest.TestSuite()
        discover = unittest.defaultTestLoader.discover(case_path, pattern='test*.py', top_level_dir=None)
        # 将测试用例加入测试容器中
        for test_suite in discover:
            testunit.addTest(test_suite)
        return testunit

    def runCase(self):
        '''
        运行HTMLTestRunner
        '''
        now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
        day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        device_info = devices_info.get_all_device_info()
        # 定义个报告存放路径，支持相对路径。。。uu
        tdresult = os.path.join(result, day)
        if os.path.exists(tdresult):
            filename = os.path.join(tdresult, now + "_result.html")
            fp = file(filename, 'wb')
            # 定义测试报告
            runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'MD_android测试报告', description=u'用例执行情况：',
                                                   devices_info=device_info)
            # 运行测试用例
            runner.run(self.Creatsuite())
            fp.close()# 关闭报告文件
        else:
            os.makedirs(tdresult)
            # os.mkdir(tdresult+"\\image")
            filename = os.path.join(tdresult, now + "_result.html")
            fp = file(filename, 'wb')
            # 定义测试报告
            runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'MD_android测试报告', description=u'用例执行情况：',
                                                   devices_info=device_info)

            # 运行测试用例
            runner.run(self.Creatsuite())
            fp.close()  # 关闭报告文件

    def top_permissions(self):
        time.sleep(2)
        top = Ia('D:\\logs', '6f705b4d')
        top.tap_permissions()

    def run(self):
        try:
            # ia = Ia('D:\\logs', '6f705b4d')
            # ia.main()
            #获取系统当前时间
            self.myServer.start_server()
            time.sleep(5)
            if self.myServer.is_running():
                print 'appium is running'
                self.runCase()
            else:
                self.myServer.re_start_server()
                if self.myServer.is_running():
                    print 'appium is running'
                    self.runCase()
        except Exception as e:
            print e.message
        finally:
            try:
                self.myServer.stop_server()
            except URLError as e:
                print e.message
            except ConnectionRefusedError as e:
                print e.message
            except KeyError as e:
                print e.message

if __name__ == '__main__':
    ojb = AllTest()
    ojb.run()