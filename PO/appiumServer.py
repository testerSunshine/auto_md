# -*- coding: utf8 -*-
import os
import platform
import threading
import urllib2
from multiprocessing import Process
from time import sleep
from urllib2 import URLError
from PO.apkBase import ApkInfo
import readConfig as readConfig
from PO.installAPP import Ia

readConfigLocal = readConfig.ReadConfig()


class RunServer(threading.Thread):

    def __init__(self, cmd):
        threading.Thread.__init__(self)
        self.cmd = cmd

    def run(self):
        os.system(self.cmd)
class myAppiumServer:
    def __init__(self):
        global openAppium, baseUrl
        if os.name == 'posix':
            openAppium = readConfigLocal.getCmdValue("openAppiumLinux")
            self.ApkInfo = ApkInfo(readConfigLocal.getAppiumValue('appPathLinux'))
        elif os.name == 'nt':
            openAppium = readConfigLocal.getCmdValue("openAppiumWin")
            self.ApkInfo = ApkInfo(readConfigLocal.getAppiumValue('appPathWin'))
        baseUrl = readConfigLocal.getAppiumValue("baseUrl")

    def top_permissions(self):
            sleep(2)
            top = Ia('D:\\logs', '6f705b4d')
            top.tap_permissions()

    def run_server(self):
        os.system(openAppium)

    def start_server(self):
        '''
        start appium server
        :return:None
        '''

        threads = []
        start_server1 = threading.Thread(target=self.run_server, args=())
        threads.append(start_server1)
        process_list = range(len(threads))
        for i in process_list:
            threads[i].start()

    def stop_server(self):
        """stop the appium server and uninstall app
        :return:None
        """
        system = platform.system()
        if system is 'Windows':
            os.popen('taskkill /f /im  node.exe')
        else:
            os.popen('pkill node')

    def is_running(self):
        """Determine whether server is running
        :return:True or False
        """
        response = None
        url = baseUrl + "/status"
        try:
            response = urllib2.urlopen(url, timeout=5)
            if response.code == 200:
                return True
            else:
                return False
        except URLError:
            return False
        finally:
            if response:
                response.close()

    def re_start_server(self):
        """reStart the appium server
        """
        self.stop_server()
        self.start_server()

# if __name__ == "__main__":
#     a = myAppiumServer()
#     a.start_server()


