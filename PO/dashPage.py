# -*- coding: utf8 -*-
__author__ = 'MR.wen'

from PO import performance
from PO.warp import wp_write_cpu_men
from PO.apkBase import ADB

import os
import time
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from PIL import Image
from selenium.webdriver.support.wait import WebDriverWait

from PO.utils import GetMyLog
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p))
now = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))
day = time.strftime('%Y-%m-%d', time.localtime(time.time()))

class A():
    pass

BY_BACK_ID = (By.ID, 'com.hs.yjseller:id/backBtn')
BY_BACK_ID2 = (By.ID, 'com.hs.yjseller:id/common_toplayout_left')

class Dash():
    def __init__(self, driver):
        self.driver = driver

    def __str__(self):
        return 'webDdriver'

    @wp_write_cpu_men
    def find_element(self, ename, *loc):
        """
        定位元素,定位正确后返回元素的信息,外部调用传入元组参数必须有*,
        例如:
        find_element(*self.XXXX)
        如果请求超时，调用截图方法
        :param loc: 元组类型,结构必须是(By.NAME, u'XXXX')
        :return: element,ename
        """
        element = False
        try:
            element = WebDriverWait(self.driver, 15).until(lambda driver: driver.find_element(*loc))
        except:
            return element, ename
        e = element, ename

        # window_size = self.get_size()
        # bound_h = (0, window_size['height'])

        adb = ADB()
        height = adb.get_screen_resolution()[1]
        bound_h = (0, height)

        try:
            bh = map(int, self.get_bounds(e)[1::2])
            # print bh[0], bh[1], bh[0], bound_h[0], bh[1], bound_h[1]
            if (bh[0] <= bh[1]) and (bh[0] >= bound_h[0]) and (bh[1] <= bound_h[1]):
                return e
            else:
                return False, ename
        except:
            return False, ename

    @wp_write_cpu_men
    def find_elements(self, enames, *loc):
        '''
        定位元素组,定位正确后返回元素的信息,外部调用传入元组参数必须有*,
        例如:
        :param enames:
        :param loc:
        :return:
        '''
        try:
            e = WebDriverWait(self.driver, 15).until(lambda driver: driver.find_elements(*loc))
            return e, enames
        except:
            return False, enames

    @wp_write_cpu_men
    def find_element_by_accessibility_id(self, ename, id, time = 15):
        try:
            # e = self.driver.find_element(by=MobileBy.ACCESSIBILITY_ID, value=id)
            e = WebDriverWait(self.driver, time).until(
                lambda driver: driver.find_element(by=MobileBy.ACCESSIBILITY_ID, value=id))
            e = e, ename
            window_size = self.get_size()
            bound_h = (0, window_size['height'])
            bh = map(int, self.get_bounds(e)[1::2])
            if (bh[0] < bh[1]) and (bh[0] > bound_h[0]) and (bh[1] < bound_h[1]):
                return e
            else:
                return False, ename
        except:
            return False, ename

    @wp_write_cpu_men
    def mySend_keys(self, loc, value, is_screenshot=True):
        '''
        封装自带输入方法
        :param loc: 传入的值
        :param value:
        :param clear_first:
        :param click_first:
        :return:
        '''
        if loc:
            loc.send_keys(value)
            return value
        else:
            raise NoSuchElementException(msg=value)

    @wp_write_cpu_men
    def myClick(self, element, is_screenshot=True):
        '''
        :param element:元素
        :param is_screenshot:元素默认存在
        :return:
        '''
        if element[0]:
            element[0].click()
            return element[1]
        else:
            if is_screenshot:
                raise NoSuchElementException(msg=element[1])

    @wp_write_cpu_men
    def find_uiautomator(self, type, by, wait_time=10, is_screenshot=True):
        '''
        使用uiautomator定位
        :param type:
        :param by:
        :param is_screenshot:
        :return:
        '''
        if by == 'text':
            u_element = WebDriverWait(self.driver, wait_time).until(lambda driver: driver.find_element_by_android_uiautomator("new UiSelector().text(\"%s\")" % type))
            if u_element:
                return u_element, type
            else:
                return False, type

    def wait(self, time):
        self.driver.implicitly_wait(time)

    @wp_write_cpu_men
    def sysback(self):
        """
        系统的返回按钮
        :return: None
        """
        self.driver.keyevent(4)

    def get_size(self):
        """
        获取当前屏幕的分辨率
        :return: int, x*y
        """
        size = self.driver.get_window_size()
        return size

    @wp_write_cpu_men
    def swipe_to_up(self, number):
        """
        从下往上滑动
        :param number:滑动次数
        :return: None
        """
        for i in range(number):
            sleep(1)
            window_size = self.get_size()
            width = window_size.get("width")
            height = window_size.get("height")
            self.driver.swipe(width / 2, height * 2 / 3, width / 2, height / 4, 600)
            sleep(2)
        return number

    @wp_write_cpu_men
    def swipe_to_down(self, number):
        """
        从上往下滑动
        :param number:滑动次数
        :return: None
        """
        for i in range(number):
            window_size = self.get_size()
            width = window_size.get("width")
            height = window_size.get("height")
            self.driver.swipe(width / 2, height / 3, width / 2, height * 3 / 4, 600)
            sleep(2)
        return number

    @wp_write_cpu_men
    def swipe_to_right(self, number):
        '''
        从右往左滑动
        :param number:滑动次数
        :return: None
        '''
        for i in range(number):
            sleep(1)
            window_size = self.get_size()
            print window_size
            width = window_size.get("width")
            height = window_size.get("height")
            self.driver.swipe(width / 4, height / 2, width * 3 / 4, height / 2, 600)
            # sleep(1)
        return number

    @wp_write_cpu_men
    def swipe_to_left(self, number, location = None):
        """
        从右往左滑动
        :param number:滑动次数
        :return: None
        """
        if location == None:
            for i in range(number):
                window_size = self.get_size()
                sleep(1)
                width = window_size.get("width")
                height = window_size.get("height")
                self.driver.swipe(width * 4 / 5, height / 2, width / 5, height / 2, 600)
            return number
        else:
            for i in range(number):
                self.driver.swipe(location[1], location[2], location[0], location[2], 600)
            return number

    def getLocation(self, element):
        """
        获取元素的定位信息,外部调用传入元组参数必须有*,
        例如:
        (*self.native_caixun)
        :param loc: 元素的定位方式
        :return: list, [x, y]
        """
        locaX = element[0].location.get('x')
        locaY = element[0].location.get('y')
        rst = (locaX, locaY)
        return rst

    def reLoadApp(self):
        """
        重启app
        :return:None
        """
        self.driver.close_app()
        self.driver.launch_app()

    def trans(self, str):
        '''
        转义字符串
        '''
        key = {'0': '7', '1': '8', '2': '9', '3': '10', '4': '11', '5': '12', '6': '13', '7': '14', '8': '15', '9': '16',
               'A': '29', 'B': '30', 'C': '31', 'D': '32', 'E': '33', 'F': '34', 'G': '35', 'H': '36', 'I': '37',
               'J': '38', 'K': '39', 'L': '40', 'M': '41', 'N': '42', 'O': '43', 'P': '44','Q': '45', 'R': '46',
               'S': '47', 'T': '48', 'U': '49', 'V': '50', 'W': '51', 'X': '52','Y': '53', 'Z': '54'}
        self.driver.keyevent(key[str])
        sleep(0.5)

    def myKeyEvent(self,number):
        '''
        调用手机号数据字符串
        :param number:
        :return:需要调用小键盘的字符串，目前只支持1234567890
        '''
        map(self.trans,number)
        sleep(1)

    def screenshot_rect(self, file_path, bounds):
        self.driver.save_screenshot(file_path)
        sleep(1)
        image = Image.open(file_path)
        return image.crop(bounds)

    @wp_write_cpu_men
    def press_back(self):
        sleep(1)
        BY_BACK_IDS = [BY_BACK_ID, BY_BACK_ID2]
        e = self.find_element_for_by_list('返回', BY_BACK_IDS)
        self.myClick(e)

    @wp_write_cpu_men
    def press_back_by_keycode(self):
        sleep(2)
        self.driver.press_keycode(4)  # 按返回键
        sleep(1)

    def image_max_pix_rate(self, image):
        '''
        获取图片像素值最多的所占比率
        :param image:
        :return:
        '''
        image = image.convert('L')
        x, y = image.size
        colors = image.getcolors()
        i_max = max([i[0] for i in colors])
        return i_max / float(x * y)
        # return {i[1]: i[0] for i in colors}[rgb] / float(x * y)

    def check_image(img, rate=1.0):
        w, h = img.size
        img = img.thumbnail((int(w / rate), int(h / rate)))
        # self.image_max_pix_rate(img)

    def get_element_size(self, element):
        '''
        得到元素长宽
        :param element:
        :return:
        '''
        return (element[0].size['width'], element[0].size['height'])

    def get_bounds(self, element):
        '''
        得到元素左上角,和右下角坐标
        :param element:
        :return:
        '''
        if not element[0]:
            raise NoSuchElementException
        rect = self.getLocation(element)
        size = self.get_element_size(element)
        end_x = int(rect[0] + size[0])
        end_y = int(rect[1] + size[1])
        return rect[0], rect[1], end_x, end_y

    @wp_write_cpu_men
    def wait_element(self, element, is_screenshot = True, times = 15):
        '''
        等待某个元素出现
        :param element:
        :param times:
        :return:
        '''
        while 0 < times:
            if element[0]:
                return
            sleep(1)
            times -= 1
        if is_screenshot:
            raise NoSuchElementException

    @wp_write_cpu_men
    def wait_element2(self, by, is_screenshot = True, times = 3):
        '''
        等待某个元素出现
        :param element:
        :param times:
        :return:
        '''
        while 0 < times:
            try:
                e = self.driver.find_element(*by)
                return e
            except:
                sleep(1)
            times -= 1
        if is_screenshot:
            return False
        # else:
        #     raise NoSuchElementException

    def compare_by_name(self, name1, name2):
        '''
        text文件校验
        :param name1:
        :param name2:
        :return:
        '''
        try:
            name1 = name1.split("[goodsIcon]")[1]
        except:
            pass
        s1 = name1.replace(' ', '')
        s2 = name2.replace(' ', '')
        if (s1 in s2) or (s2 in s1):
            return True
        else:
            return False

    def get_x_y(self, img):
        img = img.convert('L')
        img = img.transpose(Image.ROTATE_270)
        i_x, i_y = -1, -1
        y, x = img.size
        print x, y
        for i in range(x):
            temp = True
            prec = -1
            for j in range(y):
                if prec == -1:
                    prec = img.getpixel((j, i))
                elif prec != img.getpixel((j, i)):
                    i_x = i
                    break
                temp = False
            if temp:
                break

        for i in range(x - 1, 0, -1):
            temp = True
            prec = -1
            for j in range(y):
                if prec == -1:
                    prec = img.getpixel((j, i))
                elif prec != img.getpixel((j, i)):
                    i_y = i
                    break
                temp = False
            if temp:
                break
        return i_x, i_y

    def get_min_dif(nums):
        '''
        # 获取一组数最小差值
        :return:
        '''
        nums.sort()
        t = nums[-1]
        for i in range(len(nums) - 1):
            temp = nums[i + 1] - nums[i]
            if temp < t:
                t = temp
        return t

    @wp_write_cpu_men
    def myTap(self,a):
        self.driver.tap(a)
    @wp_write_cpu_men
    def mySend_keys2(self, loc, value, is_screenshot=True):
        temp = 0
        while loc:
            loc.send_keys(value)
            sleep(2)
            if loc.text == value:
                return value
            temp += 1
            if temp >= 10:
                raise Exception(msg='输入超过10次') #次数
        else:
            if is_screenshot:
                raise NoSuchElementException(msg=value)

    def input_info(self, element, info):
        # print element[0].text
        self.myClick(element)
        temp = 0
        while True:
            self.mySend_keys(element[0], info)
            # print element[0].text
            if element[0].text.replace(' ', '') == info.replace(' ', ''):
                break
            element[0].clear()

    @wp_write_cpu_men
    def find_element_for_by_list(self, ename, loc_list, bound_h=0):
        if bound_h == 0:
            bound_h = (0, self.get_size()['height'])
        for i in range(2):  #循环找2次
            for loc in loc_list:
                try:
                    es = self.driver.find_elements(*loc)
                    sleep(2)
                    for e in es:
                        bh = map(int, self.get_bounds((e, ename))[1::2])
                        if (bh[0] < bh[1]) and (bh[0] > bound_h[0]) and (bh[1] < bound_h[1]):
                            return e, ename
                except:
                    pass
        return False, ename

    @wp_write_cpu_men
    def find_elements_for_by_list(self, ename, loc_list, bound_h=0):
        if bound_h == 0:
            bound_h = (0, self.get_size()['height'])
        elist = []
        for loc in loc_list:
            try:
                e = self.driver.find_element(*loc)
                sleep(2)

                bh = map(int, self.get_bounds((e, ename))[1::2])
                if (bh[0] < bh[1]) and (bh[0] > bound_h[0]) and (bh[1] < bound_h[1]):
                    elist.append(e)
            except:
                pass
        return elist, ename

    @wp_write_cpu_men
    def find_element_for_bounds(self, ename, bound_h, *loc):
        '''
        获取当前屏幕范围指定元素
        :param ename: 元素组名字
        :param bound_h: 屏幕高度返回(0,screen_h)
        :param loc:
        :return:
        '''
        if bound_h == 0:
            bound_h = (0, self.get_size()['height'])
        try:
            es = WebDriverWait(self.driver, 15).until(lambda driver: driver.find_elements(*loc))
            for e in es:
                bh = map(int, self.get_bounds((e, ename))[1::2])
                # if (bh[0] < bh[1]) and (bh[0] > bound_h[0]) and (bh[1] < bound_h[1]) and ename == e.get_attribute('name'):
                if (bh[0] < bh[1]) and (bh[0] > bound_h[0]) and (bh[1] < bound_h[1]):
                    return e, ename
        except:
            return False, ename

    @wp_write_cpu_men
    def find_elements_for_bounds(self, enames, bound_h, *loc):
        '''
        获取当前屏幕范围指定元素
        :param enames: 元素组名字
        :param bound_h: 屏幕高度返回(0,screen_h)
        :param loc:
        :return:
        '''
        if bound_h == 0:
            bound_h = (0, self.get_size()['height'])
        my_es = []
        try:
            es = WebDriverWait(self.driver, 15).until(lambda driver: driver.find_elements(*loc))
            for e in es:
                bh = map(int, self.get_bounds((e, enames))[1::2])
                if (bh[0] < bh[1]) and (bh[0] > bound_h[0]) and (bh[1] < bound_h[1]):
                    # print str(bh), "in", str((bound_h[0], bound_h[1]))
                    my_es.append((e, e.get_attribute('name')))
            if my_es == []:
                return False, enames
            else:
                return my_es
        except:
            return False, enames

    @wp_write_cpu_men
    def swipe_to_down_find_element(self, ename, *loc):
        temp = 0
        while temp < 5:
            try:
                e = self.driver.find_element(*loc)
                return e, ename
            except:
                pass
            self.swipe_to_down(1)
            temp += 1
        return False, ename

    @wp_write_cpu_men
    def swipe_to_up_find_element(self, ename, *loc):
        temp = 0
        while temp < 5:
            try:
                e = self.find_element_for_bounds(ename, 0, *loc)
                if e[0]:
                    return e
            except:
                pass
            self.swipe_to_up(1)
            temp += 1
        return False, ename

    @wp_write_cpu_men
    def swipe_to_up_find_element_by_accessibility_id(self, ename, loc, time = 5):
        temp = 0
        while temp < 5:
            e = self.find_element_by_accessibility_id(ename, loc, time)
            if e[0]:
                return e
            self.swipe_to_up(1)
            temp += 1
        return False, ename

    @wp_write_cpu_men
    def click(self, x, y):
        self.driver.tap([(x, y)])  # 点击x,y
        return '%d,%d' % (x, y)

    def swipe_to_left_del_item(self, e):
        x0, y0, x1, y1 = self.get_bounds((e))
        self.swipe_to_left(1, location=(x0, x1, y1))
        self.click(x1, y1)

class WebUI(Dash):
	def __str__(self):
		return 'WEB UI'

class AppUI(Dash):
	def __str__(self):
		return 'App UI'