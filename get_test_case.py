# -*- coding: utf8 -*-
import threading
import time,datetime
import re
from multiprocessing import Process
__author__ = 'ALEX.XU'

import sys, time, os
from pprint import pprint
import unittest
from public import HTMLTestRunner
from PO.appiumServer import myAppiumServer
from PO.installAPP import Ia
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append("public")
case_path = ".\\TestCase\\"
result = '.\\Result\\' #结果存放路径
class CaseSet(object):
    def __init__(self, case_set_name, cnum, cname_list):
        self.case_set_name = case_set_name
        self.cnum = 0
        self.cname_list = []

class CaseLoader(object):
    def __init__(self):
        pass

    def seach(self, path, file_list):
        listdir = [f for f in os.listdir(path)]
        # print("当前目录:"+path)
        # print(listdir)

        for file in listdir:
            # 保存文件名字
            file_name = file
            file = os.path.join(path, file)
            if os.path.isdir(file):
                self.seach(file, file_list)
            # elif os.path.isfile(file) and "aplog_" in file_name:
            elif os.path.isfile(file) and file_name.startswith('test_') and file_name.endswith('.py'):
                file_list.append(file)
                # print("当前文件:" + file)
                #         else:
                # #aplog_JAVACRASH_20160715111521
                # #aplog_TOMBSTONE_20160713195128
                # #aplog_ANR_20160714162038 []
                #             print("当前文件:"+file)

    def find_case(self, casepath):
        case_set_name = casepath.split('\\')[-1].split('.')[0]
        case_num = 0
        case_name = []

        re1 = re.compile(r'# def (test[0-9a-zA-Z\_]+)')
        with open(casepath, 'r') as f:
            for line in f.readlines():
                res = re.findall(re1, line)
                if res:
                    case_name.append(res[0])
                    case_num += 1
        return {case_set_name: [case_num, case_name]}

    def find_all_case(self, case_list):
        return map(self.find_case, case_list)
def main():
    starttime = datetime.datetime.now()
    cpath = os.path.join(os.getcwd(), "TestCase")
    # print("当前根目录:"+cpath)
    file_list = []
    caseLoad = CaseLoader()
    caseLoad.seach(cpath, file_list)
    # a = caseLoad.find_case('F:\\appium\\TestCase\\4_5\\TC_login\\test_login_by_pwd.py')
    print file_list
    print(len(file_list))
    # print a
    all_case = caseLoad.find_all_case(file_list)
    case_account = 0
    for case in all_case:
        for k,v in case.items():
            print k,v
            case_account += v[0]
    print "case总数为:%d" %case_account
    endtime = datetime.datetime.now()
    print"Finish work:%s" % (datetime.datetime.strftime(endtime, '%Y-%m-%d %H:%M:%S'))
    print'Run time :%ss' % ((endtime - starttime).seconds)

if __name__ == '__main__':
    main()