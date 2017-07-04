# -*- coding: utf8 -*-
from functools import wraps
from selenium.common.exceptions import NoSuchElementException
from myExceptions.myException import MyException
import performance
from time import sleep
from PO.utils import GetMyLog
from myExceptions.myException import MyAssertionError
import time
import os

from selenium.webdriver import *
import inspect
import sys
logger = GetMyLog.myLog()
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p))
UI_OPTIONS = {'myClick': '点击',
                'mySend_keys': '输入',
                'swipe_to_up': '滑动向上次数',
                'swipe_to_down': '滑动向下次数',
                'swipe_to_left': '滑动向左次数',
                'swipe_to_right': '滑动向右次数',
                'find_elements': '查找元素组',
                'find_element': '查找元素',
                'find_element_by_accessibility_id': '查找元素[desc]',
                'sysback': '返回上个页面成功',
                'press_back': '按软键盘返回',
                'press_back_by_keycode': '按硬件返回',
                'wait_element': '等待元素1',
                'wait_element2': '等待元素2',
                'mySend_keys': '输入字符串',
                'mySend_keys2': '输入字符串2',
                'find_uiautomator': '按uia查找元素',
                'find_element_for_by_list': '按by_list查找元素',
                'find_elements_for_by_list': '按by_list查找元素组',
                'find_element_for_bounds': '按指定边界查找元素',
                'find_elements_for_bounds': '按指定边界查找元素组',
                'swipe_to_down_find_element': '自上而下划查找元素',
                'swipe_to_up_find_element': '自下而上划查找元素',
                'swipe_to_up_find_element_by_accessibility_id': '自下而上划按desc查找元素',
                'click': '点击坐标'
               }

flag = '_IMAGE'
def _screenshot():
    now = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))
    day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    runpath = os.getcwd()
    if 'TestCase' in runpath:
        runpath = os.path.join(runpath, os.pardir,os.pardir,os.pardir)
    imgpath = os.path.abspath(os.path.join(runpath, 'Result', day, "img"))
    dirname = imgpath
    os.popen("adb wait-for-device")
    os.popen("adb shell screencap -p /mnt/sdcard/tmp.png")
    if not os.path.isdir(dirname):
        os.makedirs(dirname)
    pic = now + ".png"

    pic_path = os.path.join(dirname, pic)
    os.popen("adb pull /mnt/sdcard/tmp.png " + PATH(pic_path))
    os.popen("adb shell rm /mnt/sdcard/tmp.png")
    return pic_path

def testcase(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
            performance.get_cpu_men()
            logger.info('[%s]执行成功\n' % func.__name__)
            sleep(1)
        except NoSuchElementException as e:
            performance.get_cpu_men()
            logger.info('[%s]执行失败:%s\n' % (func.__name__, e.msg))
            raise NoSuchElementException(msg=flag + _screenshot())
        except AssertionError as e:
            performance.get_cpu_men()
            logger.info('[%s]执行失败:%s\n' % (func.__name__, e.message))
            raise MyAssertionError(msg=flag + _screenshot())
        except Exception as e:
            performance.get_cpu_men()
            if isinstance(e, MyException):
                logger.info('[%s]执行失败:%s\n' % (func.__name__, e.msg))
            else:
                logger.info('[%s]执行失败:\n' % func.__name__)
            raise MyException(msg=flag + _screenshot())
    return wrapper

def wp_write_cpu_men(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        cpu, men = performance.write_cpu_men()
        if isinstance(res, tuple) and (res[0] is False or res[0] is []):
            logger.info('[%s][%s]失败\t当前性能情况 cpu:%s men:%s' % (UI_OPTIONS.get(func.__name__), res[1], cpu, men))
            sleep(1)
            return res
        elif res is False:
            logger.info('[%s]失败\t当前性能情况 cpu:%s men:%s' % (UI_OPTIONS.get(func.__name__), cpu, men))
            sleep(1)
            return res
        else:
            if isinstance(res, str) or isinstance(res, unicode):
                logger.info('[%s][%s]成功\t当前性能情况 cpu:%s men:%s' % (UI_OPTIONS.get(func.__name__), res, cpu, men))
            elif isinstance(res, tuple):
                logger.info('[%s][%s]成功\t当前性能情况 cpu:%s men:%s' % (UI_OPTIONS.get(func.__name__), res[1], cpu, men))
            elif isinstance(res, int):
                logger.info('[%s][%d]成功\t当前性能情况 cpu:%s men:%s' % (UI_OPTIONS.get(func.__name__), res, cpu, men))
            else:
                logger.info('[%s]成功\t当前性能情况 cpu:%s men:%s' % (UI_OPTIONS.get(func.__name__), cpu, men))
            sleep(1)
            return res

        # try:
        #     # res = '$$$'
        #     res = func(*args, **kwargs)
        #     cpu, men = performance.write_cpu_men()
        #     if isinstance(res, tuple) and (res[0] is False or res[0] is []):
        #         logger.info( '[%s][%s]失败\t当前性能情况 cpu:%s men:%s' % (res[1], cpu, men))
        #         sleep(2)
        #     elif res is False:
        #         logger.info( '[%s]失败\t当前性能情况 cpu:%s men:%s' % (cpu, men))
        #         sleep(2)
        #     else:
        #         if isinstance(res, tuple):
        #             logger.info( '[%s][%s]成功\t当前性能情况 cpu:%s men:%s' % (res[1], cpu, men))
        #             sleep(2)
        #         else:
        #             logger.info( '[%s]成功\t当前性能情况 cpu:%s men:%s' % (cpu, men))
        #             sleep(2)
        # except NoSuchElementException as e:
        #     cpu, men = performance.write_cpu_men()
        #     logger.info( '[%s][%s]失败\t当前性能情况 cpu:%s men:%s' % (e.msg, cpu, men))
        #     sleep(2)
        #     raise NoSuchElementException
        # except Exception as e:
        #     cpu, men = performance.write_cpu_men()
        #     # logger.info( '[%s][%s]失败\t当前性能情况 cpu:%s men:%s' % (e.msg, cpu, men))
        #     logger.info( '[%s]失败\t当前性能情况 cpu:%s men:%s' % (cpu, men))
        #     sleep(2)
        #     raise RuntimeError
    return wrapper
