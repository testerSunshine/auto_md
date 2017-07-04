# -*- coding: utf8 -*-
from time import sleep
import os
from PO.basePage import Base
from selenium.webdriver.common.by import By
from PIL import Image
from PO.dashPage import AppUI
from selenium.common.exceptions import NoSuchElementException
from common.base_login import Login

class Message(Base,Login):
    by_myMessage_xpath = (By.XPATH, '//android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout[3]')  # 消息
    by_message_item_id = (By.ID, 'com.hs.yjseller:id/message_listitem_title')  # 消息项
    by_edit_id = (By.ID, 'com.hs.yjseller:id/contentEditTxt')  # 编辑
    by_sendBtn_id = (By.ID, 'com.hs.yjseller:id/sendBtn')  # 发送
    by_chatText_id = (By.ID, 'com.hs.yjseller:id/ease_chat_txt')  # messageText
    by_confirm_id = (By.ID, 'com.hs.yjseller:id/common_toplayout_right')  # 确定
    by_right_id = (By.ID, 'com.hs.yjseller:id/common_toplayout_right')  # 确定
    by_top_title_id = (By.ID, 'com.hs.yjseller:id/common_toplayout_title')  # 确定
    by_pop_message_id = (By.ID, 'android:id/message')  # 弹出消息
    by_button1_id = (By.ID, 'android:id/button1')  # 知道了btn
    by_button2_id = (By.ID, 'android:id/button2')  # 商品管理
    by_goods_sort_right_id = (By.ID, 'com.hs.yjseller:id/goods_sort_menu_right_layout')  # 筛选
    by_proxy_goods_id = (By.ID, 'com.hs.yjseller:id/filter_type_proxy_txt')  # 代销商品
    by_filter_btn_id = (By.ID, 'com.hs.yjseller:id/filter_btn_view')  # 确定
    by_productNameTxtView_id = (By.ID, 'com.hs.yjseller:id/productNameTxtView')  # 第一个分销商品名

    by_goodsNameTxtView_id = (By.ID, 'com.hs.yjseller:id/goodsNameTxtView')  # goodsName
    by_goodsNums_id = (By.ID, 'com.hs.yjseller:id/sellGoodsNumTxtView')  # goodsNum
    by_moreMenu_id = (By.ID, 'com.hs.yjseller:id/moreDropDownView')  # 更多菜单
    by_set_black_list_id = (By.ID, 'com.hs.yjseller:id/sb_person_setting_black_list')  # 黑名单

    # 选择联系人
    by_message_select_group_id = (By.ID, 'com.hs.yjseller:id/search_layout_now')  # 添加通讯录好友
    by_message_select_face2face_id = (By.ID, 'com.hs.yjseller:id/search_layout_face')  # 面对面建群
    by_message_select_partner_id = (By.ID, 'com.hs.yjseller:id/search_layout_partner')  # 选择合伙人
    by_message_select_master_id = (By.ID, 'com.hs.yjseller:id/search_layout_master_item_name')  # 师傅
    by_message_select_friend_id = (By.ID, 'com.hs.yjseller:id/adapter_contacts_friend_item_name')  # 好友
    by_send_message_btn_id = (By.ID, 'com.hs.yjseller:id/btn_person_send_message')  # 发消息
    by_enter_store_btn_id = (By.ID, 'com.hs.yjseller:id/btn_person_goto_shop')  # 进入店铺
    by_bottomTxtView_id = (By.ID, 'com.hs.yjseller:id/bottomTxtView')  # 一键上架商品
    by_messageTxtView_id = (By.ID, 'com.hs.yjseller:id/messageTxtView')  # 一键上架商品

    by_message_partner_name_id = (By.ID, 'com.hs.yjseller:id/partner_adapter_item_name')  # 选择合伙人
    by_radioBtn_class = (By.CLASS_NAME, 'android.widget.RadioButton')  # 选择合伙人
    by_itemName_id = (By.ID, 'com.hs.yjseller:id/contacts_adapter_item_name')  # 选择合伙人

    by_slidelist_title_id = (By.ID, 'com.hs.yjseller:id/customer_manager_slidelist_title')  # 选择合伙人
    by_message_contact_id = (By.ID, 'com.hs.yjseller:id/common_toplayout_left')  # 选择合伙人

    by_contributionNum_id = (By.ID, 'com.hs.yjseller:id/contributionNumTextView')  # 贡献值
    by_partnerNum_id = (By.ID, 'com.hs.yjseller:id/partnerNumTextView') #合伙人
    by_sellNum_id = (By.ID, 'com.hs.yjseller:id/sellNumTextView')   #卖出
    by_explanationTxt_id = (By.ID, 'com.hs.yjseller:id/explanationTxtView')  # 卖出
    by_goodsNameTxt_id = (By.ID, 'com.hs.yjseller:id/goodsNameTxtView')  # 商品
    by_buy_account_id = (By.ID, 'com.hs.yjseller:id/layout_subscription')  # 购物号
    by_first_store_id = (By.ID, 'com.hs.yjseller:id/tv_title')  # 专营店

    by_bottom_items_class = (By.CLASS_NAME, 'android.widget.LinearLayout')  # 第一个专营店
    by_contact_customer_xpath = (By.XPATH, '//android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]')  # 联系客服
    by_enter_store_xpath = (By.XPATH, '//android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[2]')  # 进入店铺
    by_before_messages_xpath = (By.XPATH, '//android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[3]')  # 历史消息
    by_myChatText_id = (By.ID, 'com.hs.yjseller:id/ease_chat_txt')  # 点击客服弹出商品的标题
    by_contact_phone_id = (By.ID, 'com.hs.yjseller:id/phoneBtn')  # 点击客服弹出未开通,电话联系
    by_phone_number_id = (By.ID, 'android:id/text1')  #电话联系,电话号码
    by_phone_number_ids = [(By.ID, 'com.android.contacts:id/digits'), (By.ID, 'android:id/input')]

    by_face2face_edit_class = (By.CLASS_NAME, 'android.widget.EditText')  # 面对面建群编辑
    by_member_id = (By.ID, 'com.hs.yjseller:id/face_num')  # 群聊成员
    by_enterGroupBtn_id = (By.ID, 'com.hs.yjseller:id/enterGroupBtn')  # 进入群聊
    by_groupTips_id = (By.ID, 'com.hs.yjseller:id/transferTipsTxtView')  # 进入群聊

    by_bottom_customer_id = (By.ID, 'com.hs.yjseller:id/goods_detial_bottom_customer')  # 客服

    by_bottomBtn1_id = (By.ID, 'com.hs.yjseller:id/layoutBottomBtn1')  # 上架代销
    by_bottomBtn2_id = (By.ID, 'com.hs.yjseller:id/layoutBottomBtn2')  # 立即分享
    by_okBtn_id = (By.ID, 'com.hs.yjseller:id/okBtn')  # 确定
    by_tvActionTitle_id = (By.ID, 'com.hs.yjseller:id/tvActionTitle1')  # 确定

    def enter_message(self):
        '''
        进入消息
        :return:
        '''
        temp = 0
        while True:
            sleep(1)
            self.myClick(self.find_element('消息模块', *self.by_myMessage_xpath))
            if self.wait_element2((By.ID, 'com.hs.yjseller:id/login_commit'), is_screenshot=False, times=2):
                self.login_by_pwd(self.localReadConfig().getMobileInfo('mobile1'),
                                  self.localReadConfig().getMobileInfo('pwd'))
                print "登录成功，点击..."
                sleep(2)
                self.swipe_to_down(1)

            e = self.wait_element2((By.ID, 'com.hs.yjseller:id/common_toplayout_title'), times=2) # 消息
            if temp >= 3:
                raise NoSuchElementException(msg='进入消息模块失败超过3次')
            if (temp < 3) and e:
                break
            else:
                temp += 1
            sleep(1)

    def find_message_item_by_name(self, mname):
        for i in range(5):
            es = self.find_elements_for_bounds(mname, 0, *self.by_message_item_id)
            for e in es:
                if mname == e[1]:
                    return e
            self.swipe_to_up(1)
        return False, mname

    def face2face(self):
        self.mySend_keys(self.find_element('面对面建群', *self.by_face2face_edit_class)[0], '9527')
        sleep(2)
        self.assertTrue(self.wait_element2(self.by_member_id))
        self.myClick(self.find_element('进入该群', *self.by_enterGroupBtn_id))
        self.assertTrue(self.wait_element2(self.by_groupTips_id))

    def input_message(self, test_message):
        self.input_info(self.find_element('编辑', *self.by_edit_id), test_message)
        self.myClick(self.find_element('发送', *self.by_sendBtn_id))
        es = self.find_elements('MessageText', *self.by_chatText_id)
        try:
            for e in es:
                if e[0].text == test_message:
                    break
        except:
            
            raise NoSuchElementException

    def send_cs_message(self, s_text='testing'):
        e_editTex = self.find_element('输入框', *self.by_edit_id)
        self.myClick(e_editTex)
        self.mySend_keys(e_editTex[0], s_text)
        self.myClick(self.find_element('发送', *self.by_sendBtn_id))
        e_ChatTexts = self.find_elements('已发送的信息', *self.by_myChatText_id)[0]
        for e in e_ChatTexts:
            if e and (e.text.replace(' ', '') == s_text):
                return
        raise NoSuchElementException

    def check_cs(self):
        self.myClick(self.find_element('客服', *self.by_bottom_customer_id))
        self.send_cs_message()