# -*- coding: utf8 -*-
from time import sleep

from selenium.webdriver.common.by import By
from PO.basePage import Base
from PO.dashPage import AppUI
import random
import os
from PO.basePage import Base
from PO.dashPage import myequal
from common.base_login import Login
from common.base_tuangou import TuanGou
from time import sleep
from selenium.common.exceptions import NoSuchElementException

SHOP_RATE_COLLECTED = [0.860679012346]
SHOP_RATE_UNCOLLECT = [0.906975308642]
class Mengtz(Base, Login):
    SAVE_ID = (By.ID, 'com.hs.yjseller:id/tv_commit')  # 保存

    #################################设置头像####################################
    #萌团长
    ID_ENTRY_XPATH = (By.XPATH, '//android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout[4]')
    MY_ICON_ID = (By.ID, 'com.hs.yjseller:id/iv_my_icon')  #我的信息入口
    HEAD_IMG_ID = (By.ID, 'com.hs.yjseller:id/center_setting_headimg_layout')  #我的头像入口

    FIRST_IMG_XPATH = (By.XPATH, '//android.widget.GridView/android.widget.FrameLayout[2]')
    DONE_HTC_ID = (By.ID, 'com.htc.photoenhancer:id/crop_done_btn')  #完成
    DONE_HUAWEI_ID = (By.ID, 'com.android.gallery3d:id/head_select_right')  # 完成


    ###################################昵称##################################
    SETTING_NICK_ID  = (By.ID, 'com.hs.yjseller:id/center_setting_name_layout')  #设置昵称
    NICKNAME_TEXT_ID = (By.ID, 'com.hs.yjseller:id/center_setting_name_result')  #昵称text
    NICKNAME_ID = (By.ID, 'com.hs.yjseller:id/et_nickname')  #昵称

    ###################################个人介绍##################################
    INTRODUCE_TEXT_ID = (By.ID, 'com.hs.yjseller:id/tv_self_intro')  #个人介绍文本
    EDIT_INTRODUCE_ID = (By.ID, 'com.hs.yjseller:id/et_message')  #个人介绍编辑框

    ALER_TITLE_ID = (By.ID, 'android:id/alertTitle')  #弹出框标题
    COMFIRM_ID = (By.ID, 'android:id/button2')  #确认

    BACK_BTN1_ID = (By.ID, 'com.hs.yjseller:id/fortunelist_toplayout_left')
    BACK_BTN2_ID = (By.ID, 'com.hs.yjseller:id/backBtn')
    ###################################收货地址##################################
    RECEIVE_ADDR_ID = (By.ID, 'com.hs.yjseller:id/tv_receive_addr')  #收货地址
    # 暂无收货地址哦~
    APPEND_ADDR_ID = (By.ID, 'com.hs.yjseller:id/append_btn')  # 添加收货地址
    ADDRESS_TEXT_ID = (By.ID, 'com.hs.yjseller:id/address_txt')  # 收货地址
    RECEIVE_ADDR_XPATH = (By.XPATH, "//android.widget.ListView/android.widget.FrameLayout[1]")
    PHONE_NUM_ID = (By.ID, 'com.hs.yjseller:id/address_phoneNum')  # 收货人联系电话
    DELETE_RECEIVE_ADDR_ID = (By.ID, 'com.hs.yjseller:id/rightTxtView')  # 收货人联系电话

    ###################################我是萌团长##################################
    I_AM_MTZ_ID = (By.ID, 'com.hs.yjseller:id/tv_meng_head')  # 我是萌团长

    ###################################我的二维码##################################
    WEICHAT_ID = (By.ID, 'com.hs.yjseller:id/qrcodeWeiXinImgView')

    ###################################商品多规格##################################
    by_tvGoodsTips_id = (By.ID, 'com.hs.yjseller:id/tvGoodsTips')  # 选择商品属性
    by_goodsTypes_xpath = (By.XPATH, '//android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup/*')

    ###################################累计奖金##################################
    TOTAL_MONEY_ID = (By.ID, 'com.hs.yjseller:id/ll_total_money')  # 进入我的二维码

    ###################################二维码##################################
    MY_QR_CODE_ID = (By.ID, 'com.hs.yjseller:id/ll_my_code')  # 进入我的二维码
    QR_CODE_ID = (By.ID, 'com.hs.yjseller:id/qrcodeImgView')  # 二维码
    QR_CODE_SAVE_ID = (By.ID, 'com.hs.yjseller:id/dialogSaveTxtView')  # 二维码保存

    ###################################萌团长收入##################################
    MTZ_BILL_ID = (By.ID, 'com.hs.yjseller:id/fortneTxtView')  # 账单
    BILL_EMPTY_ID = (By.ID, 'com.hs.yjseller:id/empty_text')  # 没有记录
    BILL_TOTAL_ID = (By.ID, 'com.hs.yjseller:id/fortunelist_toplayout_right')  # 累计
    BILL_RECORD_ID = (By.ID, 'com.hs.yjseller:id/descTxtView')  # 账单记录
    BILL_TOTAL_POP_ICON_ID = (By.ID, 'com.hs.yjseller:id/billtypeTxtView')  # 账单记录
    BILL_TOTAL_POP_ICON_ID2 = (By.ID, 'com.hs.yjseller:id/menuTxtView')

    MTZ_RHZ_ID = (By.ID, 'com.hs.yjseller:id/mruleTexView')  # 萌团长如何赚

    TODAY_INCOME_ID = (By.ID, 'com.hs.yjseller:id/todayEarnTxtView')
    MONTH_INCOME_ID = (By.ID, 'com.hs.yjseller:id/monthEarnReLay')
    TOTAL_INCOME_ID = (By.ID, 'com.hs.yjseller:id/totalEarnReLay')
    WAIT_CONFIRM_INCOME_ID = (By.ID, 'com.hs.yjseller:id/dqrReLay')

    KTX_FUND_ID = (By.ID, 'com.hs.yjseller:id/ktxReLay')  # 可提现金额
    KTX_BALANCE_ID = (By.ID, 'com.hs.yjseller:id/tv_balance')  # 可提现金额
    TX_RECODE_ID = (By.ID, 'com.hs.yjseller:id/rightTxtView')  # 提现记录

    MY_INCOME_TYPE_ID = (By.ID, 'com.hs.yjseller:id/titleLinLay')  # 收入类型
    POP_INCOME_TYPE_ID = (By.ID, 'com.hs.yjseller:id/billflow_popuplayout_text')  # 收入类型

    MY_BALANCE_BACK_ID = (By.ID, 'com.hs.yjseller:id/backBtn')

    TX_BUY_GIFT_ID = (By.ID, 'com.hs.yjseller:id/mbtnSendMessage')

    ###################################我的团员##################################
    MY_PARTNER_NUM_ID = (By.ID, 'com.hs.yjseller:id/tv_my_members')
    MY_PARTNER_NAME_ID = (By.ID, 'com.hs.yjseller:id/tv_my_members_name')
    GET_PARTNER_BY_QRCODE_ID = (By.ID, 'com.hs.yjseller:id/tv_my_members_hint_title')

    ###################################待付款##################################
    WAIT_PAYMENT_ID = (By.ID, 'com.hs.yjseller:id/tv_pending_pay') #待付款
    PRODUCT_ID = (By.ID, 'com.hs.yjseller:id/productLinLay')
    EMPTY_BTN_ID = (By.ID, 'com.hs.yjseller:id/emptyBtn')
    WAIT_SEND_ID = (By.ID, 'com.hs.yjseller:id/layout_pending_send')  #待发货
    WAIT_RECEIVE_ID = (By.ID, 'com.hs.yjseller:id/tv_pending_receive')  # 待收货
    WAIT_COMMENT_ID = (By.ID, 'com.hs.yjseller:id/tv_pending_comment')  # 待评价
    CASH_BACK_ID = (By.ID, 'com.hs.yjseller:id/tv_cash_back')  # 退款/维权



    ###################################待发货##################################
    WAIT_DELIVERY_ID = (By.ID, 'com.hs.yjseller:id/tv_pending_send')
    PRODUCT_ID = (By.ID, 'com.hs.yjseller:id/productLinLay')
    EMPTY_BTN_ID = (By.ID, 'com.hs.yjseller:id/emptyBtn')


    ###################################取消订单##################################
    by_cancelOrPay_class = (By.CLASS_NAME, 'android.widget.Button')  # [取消订单|付款]
    by_confirm_cancel_order_id = (By.ID, 'com.hs.yjseller:id/bottomOkBtn')  # 确定(取消支付)
    by_orderStatus_id = (By.ID, 'com.hs.yjseller:id/orderStatusTxtView')  # 订单状态(代付款..)
    s_orderStatusClosed = '交易关闭'
    by_delOrder_class = (By.CLASS_NAME, 'android.widget.Button')  # [取消订单|付款]
    by_delOrderOK_id = (By.ID, 'android:id/button2')  # 确定(删除订单)

    ALL_ORDER_ID = (By.ID, 'com.hs.yjseller:id/layout_all_orders_item')  # 全部订单

    ###################################钱包##################################

    WALLET_ID = (By.ID, 'com.hs.yjseller:id/tv_my_fortune')  # 钱包
    WALLET_BILL_ID = (By.ID, 'com.hs.yjseller:id/myRewardTxtView')  # 钱包账单
    ALL_BILL_ID = (By.ID, 'com.hs.yjseller:id/fortunelist_toplayout_title')  # 钱包
    EXPECT_INCOME_ID = (By.ID, 'com.hs.yjseller:id/tv_expected_income')  # 总资产
    ASSERT_ID = (By.ID, 'com.hs.yjseller:id/assetTxtView')  # 资产额

    ASSERT_NAME_ID = (By.ID, 'com.hs.yjseller:id/layout_father')  # 资产名

    RATE_OF_ID = (By.ID, 'com.hs.yjseller:id/rateOfReturn')  # 银行卡
    ENTER_CARD_ID = (By.ID, 'com.hs.yjseller:id/layout_card_pack')  # 卡卷
    CARD_ITEM_ID = (By.ID, 'com.hs.yjseller:id/layout_single_coupon')  # 卡卷item
    EXCHANGE_ID = (By.ID, 'com.hs.yjseller:id/rightTxtView')  # 兑换
    EDIT_TEXT_CLASS = (By.CLASS_NAME, 'ndroid.widget.EditText')  # 兑换

    BY_DHJ_ID = (By.ID, 'com.hs.yjseller:id/rightTxtView')  # 兑换券


    #########################店铺收藏########################
    by_back_id = (By.ID, 'com.hs.yjseller:id/backBtn')  # 商品标题
    SEARSH_ID = (By.ID, 'com.hs.yjseller:id/title')  # 搜索
    XLK_ID = (By.ID, 'com.hs.yjseller:id/histroyTopTypeLinLay')  # 下拉框
    DP_SP_ID = (By.ID, 'com.hs.yjseller:id/typeTxtView')  # 选项
    SEARCH_BTN_ID = (By.ID, 'com.hs.yjseller:id/searchCancelBtn')  # 搜索
    SHOPNAME_ID = (By.ID, 'com.hs.yjseller:id/shopNameTxtView')  # 店铺项
    SHOP_COLLECT_ID = (By.ID, 'com.hs.yjseller:id/enshrineImageView')  # 店铺收藏
    SHOPNAME_REAl_ID = (By.ID, 'com.hs.yjseller:id/shopName')  # 店铺名字
    SHOPNAME_NUM_ID = (By.ID, 'com.hs.yjseller:id/tv_save_shop_num')  # 关注的店铺数量
    MTZ_SHOPNAME_ID = (By.ID, 'com.hs.yjseller:id/item_name')  # 萌团长收藏第一个店铺名字

    ##########################店铺收藏########################
    SETTING_ID = (By.ID, 'com.hs.yjseller:id/iv_my_setting')  # 设置
    ONCEBTN_ID = (By.ID, 'android:id/button_once')  # 设置

    def enter_mtz(self):
        temp = 0
        while True:
            sleep(1)
            e = self.find_element(u'萌团长', *self.myBtn)
            self.myClick(e)
            self.swipe_to_down(1)
            if self.wait_element2((By.ID, 'com.hs.yjseller:id/login_commit'), is_screenshot=False, times=2):
                self.login_by_pwd(self.localReadConfig().getMobileInfo('mobile1'),
                                  self.localReadConfig().getMobileInfo('pwd'))
                # print "登录成功，点击..."
                sleep(2)
                self.swipe_to_down(1)
            e = self.wait_element2((By.ID, 'com.hs.yjseller:id/tv_pending_pay'), times=2) # 我的信息入口
            if temp >= 3:
                # 
                raise NoSuchElementException #进入萌团长模块错误次数超过3次
            if (temp < 3) and e:
                break
            else:
                temp += 1
            sleep(1)

    def random_number(self, randomlength=8):
        return ''.join([str(random.randint(0, 9)) for i in range(randomlength)])

    def add_address_info(self):
        '''
        添加收获地址

        :param s_name:
        :return:
        '''
        s_phone_number = '138' + self.random_number()   #随机生成一个138电话号码

        self.input_info(self.find_element('收货人姓名', *TuanGou.by_receiverName_id), u'徐振环')
        self.input_info(self.find_element('联系人电话', *TuanGou.by_receiverContactNum_id), s_phone_number)
        self.myClick(self.find_element('省,市,区', *TuanGou.by_tx_street_id))
        self.myClick(self.find_element('确定', *TuanGou.by_ok_id))

        self.input_info(self.find_element('详细地址', *TuanGou.by_detailAddress_id), 'beijin')
        self.myClick(self.find_element('设为默认地址', *TuanGou.by_default_address_id))
        self.myClick(self.find_element('保存', *TuanGou.by_save_id))
        # e = self.find_element('知道了', *(By.ID, 'android:id/button2'))
        e = self.wait_element2(('保存', TuanGou.by_save_id), is_screenshot=False)
        if e:
            self.myClick((e, '保存'))
            self.input_info(self.find_element('身份证号', *TuanGou.by_personalID_id), '362322199004022418')
            self.press_back_by_keycode()
            self.myClick(self.find_element('保存', *TuanGou.by_save_id))
        return s_phone_number

    def check_address_info(self, s_phone_number):
        temp = 0
        while temp < 10:
            # e = self.find_element('收货人电话', *self.PHONE_NUM_ID)
            e = self.wait_element2(self.PHONE_NUM_ID)
            if not e:
                break
            e_phone_number = e.text.replace(' ', '')
            if e_phone_number == s_phone_number.replace(' ', ''):
                flag = True

            self.myClick((e, '收货人电话'))
            self.myClick(self.find_element('删除收货地址', *self.DELETE_RECEIVE_ADDR_ID))
            temp += 1

        #收货人联系方式有误
        self.assertTrue(flag)

    def check_tvGoodsTips(self, buyType=True):
        '''

        :param tname:
        :param buyType: false代表单独购买
        :return:True 0 false
        '''
        # e_tvGoodsTips = self.find_element('商品属性', *self.by_tvGoodsTips_id)
        e_tvGoodsTips = self.wait_element2(TuanGou.by_tvGoodsTips_id, is_screenshot=False)
        if e_tvGoodsTips:
            # e_tvGoodsTips = self.find_element('商品规格', *self.by_tvGoodsTips_id)
            # print self.driver.page_source
            tips = e_tvGoodsTips.text.split('"')[1].split(' ')
            isSelected = e_tvGoodsTips.text.split('"')[0].replace(' ', '')
            print isSelected
            if "已选" != isSelected:
                es_goodsTips = self.find_elements('商品规格', *TuanGou.by_goodsTypes_xpath)
                print es_goodsTips[1]
                temp = False
                i = 0
                for e in es_goodsTips[0]:
                    if e.get_attribute('className') == 'android.widget.CheckBox':
                        if not temp:
                            if e.get_attribute('checked') == 'false':
                                print 'click %s' % tips[i]
                                self.myClick((e, tips[i]))
                                i += 1
                        temp = True
                    else:
                        temp = False

            if buyType:
                self.myClick(self.find_element('参团', *TuanGou.by_goodsTypeConfirm_id))
            else:
                self.myClick(self.find_element('单独购买', *TuanGou.by_buynow_id))

    def check_address_info(self, s_name):
        e = self.find_element('订单地址', *TuanGou.by_addressTxt_id)
        if e[0]:
            return True
        else:
            e_noAddressInfo = self.find_element('没有订单地址', *TuanGou.by_noAddressInfo_id)
            if e_noAddressInfo[0]:
                self.myClick(e_noAddressInfo)
                self.add_address_info(s_name)
                self.wait_element(self.find_element('确认订单', *TuanGou.by_comfirmOrder_id))

    def check_order(self):
        self.myClick(self.find_element('确认', *TuanGou.by_order_ok_id))
        sleep(2)
        e = self.wait_element2(TuanGou.by_payMethodName_id, times=10)
        if e:
            self.myClick(self.find_element('关闭', *TuanGou.by_payMethodClose_id))
            self.myClick(self.find_element('确定', *TuanGou.by_cancelPayOK_id))
            e = self.wait_element2(TuanGou.by_orderStatus_id, times=10)
            print e.text
            self.assertEqual(e.text, TuanGou.s_orderStatusWaitPay)
        else:
            
            raise NoSuchElementException

    def check_qrcode(self):
        e_qrcode = self.find_element('二维码', *self.QR_CODE_ID)
        self.driver.drag_and_drop(e_qrcode[0], e_qrcode[0])
        self.myClick(self.find_element('保存', *self.QR_CODE_SAVE_ID))
        sleep(2)
        self.assertTrue(self.wait_element2(self.QR_CODE_ID))

    def check_mtz_rhz(self):
        '''
        检查萌团长如何赚
        :return:
        '''
        self.myClick(self.find_element('萌团长如何赚', *self.MTZ_RHZ_ID))
        e = self.swipe_to_up_find_element('招募更多团员', *(By.ID, 'btn1'))
        self.assertTrue(e[0])
        e_gobuy = self.get_qwgm()
        self.assertTrue(e_gobuy[0])

    def check_bill(self):
        '''
        检查账单
        :return:
        '''
        self.myClick(self.find_element('账单', *self.MTZ_BILL_ID))
        temp = False  # 定义一个标识,如果首页有账单,那么累计里面一定有账单
        if not self.wait_element2(self.BILL_EMPTY_ID):
            self.assertTrue(self.wait_element2(self.BILL_RECORD_ID))
            temp = True
        self.myClick(self.find_element('累计', *self.BILL_TOTAL_ID))
        es = self.find_elements('今日,本月,累计', *self.BILL_TOTAL_POP_ICON_ID2)
        print len(es[0])
        for e in es[0]:
            self.myClick((e, '今日,本月,累计'))
            sleep(2)
            if not self.wait_element2(self.BILL_EMPTY_ID):
                self.assertTrue(self.wait_element2(self.BILL_RECORD_ID))
            self.myClick(self.find_element('累计', *self.BILL_TOTAL_ID))

    def check_bill_for_wallet(self):
        self.myClick(self.find_element('全部账单', *self.ALL_BILL_ID))
        es = self.find_elements('所有账单类型', *self.BILL_TOTAL_POP_ICON_ID)
        print len(es[0])
        for e in es[0]:
            self.myClick((e, e.text))
            sleep(2)
            if not self.wait_element2(self.BILL_EMPTY_ID):
                self.assertTrue(self.wait_element2(self.BILL_RECORD_ID))
            self.myClick(self.find_element('全部账单', *self.ALL_BILL_ID))

    def check_recode(self, ename, *by):
        self.myClick(self.find_element(ename, *by))
        sleep(2)
        empty_flags = [self.BILL_EMPTY_ID, self.EMPTY_BTN_ID]
        for empty_flag in empty_flags:
            e = self.wait_element2(empty_flag, times=2)
            if e:
                self.my_press_back()
                return

        #如果不为空就判断是否有记录存在
        recodes = [self.PRODUCT_ID, self.BILL_RECORD_ID]
        temp = False
        for recode in recodes:
            if self.wait_element2(recode, times=2):
                temp = True
        self.assertTrue(temp)
        self.my_press_back()

    def my_press_back(self):
        # 按返回键
        back_btn_bys = [self.BACK_BTN1_ID, self.BACK_BTN2_ID]
        for back_btn_by in back_btn_bys:
            e = self.wait_element2(back_btn_by, times=3)
            if e:
                self.myClick((e, '返回'))
                sleep(1)
                return
        
        raise NoSuchElementException  # 进入萌团长模块错误次数超过3次

    def del_order(self):
        flag = True
        while flag:
            es = self.find_elements('删除订单', *self.by_cancelOrPay_class)
            for e in es[0]:
                temp = 0
                if '删除订单' == e.get_attribute('name'):
                    e = (e, '删除订单')
                    while True:
                        self.myClick(e)
                        e_confirm = self.wait_element2(self.COMFIRM_ID)
                        if e_confirm:
                            break
                        elif temp >= 3:
                            
                            raise NoSuchElementException
                        else:
                            temp += 1

                    self.myClick((e_confirm, '确定删除'))
                    flag = True
                    break
                else:
                    flag = False

    def my_cancel_order(self):
        flag = True
        while flag:
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
                    flag = True
                    break
                else:
                    flag = False

    def check_assert(self):
        '''检查钱包所有资产'''

        assert_names = ['收入', '余额', '银行卡', '聚宝匯理财']
        # 总资产
        self.myClick(self.find_element('总资产', *self.EXPECT_INCOME_ID))
        self.assertTrue(self.wait_element2(self.ASSERT_ID))
        self.my_press_back()

        es = self.find_elements('收入,余额,银行卡,聚宝匯理财', *self.ASSERT_NAME_ID)[0]
        print len(es)
        for e in es:
            if '收入' == e.text:
                self.myClick((e, '收入'))
                self.assertTrue(self.wait_element2(self.TODAY_INCOME_ID))
            elif '余额' == e.text:
                self.myClick((e, '余额'))
                self.assertTrue(self.wait_element2(self.KTX_BALANCE_ID))
            elif '银行卡' == e.text:
                self.myClick((e, '银行卡'))
            elif '聚宝匯理财' == e.text:
                self.myClick((e, '聚宝匯理财'))
                self.assertTrue(self.wait_element2(self.RATE_OF_ID))

    def enter_collect(self):
        temp = 0
        while True:
            self.myClick(self.find_uiautomator('收藏的商品', 'text'))
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

    def shop_is_collect(self):
        e_collect = self.find_element('收藏', *self.SHOP_COLLECT_ID)
        rect = self.get_bounds(e_collect)
        # print self.tnames[tname][1]
        file_path = os.path.join(os.getcwd(), '%s_collected.png' % 'shop')
        image_collect = self.screenshot_rect(file_path, rect)
        rate = self.image_max_pix_rate(image_collect)
        print rate

        # 删除图片
        if os.path.exists(file_path):
            os.remove(file_path)

        if rate < (SHOP_RATE_COLLECTED[0] + SHOP_RATE_UNCOLLECT[0]) / 2:
            print '已收藏'
            return True
        else:
            print '未收藏'
            return False

    def shop_set_collect(self):
        e_collect = self.find_element('收藏', *self.SHOP_COLLECT_ID)
        if not self.shop_is_collect():
            self.myClick(e_collect)
            # 如果跳出登录，就执行登录模块
            if self.find_element('登录', *(By.ID, 'com.hs.yjseller:id/login_commit'))[0]:
                self.login_by_pwd(self.localReadConfig().getMobileInfo('mobile1'),
                                  self.localReadConfig().getMobileInfo('pwd'))

            self.assertTrue(self.shop_is_collect())
        else:
            # 已收藏的话就点击取消再收藏一次，这样保证商品再收藏列表的第一个
            self.myClick(e_collect)
            self.myClick(e_collect)
            self.assertTrue(self.shop_is_collect())
        s_shop_title = self.find_element('商品标题', *self.SHOPNAME_REAl_ID)[0].text
        return s_shop_title

    def search_shop(self, s_shop_name):
        self.myClick(self.find_element('搜索', *self.SEARSH_ID))
        self.myClick(self.find_element('下拉框', *self.XLK_ID))
        e = None
        try:
            e = self.find_elements('商品_店铺', *self.DP_SP_ID)[0][1], '店铺'
        except:
            myequal.myscreenshot()
            raise NoSuchElementException
        self.myClick(e)

        self.input_info(self.find_element('搜索', *(By.ID, 'com.hs.yjseller:id/searchEditTxt')), s_shop_name)
        self.myClick(self.find_element('搜索', *self.SEARCH_BTN_ID))
        temp = 0
        while temp < 3:
            e = self.wait_element2(self.SHOPNAME_ID)
            if e and temp < 3:
                self.myClick((e, '店铺名称'))
                break
            else:
                temp += 1

    def get_qwgm(self):
        by_qwgm_huawei_xpath = (By.XPATH, '//android.webkit.WebView/android.webkit.WebView/android.view.View/android.widget.ListView[last()]/android.view.View[1]/android.view.View[2]')
        by_qwgm_htc_xpath = (By.XPATH,
                         '//android.webkit.WebView/android.webkit.WebView/android.widget.ListView[last()]/android.view.View[1]')
        self.swipe_to_up(3)
        loc_list = [by_qwgm_huawei_xpath, by_qwgm_htc_xpath]

        # return self.find_element('前往购买', *by_qwgm_xpath)
        return self.find_element_for_by_list('前往购买', loc_list)

