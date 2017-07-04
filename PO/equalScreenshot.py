# -*- coding: utf8 -*-
__author__ = 'MR.wen'
import inspect
import sys
import time
import os
import unittest
reload(sys)
sys.setdefaultencoding('UTF-8')
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p))

class myequal(object):
    def __init__(self):
        pass

    def get_current_function_name(self):
        '''
        截图得到该case的方法名称
        :return: case方法名
        '''
        return inspect.stack()[1][3]
    #
    # def myscreenshot(self):
    #     '''
    #     使用adb自带的截图功能进行截图
    #     :param screensshot_name:截图名称
    #     :return:None
    #     '''
    #     try:
    #         now = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))
    #         day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    #         runpath = os.getcwd()
    #         imgpath = os.path.abspath(os.path.join(runpath, 'Result', day, "img"))
    #         self.dirname = imgpath
    #         os.popen("adb wait-for-device")
    #         os.popen("adb shell screencap -p /mnt/sdcard/tmp.png")
    #         if not os.path.isdir(self.dirname):
    #             os.makedirs(self.dirname)
    #         self.pic = now + ".png"
    #         # self.path = self.dirname + "\\" + self.pic
    #         self.path = os.path.join(self.dirname, self.pic)
    #         os.popen("adb pull /mnt/sdcard/tmp.png " + PATH(self.path))
    #         os.popen("adb shell rm /mnt/sdcard/tmp.png")
    #         print "Screenshot"
    #         print self.path
    #     except Exception as e:
    #         print e.message

    def myAssertEqual(self, first, second):
        '''
        assertEqual(a, b)     a == b
        :param screenshot_name 截图为当前方法名
        :param first:实际结果
        :param second:预期结果
        :return:None
        '''
        if isinstance(first, str):
            first = first.decode(encoding='utf-8')
        if isinstance(second, str):
            second = second.decode(encoding='utf-8')

        try:
            self.assertEqual(first, second)
        except AssertionError:
            self.myscreenshot()
            print 'assert error:'+str(second)+',screenshot path:'+self.path

            raise AssertionError, 'equal error!'

    def myAssertTrue(self, expr):
        '''
        :param expr:
        :return:
        '''
        try:
            self.assertTrue(expr)
        except AssertionError:
            self.myscreenshot()
            print 'assertTrue error: screenshot path:%s' %self.path
            raise AssertionError, 'equal error!'

    def myAssertNotEqual(self, first, second):
        '''
        assertNotEqual(a, b)     a != b
        :param screenshot_name 截图为当前方法名
        :param first:实际结果
        :param second:预期结果
        :return:None
        '''
        try:
            self.assertNotEqual(first, second)
        except AssertionError as e:
            print e.message
            self.myscreenshot()
            print 'assert error:'+str(second)+',screenshot path:'+self.path
            raise AssertionError,'equal error!'
