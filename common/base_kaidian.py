# -*- coding: utf8 -*-
import random

__author__ = 'MR.wen'
from PO.basePage import Base
from PO.utils import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class Kaidian(Base):
    #----开店页面数据----
    kd_bill_id = (By.ID, 'com.hs.yjseller:id/mdHomeBillLinlayView')
    login_title = (By.ID, 'titleTxtView')

    #----账单页面数据----
    bill_return = (By.ID, 'fortunelist_toplayout_left')
    bill_title = (By.ID, 'fortunelist_toplayout_title')
    bill_leiji = (By.ID, 'fortunelist_toplayout_right')
    bill_type = (By.ID, 'com.hs.yjseller:id/billtypeTxtView')
    bill_list = (By.ID, 'com.hs.yjseller:id/descTxtView') #账单列表页面
    bill_count_id = (By.ID, 'com.hs.yjseller:id/menuTxtView')
    income_today_id = (By.ID, 'com.hs.yjseller:id/home_sub_layout_income')

    #----账单页面数据----
    today_visitors_id = (By.ID, 'com.hs.yjseller:id/layout_home_daily_visit')
    month_sales_id = (By.ID, 'com.hs.yjseller:id/layout_home_month_sales')
    month_income_id = (By.ID, 'com.hs.yjseller:id/layout_home_month_income')
    toplayout_title_id = (By.ID, 'com.hs.yjseller:id/common_toplayout_title') #店铺统计标题
    store_bank_id = (By.ID, 'com.hs.yjseller:id/common_toplayout_left')

    #----店铺数据----
    store_icon_id = (By.ID, 'com.hs.yjseller:id/home_user_icon')
    store_title_id = (By.ID, 'com.hs.yjseller:id/home_shop_title')
    store_details_title_id = (By.ID, 'com.hs.yjseller:id/titleTxtView')
    store_details_bank_id = (By.ID, 'com.hs.yjseller:id/backBtn')

    #----自营添加商品----
    home_add_goods_id = (By.ID, 'com.hs.yjseller:id/home_add_goods')
    add_proprietary_goods_id = (By.ID, 'com.hs.yjseller:id/selfLinLay')#自营入口
    add_daixiao_goods_id = (By.ID, 'com.hs.yjseller:id/wholesaleLinLay')#代销入口
    add_goods_name_id = (By.ID, 'com.hs.yjseller:id/productNameEditTxt')

    add_goods_image_class = (By.CLASS_NAME, 'android.widget.ImageView')#上传图片&分享标签
    add_goods_image_selected_id = (By.ID, 'com.hs.yjseller:id/selectedImgView')
    add_goods_confirm_id = (By.ID, 'com.hs.yjseller:id/rightBtn') #上传图片确定按钮

    add_goods_content_id = (By.ID, 'com.hs.yjseller:id/productIntroEditTxt')
    add_goods_price_id = (By.ID, 'com.hs.yjseller:id/skuPriceEditTxt')# 价格
    #分销
    add_goods_set_commission_id = (By.ID, 'com.hs.yjseller:id/distriReLay')
    add_goods_commission_id = (By.ID, 'com.hs.yjseller:id/distriCommissionEditTxt')# 分佣佣金比例

    add_goods_num_id = (By.ID, 'com.hs.yjseller:id/skuNumEditTxt')#库存
    add_goods_freight_id = (By.ID, 'com.hs.yjseller:id/freightEditTxt')#运费
    add_goods_top_id = (By.ID, 'com.hs.yjseller:id/topSwitchBtn')#置顶商品
    add_goods_switch_id = (By.ID, 'com.hs.yjseller:id/switchBtn')#店长推荐
    add_goods_savelibrary_id = (By.ID, 'com.hs.yjseller:id/saveToLibraryBtn')#保存仓库
    add_goods_shelves_id = (By.ID, 'com.hs.yjseller:id/directShelvesBtn')#直接上架

    add_goods_result_id = (By.ID, 'com.hs.yjseller:id/resultTxtView')#上架状态
    add_wancheng_id = (By.ID, 'com.hs.yjseller:id/rightBtn')#确定
    add_continue_goods_id = (By.ID, 'com.hs.yjseller:id/goAddSelfRunReLay')

    #----自营添加商品----
    add_daixiaogoods_id = (By.ID, 'com.hs.yjseller:id/tv_title0') #进口美食
    add_daixiaogoods_image_id = (By.ID, 'com.hs.yjseller:id/iv_goods_image') #列表图片
    add_goods_detials_daixiao_id = (By.ID, 'com.hs.yjseller:id/tvActionTitle1') #我要代销&下架
    add_goods_queren_daixiao_id = (By.ID, 'com.hs.yjseller:id/okBtn') #确认代销分组


    shaixuan_goods_id = (By.ID, 'com.hs.yjseller:id/goods_sort_menu_right_layout') #筛选
    shaixuan_goods_daixoa_id = (By.ID, 'com.hs.yjseller:id/filter_type_proxy_txt') #筛选代销
    shaixuan_goods_proprietary_id = (By.ID, 'com.hs.yjseller:id/filter_type_self_txt')#筛选自营
    goods_daixioa_and_proprietary_type_id = (By.ID, 'com.hs.yjseller:id/productTypeTxtView') #代销&自营标签，取此标签的text
    goods_detials_image_id = (By.ID, 'com.hs.yjseller:id/menuImgView') #操作商品的标签
    goods_down_id = (By.ID, 'com.hs.yjseller:id/downShelvesTxtView') #下架
    goods_up_id = (By.ID, 'com.hs.yjseller:id/upShelvesTxtView') #上架
    goods_yulan_id = (By.ID, 'com.hs.yjseller:id/preViewTxtView') #预览
    goods_detials_bank_id = (By.ID, 'com.hs.yjseller:id/backBtn')
    goods_details_buy_id = (By.ID, 'btn_buy')
    goods_del_id = (By.ID, 'com.hs.yjseller:id/delTxtView') #删除

    #----商品管理分类----
    shop_count_id = (By.ID, 'com.hs.yjseller:id/linLayView')
    goods_classification_id = (By.ID, 'com.hs.yjseller:id/goodsCategoryTxtView') #商品分类
    goods_recommended_id = (By.ID, 'com.hs.yjseller:id/category_layout_recommend') #店长推荐
    goods_top_id = (By.ID, 'com.hs.yjseller:id/category_layout_top') #置顶商品
    goods_category_id = (By.ID, 'com.hs.yjseller:id/categoryEditTxt') #店长推荐&置顶商品text

    #----订单管理----
    order_list_classname = (By.CLASS_NAME, 'android.widget.RadioButton')

    #----店铺管理----
    shop_yulan_id = (By.ID, 'com.hs.yjseller:id/rightBtn') #店铺预览
    shop_setting_id = (By.ID, 'com.hs.yjseller:id/shopmanager_main_setting') #店铺设置
    shop_setting_heading_id = (By.ID, 'com.hs.yjseller:id/shopsetting_headimg') #设置头像
    shop_setting_heading_image_id = (By.ID, 'android:id/text1') #设置头像
    shop_up_image_xpath = (By.XPATH, '//android.widget.GridView/android.widget.FrameLayout[2]') #选择第一张图片
    shop_up_image_ok_xpath = (By.XPATH, '//android.widget.ImageButton[1]') #确认选中图片
    shop_up_image_status_id = (By.ID, 'com.hs.yjseller:id/shopsetting_headdimgstatus') #头像是否上传成功

    shop_setting_name_id = (By.ID, 'com.hs.yjseller:id/shopsetting_name') #设置昵称
    shop_setting_name_edit_id = (By.ID, 'com.hs.yjseller:id/shopsetting_name_edit') #设置昵称
    shop_setting_name_save_id = (By.ID, 'com.hs.yjseller:id/shopsetting_name_save') #设置昵称
    shop_setting_name_status_id = (By.ID, 'com.hs.yjseller:id/shopsetting_namestatus') #设置昵称


    shop_setting_address_id = (By.ID, 'com.hs.yjseller:id/shopsetting_mjlxdz') #设置地址
    shop_setting_address_ok_id = (By.ID, 'android:id/button2') #知道了
    shop_setting_address_in_status_id = (By.ID, 'com.hs.yjseller:id/setting_dz_txt') #定位到的地址
    shop_setting_address_out_status_id = (By.ID, 'com.hs.yjseller:id/shopsetting_mjlxdz_txt') #外面的地址
    shop_save_address_id = (By.ID, 'com.hs.yjseller:id/saveBtn') #保存地址

    shop_decoration_id = (By.ID, 'com.hs.yjseller:id/shopmanager_main_decorate') #店铺装饰
    shop_decoration_list_id = (By.CLASS_NAME, 'android.widget.RadioButton') #店铺装饰列表
    shop_setting_background_id = (By.ID, 'com.hs.yjseller:id/changeBgBtn') #更换背景&设置幻灯片
    shop_setting_image_id = (By.ID, 'com.hs.yjseller:id/imgView') #选择图片
    shop_setting_OK_id = (By.ID, 'com.hs.yjseller:id/okBtn') #设置

    shop_del_iamge_id = (By.ID, 'com.hs.yjseller:id/delImgView') #删除幻灯片
    shop_add_iamge_id = (By.ID, 'com.hs.yjseller:id/goAddTxtView') #添加幻灯片
    shop_add_iamge_list_id = (By.ID, 'android:id/text1') #选择推荐美图
    shop_select_iamge_list_id = (By.ID, 'com.hs.yjseller:id/slideShowImgView') #选择五个图片
    shop_save_image_id = (By.ID, 'com.hs.yjseller:id/rightBtn') #保存五张图片

    shop_next_image_id = (By.ID, 'com.hs.yjseller:id/nextImgVIew') #下一张图片
    shop_pre_image_id = (By.ID, 'com.hs.yjseller:id/nextImgVIew') #上一张图片
    shop_setting_image_OK_id = (By.ID, 'com.hs.yjseller:id/okBtn') #上一张图片
    shop_pre_id = (By.ID, 'com.hs.yjseller:id/okBtn') #店铺预览
    shop_pre_return_id = (By.ID, 'com.hs.yjseller:id/okBtn') #店铺预览

    shop_Confirm_goods_id = (By.ID, 'com.hs.yjseller:id/shopsetting_zdqrsh') #自动确认收货
    shop_Confirm_goods_status_id = (By.ID, 'com.hs.yjseller:id/shopsetting_zdqrsh') #自动确认收货时间
    shop_order_close_id = (By.ID, 'com.hs.yjseller:id/shopsetting_zdgb') #自动确认收货
    shop_order_close_status_id = (By.ID, 'com.hs.yjseller:id/shopsetting_zdqrskstatus') #自动确认收货状态
    shop_return_sales_id = (By.ID, 'com.hs.yjseller:id/layout_rights') #七天无理由退换
    shop_return_sales_status_id = (By.ID, 'com.hs.yjseller:id/tv_rights_open') #是否开通
    shop_danbao_id = (By.ID, 'com.hs.yjseller:id/shopsetting_wq') #是否开通
    shop_danbao_status_id = (By.ID, 'com.hs.yjseller:id/shopsetting_wqstatus') #是否开通

    shop_decorate_id = (By.ID, 'com.hs.yjseller:id/shopmanager_main_decorate') #店铺装饰
    shop_sales_id = (By.ID, 'com.hs.yjseller:id/goods_sort_menu_left_layout') #商品上下架
    shop_goods_sort_id = (By.ID, 'com.hs.yjseller:id/goods_sort_menu_middle_layout') #商品排序
    shop_goods_sort_list_id = (By.ID, 'com.hs.yjseller:id/nameTxtView') #上下架和商品筛选条件排序列表

    shop_QC_id = (By.ID, 'com.hs.yjseller:id/twoDimenCodeTxtView')#店铺二维码
    shop_save_phone_id = (By.ID, 'com.hs.yjseller:id/shopmanager_qrcode_savephone')#下载店铺
    shop_share_id = (By.ID, 'com.hs.yjseller:id/shopmanager_main_share')#分享店铺

    customer_list_id = (By.ID, 'com.hs.yjseller:id/customer_manager_listitem_img')#客户列表
    customer_order_id = (By.ID, 'com.hs.yjseller:id/adapter_customer_detail_order_img')#订单
    customer_order_detail_id = (By.ID, 'com.hs.yjseller:id/titleTxtView')#订单详情

    collection_money_id = (By.ID, 'com.hs.yjseller:id/collection_stepone_money')
    collection_name_id = (By.ID, 'com.hs.yjseller:id/collection_stepone_name')
    collection_nextstep_id = (By.ID, 'com.hs.yjseller:id/collection_stepone_nextstep')
    collection_money_get_id = (By.ID, 'com.hs.yjseller:id/collection_steptwo_money')
    collection_share_QQ_id = (By.ID, 'com.hs.yjseller:id/share_gridlist_itemicon')
    collection_share_title_id = (By.ID, 'com.hs.yjseller:id/common_toplayout_title')

    shop_help_union_id = (By.ID, 'com.hs.yjseller:id/item_icon')

    shop_help_title_id = (By.ID, 'com.hs.yjseller:id/titleTxtView')

    def boolean_login(self):
        '''判断开店页面是否登录'''
        self.myClick(self.find_uiautomator('开店','text'))
        if self.wait_element2(self.kd_bill_id, is_screenshot=False, times=2):
            print '已登录...'
            return True
        elif self.wait_element2(self.login_title, is_screenshot=False, times=2):
            print '尝试登陆下...'
            self.login_by_pwd(self.localReadConfig().getMobileInfo('mobile1'), self.localReadConfig().getMobileInfo('pwd'))
            self.myClick(self.find_uiautomator('开店', 'text'))
        else:
            print '我也不知道自己在那里了...'
            
            raise NoSuchElementException

    def get_ball_status(self,tpye=1):
        '''找到所有类型的账单'''
        self.leiji = "累计"
        if tpye == 1: #账单类型
            self.myClick(self.find_element('账单', *self.bill_title))
            bill_type = self.find_elements('账单类型',*self.bill_type)[0]
            return bill_type
        if tpye == 2: #2为测试累计账单，由于无法创建测试数据，导致无法校验，所以只校验最后的点击结果
            # self.myClick(self.find_uiautomator(self.leiji,'text'))
            self.myClick(self.find_element('累计', *self.bill_leiji))
            bill_leiji = self.find_elements('日期', *self.bill_count_id)[0]
            return bill_leiji

    def income_by_today(self):
        '''今日收入入口'''
        self.myClick(self.find_element('今日收入', self.income_today_id))

    def store_statistics(self, type=1):
        '''店铺统计入口'''
        if type==1:
            self.myClick(self.find_element('今日访客', *self.today_visitors_id))
        if type==2:
            self.myClick(self.find_element('本月订单', *self.month_sales_id))
        if type==3:
            self.myClick(self.find_element('本月交易额', *self.month_income_id))
        self.swipe_to_left(1)
        title = self.find_element('店铺统计', *self.toplayout_title_id)[0].text
        return title

    def store_bank(self):
        '''返回首页'''
        self.myClick(self.find_element('返回首页',*self.store_bank_id))

    def my_shop(self):
        '''店铺首页、店铺详情'''
        shop_name = self.find_element('首页店铺名称', *self.store_title_id)[0].text.replace(' ', '')
        self.myClick(self.find_element('点击店铺头像', *self.store_icon_id))
        shop_details_name = self.find_element('详情店铺名称', *self.store_details_title_id)[0].text.replace(' ', '')
        return shop_name, shop_details_name

    def __up_image(self, type=0):
        '''上传图片'''
        self.myClick((self.find_elements('上传图片', *self.add_goods_image_class)[0][type], '上传图片'))
        self.myClick(self.find_uiautomator('images', 'text'))
        self.myClick((self.find_elements('选择图片', *self.add_goods_image_selected_id)[0][0], '选择图片'))
        self.myClick(self.find_element('确定', *self.add_goods_confirm_id))

    def add_ziying_goods(self, type=1):
        '''添加商品入口'''
        self.myClick(self.find_element('添加商品', *self.home_add_goods_id))
        if type==1:
            self.myClick(self.find_element('添加自营商品', *self.add_proprietary_goods_id))
        if type==2:
            self.myClick(self.find_element('添加代销商品', *self.add_daixiao_goods_id))

    def get_add_goods_result(self):
        '''添加商品结果'''
        return self.find_element('添加结果', *self.add_goods_result_id)[0].text

    def add_proprietar_goods(self, type=1):
        '''
        添加自营商品
        :param type:1为直销，2为分销
        :return:
        '''
        self.mySend_keys(self.find_element('输入商品名称', *self.add_goods_name_id)[0], u'自营测试商品')
        self.__up_image()#上传商品图片
        self.__up_image(-1)#上传详情配图
        self.mySend_keys(self.swipe_to_up_find_element('价格', *self.add_goods_price_id)[0], u'1')
        sleep(1)
        self.mySend_keys(self.find_element('库存', *self.add_goods_num_id)[0], u'10')
        if type == 1:
            pass
        if type == 2:
            self.myClick(self.swipe_to_down_find_element('开启佣金设置', *self.add_goods_set_commission_id))
            sleep(1)
            self.mySend_keys(self.find_element('设置佣金比例', *self.add_goods_commission_id)[0], '50')
        self.mySend_keys(self.swipe_to_up_find_element('运费', *self.add_goods_freight_id)[0], u'1')
        self.myClick(self.swipe_to_up_find_element('置顶商品', *self.add_goods_top_id))
        self.myClick(self.swipe_to_up_find_element('店长推荐', *self.add_goods_switch_id))
        self.myClick(self.swipe_to_up_find_element('直接上架', *self.add_goods_shelves_id))

    def add_daixiao_goods(self):
        '''添加代销商品'''
        s_name = '上架代销'
        x_name = '下架'
        self.myClick(self.find_element('进口美食', *self.add_daixiaogoods_id))
        self.myClick((self.find_elements('选择商品', *self.add_daixiaogoods_image_id)[0][0], '选择商品'))
        if self.find_element('上架代销', *self.add_goods_detials_daixiao_id)[0]:
            goods_status = self.find_element('上架代销', *self.add_goods_detials_daixiao_id)[0].text.replace(' ','')
            if goods_status == s_name:
                print '该商品未上架代销'
                self.myClick(self.find_element('上架代销', *self.add_goods_detials_daixiao_id))
                if self.wait_element2(self.add_goods_queren_daixiao_id): #判断如果出现分类，则点击掉
                    print '已出现'
                    self.myClick(self.find_element('选择类目', *self.add_goods_queren_daixiao_id))
                print self.find_element('查找下架字段', *self.add_goods_detials_daixiao_id)[0].text.replace(' ','')
                return self.find_element('查找下架字段', *self.add_goods_detials_daixiao_id)[0].text.replace(' ','')
            if goods_status == x_name:
                print '该商品已上架代销，执行下架操作'
                self.myClick(self.find_element('下架操作', *self.add_goods_detials_daixiao_id))
                self.myClick(self.find_element('上架商品', *self.add_goods_detials_daixiao_id))
                if self.wait_element2(self.add_goods_queren_daixiao_id):
                    self.myClick(self.find_element('选择类目', *self.add_goods_queren_daixiao_id))
                return self.find_element('查找下架字段', *self.add_goods_detials_daixiao_id)[0].text.replace(' ','')
            else:
                print '没找到按钮'
                return False
        else:
            print '未进入商详页面'
            return False

    def __goods_operation_by_down(self):
        '''商品执行下架'''
        self.myClick((self.find_elements('操作商品', *self.goods_detials_image_id)[0][0], '操作商品'))
        goods_down = self.find_element('下架', *self.goods_down_id)
        if goods_down[0]:
            self.myClick(goods_down)
            return self.find_element('查找上架按钮', *self.goods_up_id)[0]
        goods_up =self.find_element('假如是上架', *self.goods_up_id)
        if goods_up[0]:
            self.myClick(goods_up)
            self.myClick(self.find_element('下架', *self.goods_down_id))
            return self.find_element('查找上架按钮', *self.goods_up_id)[0]

    def __goods_yulan(self):
        '''预览商品商详校验'''
        self.myClick(self.find_element('预览', *self.goods_yulan_id))
        return self.find_element('立即购买按钮', *self.goods_details_buy_id)[0]

    def __goods_del(self):
        '''商品删除校验'''
        self.myClick(self.find_element('商品删除', *self.goods_del_id))
        return self.find_element('删除控件', *self.goods_del_id)[0]

    def __boolean_goodslist_status(self):
        '''商品列表标签'''
        return self.find_element('自营标签', *self.goods_daixioa_and_proprietary_type_id)[0].text

    def goods_operation(self):
        '''校验商品操作'''
        self.assertEqual(self.__boolean_goodslist_status(), '自营')
        self.assertTrue(self.__goods_operation_by_down())
        self.assertTrue(self.__goods_yulan())
        self.myClick(self.find_element('返回', *self.goods_detials_bank_id))
        self.assertTrue(not self.__goods_del())

    def __get_goods_title(self):
        return self.find_element('店长推荐', *self.goods_category_id)[0].text

    def management_goods(self):
        '''商品分类'''
        self.myClick((self.find_elements('商品管理', *self.shop_count_id)[0][0], '商品管理'))
        self.myClick(self.find_element('商品分类', *self.goods_classification_id))
        self.myClick(self.find_element('店长推荐', *self.goods_recommended_id))
        self.assertEqual(self.__get_goods_title(), '店长推荐')
        self.myClick(self.find_element('返回', *self.goods_detials_bank_id))
        self.myClick(self.find_element('店长推荐', *self.goods_top_id))
        self.assertEqual(self.__get_goods_title(), '置顶商品')

    def management_fenxiao(self):
        '''分销管理'''

    def __get_order_status(self):
        return self.find_elements('订单管理', *self.order_list_classname)[0]

    def order_manger(self):
        '''订单管理'''
        self.myClick((self.find_elements('订单管理', *self.shop_count_id)[0][1], '订单管理'))
        order_list = self.find_elements('订单状态', *self.order_list_classname)
        for i in order_list[0]:
            self.myClick((i, '订单'))
        self.assertTrue(self.__get_order_status())

    def _enter_shop_setting(self, type=1):
        '''进入店铺设置'''
        self.myClick((self.find_elements('店铺管理', *self.shop_count_id)[0][2], '店铺管理'))
        if type==1:
            self.myClick(self.find_element('店铺设置', *self.shop_setting_id))
        if type==2:
            self.myClick(self.find_element('店铺装饰', *self.shop_decoration_id))
        if type==3:
            self.myClick(self.find_element('店铺二维码', *self.shop_QC_id))

    def shop_setting_header(self):
        '''店铺设置-头像设置'''
        self._enter_shop_setting()
        self.myClick(self.find_element('点击头像头像', *self.shop_setting_heading_id))
        self.myClick((self.find_elements('从手机相册选择', *self.shop_setting_heading_image_id)[0][0], '选择'))
        if self.find_uiautomator('最近', 'text', wait_time=5):
            self.myClick(self.find_uiautomator('最近', 'text'))
        self.myClick(self.find_element('选择图片', *self.shop_up_image_xpath))
        if self.wait_element2(self.shop_up_image_ok_xpath):
            print 'OK'
            self.myClick(self.find_element('点击确认', *self.shop_up_image_ok_xpath))
        return self.find_element('获取头像', *self.shop_up_image_status_id)[0]

    def shop_setting_shop_name(self):
        '''店铺设置-昵称设置'''
        self.shop_name = u'文先森的店铺'
        self.myClick(self.find_element('点击店铺名字', *self.shop_setting_name_id))
        self.find_element('更改名字', *self.shop_setting_name_edit_id)[0].clear()
        self.mySend_keys(self.find_element('更改名字', *self.shop_setting_name_edit_id)[0], self.shop_name)
        self.myClick(self.find_element('保存', *self.shop_setting_name_save_id))
        new_shop_name = self.find_element('获取店铺名字', *self.shop_setting_name_status_id)[0].text
        # print new_shop_name
        return new_shop_name

    def shop_setting_address(self):
        '''店铺设置-地址设置'''
        self.myClick(self.find_element('设置店铺地址', *self.shop_setting_address_id))
        self.myClick(self.find_uiautomator('定位当前地址', 'text'))
        self.myClick(self.find_element('知道了', *self.shop_setting_address_ok_id))
        in_address = self.find_element('定位的地址', *self.shop_setting_address_in_status_id)[0].text.split(' ')[-1]
        self.myClick(self.find_element('保存', *self.shop_save_address_id))
        out_address = self.find_element('保存定位的地址', *self.shop_setting_address_out_status_id)[0].text.split(' ')[-1]
        # print in_address, out_address
        return in_address, out_address

    def get_shop_decoration(self, type):
        '''获取店铺封面 type==1为封面，2为店招，3为列表，4为导航'''
        if type==1:
            self.myClick((self.find_elements('封面', *self.shop_decoration_list_id)[0][0], '封面'))
        if type==2:
            self.myClick((self.find_elements('店招', *self.shop_decoration_list_id)[0][1], '店招'))
        if type==3:
            self.myClick((self.find_elements('列表', *self.shop_decoration_list_id)[0][2], '列表'))
        if type==4:
            self.myClick((self.find_elements('导航', *self.shop_decoration_list_id)[0][3], '导航'))

    def get_shop_used_status(self):
        '''获取店铺素材是否被使用'''
        used_status = self.find_element('确认使用', *self.shop_setting_OK_id)[0].text.replace(' ', '')
        print used_status
        if used_status == '使用中':
            return True
        else:
            return False

    def set_shop_image(self):
        '''设置店铺素材'''
        used_name = '使用中'
        if self.get_shop_used_status():  # 如果是使用状态，则切换一下图片，在点击使用
            self.myClick(self.find_element('点击切换滑动', *self.shop_next_image_id))
            self.myClick(self.find_element('确认使用', *self.shop_setting_OK_id))
        else:
            self.myClick(self.find_element('确认使用', *self.shop_setting_OK_id))
        used_text = self.find_element('确认使用', *self.shop_setting_OK_id)[0].text.replace(' ', '')
        self.assertEqual(used_text, used_name)

    def del_iamge(self):
        '''删除所有幻灯片'''
        e = self.find_elements('查找幻灯片', *self.shop_del_iamge_id)[0]
        e = e[::-1]
        print e
        if e:
            for del_image in e:
                self.myClick((del_image, '删除图片'))
        else:
            pass

    def check_shop_image(self):
        '''添加五个幻灯片'''
        e = self.find_elements('选择美图', *self.shop_select_iamge_list_id)[0]
        print len(e)
        if e:
            for i in range(5):
                self.myClick((e[i], '选中图片'))

    def shop_decorate(self, type):
        '''店铺装饰'''
        if type==1:#封面
            self.get_shop_decoration(type=1)
            self.myClick(self.find_element('更换背景', *self.shop_setting_background_id))
            self.myClick((self.find_elements('选择封面图片', *self.shop_setting_image_id)[0][random.randint(1, 3)],'选择封面图片'))
            self.myClick(self.find_element('设定', *self.shop_setting_OK_id))
            self.set_shop_image()
        if type==2:#店招
            self.get_shop_decoration(type=2)
            self.myClick(self.find_element('设置幻灯片', *self.shop_setting_background_id))
            self.del_iamge()
            self.myClick(self.find_element('添加图片', *self.shop_add_iamge_id))
            self.myClick((self.find_elements('选择推荐美图', *self.shop_add_iamge_list_id)[0][0],'选择推荐美图'))
            self.check_shop_image()
            self.myClick(self.find_element('保存图片', *self.shop_save_image_id))
            e = self.find_elements('查找幻灯片', *self.shop_del_iamge_id)[0]
            self.assertEqual(len(e), 5)
            self.myClick(self.find_element('返回', *self.store_details_bank_id))
            self.set_shop_image()
        if type==3:#列表
            self.get_shop_decoration(type=3)
            self.set_shop_image()
        if type==4:#导航
            self.get_shop_decoration(type=4)
            self.set_shop_image()

    def shop_QC_share(self):
        '''店铺二维码'''
        self._enter_shop_setting(type=3)
        self.myClick(self.find_element('保存图片至手机', *self.shop_save_phone_id))
        self.press_back()
        self.myClick(self.find_element('店铺分享', *self.shop_share_id))
        e = self.find_element('分享图片', *self.add_goods_image_class)[0]
        self.assertTrue(e)

    def check_customer_management(self):
        '''客户列表'''
        self.swipe_to_up(1)
        self.myClick((self.find_elements('店铺管理', *self.shop_count_id)[0][3], '店铺管理'))
        self.myClick((self.find_elements('客户列表', *self.customer_list_id)[0][0], '客户列表'))
        self.myClick(self.find_element('点击订单', *self.customer_order_id))
        e = self.find_element('获取订单页面', *self.customer_order_detail_id)[0]
        self.assertTrue(e)
        for i in range(3): #需要退出三次才能到开店页
            self.press_back_by_keycode()

    def friend_collection(self):
        '''好友收款'''
        money = 5
        self.myClick((self.find_elements('店铺管理', *self.shop_count_id)[0][4], '店铺管理'))
        self.mySend_keys(self.find_element('输入金额', *self.collection_money_id)[0], money)
        self.myClick(self.find_element('下一步', *self.collection_nextstep_id))
        s_money = self.find_element('收款价钱', *self.collection_money_get_id)[0].text.split('.')[0]
        print s_money
        self.assertEqual(str(s_money), str(money))
        self.myClick((self.find_elements('QQ分享', *self.collection_share_QQ_id)[0][1], 'QQ分享'))
        self.myClick(self.find_uiautomator('我的电脑', 'text'))
        self.myClick(self.find_uiautomator('发送', 'text'))
        self.myClick(self.find_uiautomator('返回萌店', 'text'))
        common_name = self.find_element('收款标题', *self.collection_share_title_id)[0].text.replace(' ', '')
        self.assertTrue(common_name)

    def tool_box(self):
        '''新手帮助，赚钱联盟'''
        self.swipe_to_up(1)
        # self.myClick((self.find_elements('进入赚钱联盟', *self.shop_help_union_id)[0][6], '进入赚钱联盟'))
        # self.press_back_by_keycode()
        self.myClick((self.find_elements('进入新手帮助', *self.shop_help_union_id)[0][7], '进入新手帮助'))
        help_name = self.find_element('新手帮助', *self.shop_help_title_id)[0].text.replace(' ', '')
        if help_name:
            return help_name
        else:
            return False
