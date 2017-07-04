# -*- coding: utf8 -*-
import ConfigParser
import codecs
import os
__author__ = 'MR.wen'

prjDir = os.path.split(os.path.realpath(__file__))[0]
configfile_path = os.path.join(prjDir, os.pardir, "config.ini")
configfile_path = os.path.normpath(configfile_path)

class ReadConfig(object):
    def __init__(self):
        fd = open(configfile_path)
        data = fd.read()
        # remove BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(configfile_path, "w")
            file.write(data)
            file.close()
        fd.close()

        self.cf = ConfigParser.ConfigParser()
        self.cf.read(configfile_path)

    def getAppiumValue(self, name):
        '''
        appium参数
        :param name:将要获取的参数名称
        :return:
        '''
        value = self.cf.get("appium", name)
        return value

    def getCmdValue(self, name):
        '''
        cmd参数
        :param name:将要获取的参数名称
        :return:
        '''
        value = self.cf.get("cmd", name)
        return value

    def getMobileInfo(self, name):
        '''
        登录手机参数
        :return: 获取登录账号密码
        '''
        value = self.cf.get("mobile_info", name)
        return value