# -*- coding: utf8 -*-
import time
import os
from appium import webdriver
from PO import apkBase

__author__ = 'MR.wen'
import readConfig as readConfig
readConfigLocal = readConfig.ReadConfig()

class myDriver:
    '''
    封装myDriver，配置从config里面读取数据
    '''
    if 'nt' == os.name:
        path = readConfigLocal.getAppiumValue('appPathWin')
    elif 'posix' == os.name:
        path = readConfigLocal.getAppiumValue('appPathLinux')

    myInit = apkBase.ApkInfo(apkpath=r"%s" % path)
    platformName = readConfigLocal.getAppiumValue("platformName")
    platformVersion = readConfigLocal.getAppiumValue('platformVersion')
    appPackage = myInit.get_apk_pkg()
    appActivity = myInit.get_apk_activity()
    deviceName = readConfigLocal.getAppiumValue("devicesName")
    baseUrl = readConfigLocal.getAppiumValue("baseUrl")
    app = path
    desired_caps = {"platformName": platformName, "platformVersion": platformVersion, "appPackage": appPackage,
                    "appActivity": appActivity, "deviceName": deviceName, 'app': app, 'unicodeKeyboard': True,
                    'resetKeyboard': True, 'noReset': True}
    print desired_caps

    @staticmethod
    def get_driver():
        driver = webdriver.Remote(myDriver.baseUrl, myDriver.desired_caps)
        return driver
