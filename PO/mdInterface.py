#-*-coding:utf-8-*-
__author__ = 'MR.wen'
import requests


class MD_inteface(object):
    @staticmethod
    def getSendCode(mobile_number):
        myheaders = {'Accept': r'application/json, text/javascript, */*; q=0.01',
                  'Accept-Encoding': 'gzip, deflate, sdch',
                  'Accept-Language': 'zh-CN,zh;q=0.8',
                  'Connection': 'keep-alive',
                  'Host': 'api.vd.cn',
                  'User-Agent': r'okhttp/3.4.1'
                  }

        base_url = 'http://api.vd.cn/v2/account/sendCode'
        sendCode = {"mode": "newLogin", "client_id": "1", "mobile": mobile_number, "BaseAppType": "android",
         "BaseAppVersion": "4.6.0", "SystemVersion": "6.0.1", "_sign_": "D15944473F9DC15CB76547934C6C7981",
         "appIdentifier": "com.hs.yjseller"}

        # result = requests.post(base_url, data=sendCode, headers=myheaders, session="")
        result = requests.post(base_url, data=sendCode, headers=myheaders)
        print result.json()
    @staticmethod
    def getLoginCode(mobile_number,type=1):
        '''
        获取手机验证码
        :param mobile_number:被验证手机号
        :return:返回手机对应验证码
        '''
        base_url = 'http://doc.local.weimob.com/tools/getCode.php'
        hander = {'Accept':'application/json, text/javascript, */*; q=0.01',
                       'Accept-Encoding':'gzip, deflate, sdch',
                       'Accept-Language':'zh-CN,zh;q=0.8',
                       'Connection':'keep-alive',
                       'Cookie':'PHPSESSID=dr33ngkvt6bv9ml0erq0uapv27',
                       'Host':'doc.local.weimob.com',
                       'Referer':'http://doc.local.weimob.com/tools/',
                       'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36',
                       'X-Requested-With':'XMLHttpRequest'
                       }

        if type==1:
            #app登录
            playLoad = {'env':'pl','mobile': str(mobile_number)+'_0086','version':'v2_newLogin','dataType':'json'}
            result = requests.get(base_url,playLoad)
            print base_url
            print playLoad
            print result
            print result.json()
            if result.status_code == 200:
                result = result.json()
                return result['code']
            else:
                return '获取验证码失败...'
        if type==2:
            # H5登录
            playLoad = {'env': 'pl', 'mobile': str(mobile_number)+'_0086', 'version': 'v2_h5Login', 'dataType': 'json'}
            result = requests.get(base_url, playLoad)
            if result.status_code == 200:
                result = result.json()
                return result['code']
            else:
                return '获取验证码失败...'
        if type==3:
            # H5快速登录
            playLoad = {'env': 'pl', 'mobile': str(mobile_number)+'_0086', 'version': 'v2_h5FastLogin', 'dataType': 'json'}
            result = requests.get(base_url, playLoad)
            if result.status_code == 200:
                result = result.json()
                return result['code']
            else:
                return '获取验证码失败...'
        if type==4:
            # 领券
            playLoad = {'env': 'pl', 'mobile': str(mobile_number)+'_0086', 'version': 'v2_h5CouponExchange', 'dataType': 'json'}
            # print base_url
            # print playLoad
            result = requests.get(base_url, playLoad)
            if result.status_code == 200:
                result = result.json()
                return result['code']
            else:
                return '获取验证码失败...'


MD_inteface.getSendCode('18918291947')
# print "\u7cfb\u7edf\u7e41\u5fd9\uff0c\u8bf7\u7a0d\u540e\u518d\u8bd5\uff01"

# a = MD_inteface.getLoginCode(15618715582, type=1)
# a = MD_inteface.getLoginCode(15618715584, type=1)
# print a