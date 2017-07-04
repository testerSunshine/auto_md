# -*- coding: utf8 -*-
from time import sleep
import os
from PO.basePage import Base
from selenium.webdriver.common.by import By
from PIL import Image
from PO.dashPage import AppUI
from selenium.common.exceptions import NoSuchElementException

from common.base_login import Login
from PO.dashPage import myequal
# TNAMES = ('抽奖团','秒杀团','超级团','海淘团', '试用团')
TNAMES = ('抽奖团','秒杀团','超级团', '海淘团', '试用团')
RATE_COLLECTED = [0.883766233766, 0.839523809524]
RATE_UNCOLLECT = [0.908398268398, 0.911558441558]

RATE_ICON_TUANGOU = {'超级团':0.286033,'海淘团':0.333477,'抽奖团':0.347246,'秒杀团':0.398021, '试用团':0.410053}

# 超级团=0.286033
# 83 28 83 28
# 海淘团=0.333477
# 83 28 83 28
# 抽奖团=0.347246
# 83 28 83 28
# 秒杀团=0.398021

class TuanGou(Base,Login):
    ####################################首页#############################################
    by_first_goods_xpath = (By.XPATH, '//android.webkit.WebView[1]/android.webkit.WebView[1]//android.widget.Button[1]')

    by_tuangou_xpath1 = (By.XPATH, '//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]//android.widget.ImageView')
    by_tuangou_xpath2 = (By.XPATH, '//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[3]//android.widget.ImageView')
    # 活动覆盖
    # by_tuangou_xpath1 = (By.XPATH, '//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[3]//android.widget.ImageView')
    # by_tuangou_xpath2 = (By.XPATH, '//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[4]//android.widget.ImageView')

    by_generalTuan_id = (By.ID, 'com.hs.yjseller:id/name')
    by_generalTuanGoods_id = (By.ID, 'com.hs.yjseller:id/goodsMaskView')
    by_mengTuanZhang_id = (By.ID, 'com.hs.yjseller:id/main_tab_my')  # 萌团长
    by_name = (By.ID, 'com.hs.yjseller:id/titleTxtView')
    by_collect_id = (By.ID, 'com.hs.yjseller:id/goods_detial_bottom_collect')   #收藏(点击)
    by_tvOtherCount_id = (By.ID,'com.hs.yjseller:id/tvOtherCount')  #商品参团人数，或者销售件数(超级团)
    by_goodsTitle_id = (By.ID, 'com.hs.yjseller:id/tvGoodsTitle')  # 商品标题
    by_order_num_id = (By.ID, 'com.hs.yjseller:id/tv_right')  # 订单号

    by_back_id = (By.ID, 'com.hs.yjseller:id/backBtn')  # 商品标题
    by_gdpt_id = (By.ID, 'com.hs.yjseller:id/layoutBottomBtn2')# 更多拼团
    by_mst_goGoods_bt_class = (By.CLASS_NAME, 'android.widget.Button')  # 更多拼团
    by_mst_goGoods_bt_class = (By.CLASS_NAME, 'android.widget.Button')  # 更多拼团

    by_shiyong_goods_id = (By.ID, 'com.hs.yjseller:id/name')  #试用团商品名

    by_btn_xpath = (By.XPATH, '//android.webkit.WebView/android.webkit.WebView//android.widget.Button')

    ####################################商品列表#############################################
    by_msq_name = (By.NAME, '马上抢')
    by_ckmd_id = (By.ID, 'com.hs.yjseller:id/layoutBottomBtn2')   #查看名单
    by_gbmd_name = (By.NAME, '公布名单')
    by_more_choujiang_id = (By.ID, 'com.hs.yjseller:id/tv_bottom')
    by_getGoods_id = (By.ID, 'com.hs.yjseller:id/tv_btn_single_center')

    ###################################商品详情页######################################
    by_costomer_id = (By.ID, 'com.hs.yjseller:id/goods_detial_bottom_customer')
    by_goodsTypes_xpath = (By.XPATH, '//android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup/*')
    by_goodsTypeConfirm_id = (By.ID, 'com.hs.yjseller:id/select_btn_bottom')    #商品规格确定

    ###########################################萌团长数据####################################################
    by_collected_name = (By.NAME, '收藏的商品')  # 已收藏的商品
    by_gouMai_id = (By.ID, 'com.hs.yjseller:id/tv_menu_first')  # 购买菜单
    by_fenXiao_id = (By.ID, 'com.hs.yjseller:id/tv_menu_second')  # 购买菜单

    by_saveGoodsNum_id = (By.ID, 'com.hs.yjseller:id/tv_save_good_num')  # 已收藏的商品数量
    by_first_collected_goods_id = (By.ID, 'com.hs.yjseller:id/name')  # 已收藏的商品数量
    by_rightBtn_id = (By.ID, 'com.hs.yjseller:id/rightBtn')  #  已收藏的商品批量
    by_checkBox_id = (By.ID, 'com.hs.yjseller:id/iv_checkbox')  # 单选框
    by_delete_id = (By.ID, 'com.hs.yjseller:id/tv_delete')  # 单选框

    by_go_where_id = (By.ID, 'com.hs.yjseller:id/tv_go_where')  # 去逛逛

    ###############################################################################################
    #com.hs.yjseller:id / contentEditTxt
    by_customer_editTex_id = (By.ID, 'com.hs.yjseller:id/contentEditTxt')  # 客服输入框
    by_sendBtn_id = (By.ID, 'com.hs.yjseller:id/sendBtn')  # 客服发送信息按钮
    by_linkTitle_id = (By.ID, 'com.hs.yjseller:id/ease_chat_link_title') #点击客服弹出商品的标题
    by_myChatText_id = (By.ID, 'com.hs.yjseller:id/ease_chat_txt')  # 点击客服弹出商品的标题
    ###################################商详页面##########################################
    by_DDGM_id = (By.ID, 'com.hs.yjseller:id/tvActionTitle1')  # 单独购买
    by_canTuan_id = (By.ID, 'com.hs.yjseller:id/tvActionTitle2')  # 团购
    by_LJGM_id = (By.ID, 'com.hs.yjseller:id/btn_right')  # 立即购买

    ###################################订单页面##########################################
    by_comfirmOrder_id = (By.ID, 'com.hs.yjseller:id/receiverAddressInfoReLay') #订单地址
    by_addressTxt_id = (By.ID, 'com.hs.yjseller:id/addressTxtView')
    by_noAddressInfo_id = (By.ID, 'com.hs.yjseller:id/noAddressInfoReLay') #暂无收货地址
    by_tvGoodsTips_id = (By.ID, 'com.hs.yjseller:id/tvGoodsTips')  #选择商品属性
    by_buynow_id = (By.ID, 'com.hs.yjseller:id/select_btn_right') #立即购买
    by_order_ok_id = (By.ID, 'com.hs.yjseller:id/okBtn')  # 订单确认

    ###################################订单详情##########################################
    by_orderStatus_id = (By.ID, 'com.hs.yjseller:id/orderStatusTxtView')  # 订单状态(代付款..)
    s_orderStatusWaitPay = '等待您付款'
    s_orderStatusClosed = '交易关闭'
    by_cancelOrPay_class = (By.CLASS_NAME, 'android.widget.Button')  # [取消订单|付款]
    by_confirm_cancel_order_id = (By.ID, 'com.hs.yjseller:id/bottomOkBtn')  # 确定(取消支付)
    by_delOrder_class = (By.CLASS_NAME, 'android.widget.Button')  # [取消订单|付款]
    by_delOrderOK_id = (By.ID, 'android:id/button2')  # 确定(删除订单)
    by_idCard_id = (By.ID, 'com.hs.yjseller:id/idCardTxtView')
    by_shiyong_btn_id = (By.ID, 'com.hs.yjseller:id/txtViewStatus')

    ###################################选择支付页面##########################################
    by_payMethodName_id = (By.ID, 'com.hs.yjseller:id/payMethodNameTxtView')  # 支付方法
    by_payMethodClose_id = (By.ID, 'com.hs.yjseller:id/selectCloseImgView')  # 关闭支付按钮
    by_cancelPayOK_id = (By.ID, 'android:id/button2')  #确定(取消支付)

    #################################收货地址页面###############################
    by_receiverName_id = (By.ID, 'com.hs.yjseller:id/et_receiver_name')
    by_receiverContactNum_id = (By.ID, 'com.hs.yjseller:id/et_contact_num')
    by_tx_street_id = (By.ID, 'com.hs.yjseller:id/tx_street')
    by_detailAddress_id = (By.ID, 'com.hs.yjseller:id/et_detail_address')
    by_personalID_id = (By.ID, 'com.hs.yjseller:id/et_personal_id')
    by_default_address_id = (By.ID, 'com.hs.yjseller:id/cb_default_address')    #默认地址

    by_ok_id = (By.ID, 'com.hs.yjseller:id/bottomOkBtn')
    by_save_id = (By.ID, 'com.hs.yjseller:id/save_btn')

    tnames = {'抽奖团': ['chou_jiang', '马上抢', '查看名单'],
              '秒杀团': ['miao_sha', '马上抢','已售罄',['提醒我','取消提醒'], '已结束'],
              '超级团': ['chao_ji', '去参团'],
              '海淘团': ['hai_tao', '去开团'],
              '普通团': ['pu_tong', '去开团'],
              '试用团': ['shi_yong', '申请试用', '查看名单']}

    def is_collected(self, tname):
        e_collect = self.find_element('收藏',*self.by_collect_id)
        rect = self.get_bounds(e_collect)
        # print self.tnames[tname][1]
        # file_path = os.path.join(os.getcwd(), '%s_collected.png' % self.tnames[tname][0])
        file_path = os.path.join(os.getcwd(), '%s_collected.png' % self.tnames.get(tname, tname)[0])
        image_collect = self.screenshot_rect(file_path, rect)
        rate = self.image_max_pix_rate(image_collect)
        # print rate

        # 删除图片
        if os.path.exists(file_path):
            os.remove(file_path)

        if rate < (RATE_COLLECTED[1]+RATE_UNCOLLECT[1])/2:
            # print 'collected'
            return True
        else:
            # print 'uncollected'
            return False

    def getTitle(self):
        '''
        :return:返回团购的名称
        '''

        e_title = self.find_element('团购名称', *self.by_name)
        if e_title[0]:
            return e_title[0].text
        else:
            # print "未找到团购标题"
            # raise NoSuchElementException
            return False

    def enterTuangou(self, s_name):
        temp = 0
        while True:
            sleep(1)
            e_name = self.getElement(self.s_name)
            if s_name == '海淘团':
                x0, y0, x1, y1 = self.get_bounds(e_name)
                # self.swipe_to_up(1)
                x, y = x0+(x1-x0)/2, y0+(y1-y0)*2/3
                self.click(x, y)
            else:
                self.myClick(e_name)
            if temp >= 3:
                
                raise NoSuchElementException #进入团购模块错误次数超过3次
            if (temp < 3) and (s_name == self.getTitle()):
                break
            else:
                # self.myClick(self.find_element('返回', *self.by_back_id))
                self.press_back_by_keycode()
                temp += 1
            sleep(1)
        self.swipe_to_down(1)
        # self.assertTrue(self.check_enter_tuangou(s_name))
        self.assertTrue(self.check_enter_tuangou(s_name))

    def enter_mtz(self):
        '''进入萌团长'''
        temp = 0
        while True:
            sleep(1)
            self.myClick(self.find_element('萌团长', *self.myBtn))
            if self.wait_element2((By.ID, 'com.hs.yjseller:id/login_commit'), is_screenshot=False, times=2):
                self.login_by_pwd(self.localReadConfig().getMobileInfo('mobile1'),
                                  self.localReadConfig().getMobileInfo('pwd'))
                # print "登录成功，点击..."
                sleep(2)
                self.swipe_to_down(1)

            e = self.wait_element2((By.ID, 'com.hs.yjseller:id/tv_pending_pay'), times=2) # 我的信息入口
            if temp >= 3:
                
                raise NoSuchElementException #进入萌团长模块错误次数超过3次
            if (temp < 3) and e:
                break
            else:
                temp += 1
            sleep(1)

    def enter_general_tuangou(self):
        self.swipe_to_up(1)
        sleep(2)
        h = int(self.get_size()['height'])
        bound_h = (h/5, h)
        # e = self.find_element_for_bounds("普通团", bound_h, *self.by_generalTuan_id)
        goods_list = [self.by_generalTuanGoods_id]
        e = self.find_element_for_by_list('普通团', goods_list, bound_h=bound_h)
        print e[0].text
        self.myClick(e)
        self.wait_element(self.find_element('参团人数', *self.by_tvOtherCount_id))

    def getElements(self, l_tnames = TNAMES):
        '''
        返回一个4大团的元素对象字典，以团名字为key
        :param TNAMES:团购名字
        :return:
        '''
        es_tuangou = self.find_elements('4大团', *self.by_tuangou_xpath1)

        # print "首页团购个数为:%d" %len(es_tuangou[0])
        dict_es = None
        try:
            dict_es = dict(zip(l_tnames, es_tuangou[0]))
        except:
            myequal.myscreenshot()
            raise NoSuchElementException
        return dict_es

    def getElements2(self, l_tnames = TNAMES):
        '''
        返回一个4大团的元素对象字典，以团名字为key
        :param TNAMES:团购名字
        :return:
        '''
        es_tuangou = self.find_elements('试用团', *self.by_tuangou_xpath2)

        # print "首页团购个数为:%d" %len(es_tuangou[0])
        dict_es = None
        try:
            dict_es = dict([(l_tnames[-1], es_tuangou[0][0])])
        except:
            myequal.myscreenshot()
            raise NoSuchElementException
        return dict_es

    def find_webview_btn(self, bname):
        temp = 0
        e_enter_goods = (False, bname)
        while temp < 5:
            try:
                elements = self.find_elements_for_bounds(bname, 0, *self.by_btn_xpath)
                for e in elements:
                    if bname == e[1]:
                        return e
            except:
                elements = self.find_elements_for_bounds(bname, 0, *self.by_getGoods_id)
                if elements[0] == False:
                    elements = self.find_elements_for_bounds(bname, 0, *self.by_shiyong_btn_id)
                for e in elements:
                    if bname == e[1]:
                        return e
            if '马上抢' == bname:
                break
            self.swipe_to_up(1)
            temp += 1
        return e_enter_goods

    def enter_goods_datil_page(self, tname, stock=True):
        '''
        :param tname: 团名
        :param stock: 是否有库存
        :return:
        '''
        # e_msq = self.find_element(*(By.NAME, '%s' %self.tnames[tname][1]))
        if tname == '秒杀团':
            if stock == True:
                bname = '马上抢'
                try:
                    e_enter_goods = self.find_element_for_bounds(bname, 0, *self.by_btn_xpath)
                    if not e_enter_goods[0]:
                        e_enter_goods = self.find_element_for_bounds(bname, 0, *self.by_getGoods_id)
                        if not e_enter_goods[0]:
                            
                            raise NoSuchElementException
                except:
                    # 当马上抢(申请试用)不存在，断言一下已售罄(查看名单)存不存在，不存在就有问题了
                    if self.find_element_for_bounds(self.tnames[tname][2], 0, *self.by_btn_xpath)[0]:
                        return 0
                    elif self.find_element_for_bounds(self.tnames[tname][4], 0, *self.by_btn_xpath)[0]:
                        return 0
                    else:
                        myequal.myscreenshot()
                        raise NoSuchElementException

            elif stock == False:
                e_enter_goods = self.find_webview_btn('已售罄')
                if not e_enter_goods[0]:
                    return False

        elif tname == '试用团':
            # OutputHelper.recodeInfo(str(self.driver.page_source))
            if stock == True:
                bname = '申请试用'
                try:
                    e_enter_goods = self.find_element_for_bounds(bname, 0, *self.by_btn_xpath)
                    if not e_enter_goods[0]:
                        e_enter_goods = self.find_element_for_bounds(bname, 0, *self.by_shiyong_btn_id)
                    else:
                        raise NoSuchElementException
                except:
                    # 申请试用不存在，断言一下查看名单存不存在，不存在就有问题了
                    if self.find_element_for_bounds(self.tnames[tname][2], 0, *self.by_btn_xpath)[0]:
                        return 0
                    else:
                        raise NoSuchElementException
                # e_enter_goods = self.find_element_by_accessibility_id('马上抢',self.tnames[tname][1])
                # self.assertTrue(e_enter_goods[0])
            elif stock == False:
                e_enter_goods = self.find_webview_btn('查看名单')
                if not e_enter_goods[0]:
                    return False

        elif tname == '抽奖团':
            if True == stock:
                es_enter_goods = self.find_elements(self.tnames[tname][1], *self.by_getGoods_id)
                for e in es_enter_goods[0]:
                    s_ename = e.get_attribute('name')
                    if s_ename == self.tnames[tname][1]:
                        e_enter_goods = (e, s_ename)
                        break
                    elif e.get_attribute('name') == self.tnames[tname][2]:
                        return 0
                    else:
                        raise NoSuchElementException
            elif False == stock:
                temp = 0
                while True:
                    e_enter_goods = (None, '查看名单')
                    es_enter_goods = self.find_elements('商品列表', *self.by_getGoods_id)
                    for e in es_enter_goods[0]:
                        if e.text == self.tnames[tname][2]:
                            e_enter_goods = (e, '查看名单')
                            break
                    if e_enter_goods[0]:
                        break
                    elif temp >=3:
                        # myequal.myscreenshot()
                        # logger.info('%s%s没有找到' % (tname, self.tnames[tname][1], self.tnames[tname][2]))
                        raise NoSuchElementException
                    else:
                        self.swipe_to_up(1)
                        temp += 1
        else:
            e_enter_goods = self.find_element(self.tnames[tname][1], *self.by_getGoods_id)
        self.myClick(e_enter_goods)
        self.wait_element(self.find_element('参团人数', *self.by_tvOtherCount_id))
        sleep(1)
        return True

    def enter_fist_goods_datil_page(self, tname):
        if tname == '秒杀团' or tname == '试用团':
            # OutputHelper.recodeInfo(str(self.driver.page_source))
            e_enter_goods = self.find_element(self.tnames[tname][1], *self.by_first_goods_xpath)
            if not e_enter_goods[0]:
                e_enter_goods = self.find_element(self.tnames[tname][1], *self.by_getGoods_id)
                if not e_enter_goods[0]:
                    e_enter_goods = self.find_element(self.tnames[tname][1], *self.by_shiyong_btn_id)
        else:
            e_enter_goods = self.find_element(self.tnames[tname][1], *self.by_getGoods_id)
        self.myClick(e_enter_goods)
        self.wait_element(self.find_element('参团人数', *self.by_tvOtherCount_id))

    def check_icon(self, tname):
        '''
        检查团购标签是否属实
        :param tname:团购名
        :return:True,False
        '''
        self.enter_fist_goods_datil_page(tname)
        bounds = self.get_tuangou_bounds(tname) #团购名标签bounds(秒杀,海淘,抽奖,超级)
        file_path = os.path.join(os.getcwd(), '%s.png' %self.tnames[tname][0])
        # self.save_screenshot_with_bounds(file_path, bounds)

        image = self.screenshot_rect(file_path, bounds) #团购名标签发截图(秒杀,海淘,抽奖,超级)
        y,x = self.get_x_y(image)
        new_bounds = (x, 0, y, image.size[1])
        image = image.crop(new_bounds)
        rate = self.image_max_pix_rate(image) #获取名称相似率
        # print '%s标签像素比率=%f' %(tname,rate)
        # image.save(file_path)

        # 删除图片
        if os.path.exists(file_path):
            os.remove(file_path)
        return self.is_that_icon(tname, rate)

    def save_screenshot_with_bounds(self, file_path, bounds):
        self.driver.save_screenshot(file_path)
        sleep(1)
        image = Image.open(file_path)
        image_new = image.crop(bounds)
        image_new.save(file_path)

    def confirm_oders(self):
        s_address = ''

    def getElement(self, tname):
        '''
        以团购名字返回首页团购元素
        :param tname:
        :return:
        '''
        if '试用团' == tname:
            return self.getElements2()[tname], tname
        else:
            return self.getElements()[tname], tname

    def is_that_icon(self, tname, rate):
        a = [i[1] for i in RATE_ICON_TUANGOU.items()]
        a.sort()
        i_index = a.index(RATE_ICON_TUANGOU[tname])
        if len(a) == 1:
            if i_index is 0:
                if (rate > RATE_ICON_TUANGOU[tname] - 0.026) and (rate > RATE_ICON_TUANGOU[tname] + 0.026):
                    return True
        elif len(a) > 1:
            if i_index == 0:
                f_avg_dif = (a[i_index + 1] - a[i_index]) / 2.0
                if (rate > a[i_index] - f_avg_dif) and (rate < a[i_index] + f_avg_dif):
                    return True
            elif i_index == len(a) - 1:
                f_avg_dif = (a[i_index] - a[i_index - 1]) / 2.0
                if (rate > a[i_index] - f_avg_dif) and (rate < a[i_index] + f_avg_dif):
                    return True
            else:
                # f_avg_dif = self.get_min_dif(a[i_index - 1:i_index + 1]) / 2.0
                if (rate > (a[i_index] - a[i_index - 1]) / 2.0) and (rate > (a[i_index + 1] - a[i_index]) / 2.0):
                    return True
            return False
        else:
            raise Exception

    def get_tuangou_bounds(self,tname):
        '''
        获取团购名标签bounds
        :return:团购名标签bounds(秒杀,海淘,抽奖,超级),不带团字
        '''
        e_test1 = self.find_element('Old_price', *(By.ID, 'com.hs.yjseller:id/tvGoodsOriginPrice'))
        e_test2 = self.find_element('参团人数', *self.by_tvOtherCount_id)

        start_x = int(e_test1[0].location['x'] + e_test1[0].size['width'] + 1)
        start_y = int(e_test1[0].location['y'])
        end_x = int(e_test2[0].location['x'] - 1)
        end_y = int(e_test1[0].location['y'] + e_test1[0].size['height'] * 4 / 5)

        dx_start = int((end_x - start_x) * 17 / 118)
        dx_end = int((end_x - start_x) * 46 / 118)
        if tname == '超级团':
            dy_start = int((end_y - start_y) * 8 / 45)
            dy_end = int((end_y - start_y) * 10 / 45)
        else:
            dy_start = int((end_y - start_y) * 10 / 45)
            dy_end = int((end_y - start_y) * 7 / 45)
        # bounds = (start_x + dx_start, start_y + dy_start, end_x - dx_end, end_y - dy_end)

        bounds = (start_x, start_y + dy_start, end_x, end_y - dy_end)
        return bounds

    def verify_customer_service(self, s_text):
        #判断是否登录
        if self.wait_element2((By.ID, 'com.hs.yjseller:id/login_commit')):
            self.login_by_pwd(self.localReadConfig().getMobileInfo('mobile1'),
                              self.localReadConfig().getMobileInfo('pwd'))
        self.wait_element(self.find_element('商品图标', *self.by_linkTitle_id))

        e_editTex = self.find_element('输入框', *self.by_customer_editTex_id)[0]
        self.mySend_keys(e_editTex, s_text)
        self.myClick(self.find_element('发送', *self.by_sendBtn_id))
        e_ChatTexts = self.find_elements('已发送的信息', *self.by_myChatText_id)[0]
        for e in e_ChatTexts:
            if e and (e.text.replace(' ', '') == s_text):
                return

        self.swipe_to_down(1)
        e_ChatTexts = self.find_elements('已发送的信息', *self.by_myChatText_id)[0]
        for e in e_ChatTexts:
            if e and (e.text.replace(' ', '') == s_text):
                return

        self.swipe_to_up(1)
        e_ChatTexts = self.find_elements('已发送的信息', *self.by_myChatText_id)[0]
        for e in e_ChatTexts:
            if e and (e.text.replace(' ', '') == s_text):
                return

        raise NoSuchElementException(msg="输入信息不匹配")

    def add_address_info(self, s_name):
        '''
        添加收获地址

        :param s_name:
        :return:
        '''
        self.input_info(self.find_element('收货人姓名', *self.by_receiverName_id), u'徐振环')
        self.input_info(self.find_element('联系人电话', *self.by_receiverContactNum_id), '18918291947')

        self.myClick(self.find_element('省,市,区', *self.by_tx_street_id))
        self.myClick(self.find_element('确定', *self.by_ok_id))

        self.input_info(self.find_element('详细地址', *self.by_detailAddress_id), 'beijin')
        if s_name == "海淘团":
            self.input_info(self.find_element('身份证号', *self.by_personalID_id), '362322199004022418')
            self.press_back_by_keycode()
        self.myClick(self.find_element('保存', *self.by_save_id))
        # e = self.find_element('知道了', *(By.ID, 'android:id/button2'))
        e = self.wait_element2(('保存', self.by_save_id), is_screenshot=False)
        if e:
            self.myClick((e, '保存'))
            self.input_info(self.find_element('身份证号', *self.by_personalID_id), '362322199004022418')
            self.press_back_by_keycode()
            self.myClick(self.find_element('保存', *self.by_save_id))

    def check_address_info(self, s_name):
        e = self.find_element('订单地址', *self.by_addressTxt_id)
        e_idCard = self.find_element('身份地址', *self.by_idCard_id)

        if e[0]:
            if e_idCard[0] and '未填写' == e_idCard[0].text:
                self.myClick(e)
                self.input_info(self.find_element('输入身份证号', *self.by_personalID_id), '362322199004022418')
                self.press_back_by_keycode()
                self.myClick(self.find_element('提交', *self.by_save_id))
            return True
        else:
            e_noAddressInfo = self.find_element('没有订单地址', *self.by_noAddressInfo_id)
            if e_noAddressInfo[0]:
                self.myClick(e_noAddressInfo)
                self.add_address_info(s_name)
                self.wait_element(self.find_element('确认订单', *self.by_comfirmOrder_id))

    def check_enter_tuangou(self, s_name):
        self.swipe_to_down(1)
        if '秒杀团' == s_name:
            # es_enter_goods = None
            # btn_len = 0
            try:
                es_enter_goods = self.find_elements_for_bounds('秒杀团btn', 0, *self.by_btn_xpath)
                btn_len = len(es_enter_goods[0])
            except:
                try:
                    es_enter_goods = es_enter_goods = self.find_elements('商品按钮', *self.by_getGoods_id)
                    btn_len = len(es_enter_goods[0])
                except:
                    
                    raise NoSuchElementException
            if btn_len >= 2: #如果有一个以上商品
                return True
            else:
                return False
        elif '试用团' == s_name:
            es_enter_goods = self.find_elements_for_bounds('试用团btn', 0, *self.by_btn_xpath)
            if not es_enter_goods[0]:
                es_enter_goods = self.find_elements_for_bounds('试用团btn', 0, *self.by_shiyong_btn_id)
            if len(es_enter_goods[0]) >= 1:  # 如果有一个以上商品
                return True
            else:
                return False
        else:
            es_enter_goods = self.find_elements('商品按钮', *self.by_getGoods_id)
            if len(es_enter_goods[0]) >= 1:
                return True

    def check_tvGoodsTips(self, tname, buyType = True):
        '''
        :param tname:
        :param buyType: false代表单独购买
        :return:True 0 false
        '''
        if self.wait_element2((By.ID, 'com.hs.yjseller:id/login_commit')):
            self.login_by_pwd(self.localReadConfig().getMobileInfo('mobile1'),
                              self.localReadConfig().getMobileInfo('pwd'))

        # e_tvGoodsTips = self.find_element('商品属性', *self.by_tvGoodsTips_id)
        e_tvGoodsTips = self.wait_element2(self.by_tvGoodsTips_id, is_screenshot=False)
        if e_tvGoodsTips:
            # e_tvGoodsTips = self.find_element('商品规格', *self.by_tvGoodsTips_id)
            # print self.driver.page_source
            tips = e_tvGoodsTips.text.split('"')[1].split(' ')
            isSelected = e_tvGoodsTips.text.split('"')[0].replace(' ', '')
            print isSelected

            ###############new##############
            if "已选" != isSelected:
                es_goodsTips = self.find_elements('商品规格', *self.by_goodsTypes_xpath)
                # print es_goodsTips[1]
                temp = False
                i = 0
                for e in es_goodsTips[0]:
                    # print e.get_attribute('name')
                    if e.get_attribute('className') == 'android.widget.CheckBox':
                        if not temp:
                            if e.get_attribute('checked') == 'false' and e.get_attribute('clickable') == 'true':
                                print 'click %s' % tips[i]
                                self.myClick((e, tips[i]))
                                i += 1
                                temp = True
                            elif e.get_attribute('checked'):
                                i += 1
                                temp = True
                    else:
                        temp = False
            if buyType:
                self.myClick(self.find_element('参团', *self.by_goodsTypeConfirm_id))
            else:
                self.myClick(self.find_element('单独购买', *self.by_buynow_id))

    def check_collcet_by_mtz(self, s_goods_title, isfenxiao = False):
        self.enter_mtz()
        self.swipe_to_up(1)
        self.swipe_to_up(1)
        e_saveGoodsNum = self.find_element('收藏的商品数', *self.by_saveGoodsNum_id)
        if not e_saveGoodsNum[0]:
            raise NoSuchElementException
        i_saveGoodsNum = int(e_saveGoodsNum[0].text)
        temp = 0
        while True:
            e =  self.find_uiautomator('收藏的商品', 'text')
            self.myClick(e)
            sleep(2)
            # self.myClick((self.driver.find_element_by_accessibility_id(u"收藏的商品"), "收藏的商品"))
            sleep(2)
            if temp < 3 and self.getTitle() == "萌店如何赚":
                self.myClick(self.find_element('返回', *self.by_back_id))
                temp += 1
            elif temp >= 3:
                raise NoSuchElementException  # 进入萌团长模块错误次数超过3次
            else:
                break
        if isfenxiao:
            self.myClick(self.find_element('分销', *self.by_fenXiao_id))
        else:
            self.myClick(self.find_element('购买', *self.by_gouMai_id))
        e_first_goods = self.find_element('第一个商品名', *self.by_first_collected_goods_id)
        # 进去收藏验证刚才收藏的商品
        # print e_first_goods[0].text
        # print s_goods_title
        if self.compare_by_name(e_first_goods[0].text, s_goods_title):
            self.myClick(self.find_element('批量', *self.by_rightBtn_id))
            self.myClick(self.find_element('单选框', *self.by_checkBox_id))
            self.myClick(self.find_element('删除', *self.by_delete_id))
            # self.myClick(self.find_element('确定', *self.by_ok_id))
            if not isfenxiao:
                self.myClick(self.find_uiautomator('确定', 'text'))
            self.press_back()
        else:
            raise NoSuchElementException(msg='对比失败')
        i_saveGoodsNum_new = int(self.find_element('新的收藏的商品数', *self.by_saveGoodsNum_id)[0].text)
        # print i_saveGoodsNum, i_saveGoodsNum_new + 1
        self.assertEqual(i_saveGoodsNum, i_saveGoodsNum_new + 1)

    def check_order(self):
        temp = 0
        while temp < 3:
            self.myClick(self.find_element('确认', *self.by_order_ok_id))
            #判断是否需要登陆

            e = self.wait_element2(self.by_name, times=4)
            if e:
                if e.text != "确认订单":
                    break
            else:
                break
            temp += 1
        sleep(2)

        e = self.wait_element2(self.by_payMethodName_id, times=10)
        if e:
            self.myClick(self.find_element('关闭', *self.by_payMethodClose_id))
            self.myClick(self.find_element('确定', *self.by_cancelPayOK_id))
            e = self.wait_element2(self.by_orderStatus_id, times=10)
            self.assertEqual(e.text, self.s_orderStatusWaitPay)
            self.cancel_order()
        else:
            e = self.find_element('取消', *(By.CLASS_NAME, 'android.widget.Button'))
            if e[0]:
                self.myClick(e)
                self.assertTrue(self.find_element_by_accessibility_id('申请成功', '申请成功'))
            else:
                
                raise NoSuchElementException

    def setCollected(self, s_name):
        e_collect = self.find_element('收藏', *self.by_collect_id)
        if not self.is_collected(s_name):
            self.myClick(e_collect)
            # 如果跳出登录，就执行登录模块
            if self.find_element('登录', *(By.ID, 'com.hs.yjseller:id/login_commit'))[0]:
                self.login_by_pwd(self.localReadConfig().getMobileInfo('mobile1'),
                                  self.localReadConfig().getMobileInfo('pwd'))
            self.assertTrue(self.is_collected(s_name))
        else:
            #已收藏的话就点击取消再收藏一次，这样保证商品再收藏列表的第一个
            self.myClick(e_collect)
            self.myClick(e_collect)
            self.assertTrue(self.is_collected(s_name))
        s_goods_title = self.find_element('商品标题', *self.by_goodsTitle_id)[0].text
        return s_goods_title

    def cancel_order(self):
        es = self.find_elements('取消或付款', *self.by_cancelOrPay_class)
        for e in es[0]:
            temp = 0
            if '取消订单' == e.get_attribute('name'):
                e = (e, '取消订单')
                while True:
                    self.myClick(e)
                    e_confirm = self.wait_element2(self.by_confirm_cancel_order_id)
                    if e_confirm:
                        break
                    elif temp >= 3:
                        
                        raise NoSuchElementException
                    else:
                        temp += 1

                self.myClick((e_confirm, '确定删除'))
                e = self.wait_element2(self.by_orderStatus_id, times=10)

                # self.assertEqual(e.get_attribute('name'), self.s_orderStatusClosed)    #判断是否交易关闭
                # sleep(2)
                # e_delOrd = self.driver.find_elements_by_class_name(self.by_delOrder_class[1])[1], '删除订单'
                # self.myClick(e_delOrd)

                self.assertEqual(e.text, self.s_orderStatusClosed)  # 判断是否交易关闭
                es = self.find_elements('删除订单', *TuanGou.by_delOrder_class)
                for element in es[0]:
                    if element.get_attribute('resourceId') != 'com.hs.yjseller:id/backBtn':
                        self.myClick((element, '删除订单'))
                        break
                self.myClick(self.find_element('确定删除订单', *self.by_delOrderOK_id))
                break
