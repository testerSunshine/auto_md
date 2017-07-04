# -*- coding: utf8 -*-
__author__ = 'Alex.xu'
#coding=utf-8
import requests
import json
import time
def interfacetest():
    requrl=r'http://risk.dev.fero.com.cn/api/b/risk/v1/riskModel/add?token=8v6IyeSoWr9jmEoBqpA5WaDb6m1vmiV1YE9W26np9kPmLK0MNMs1KCIu2SqvC1Qy'
    #入参key
    reqparams={"modelName":"111", "category":"商户信用贷", "comments":"ewwe"}#get 请求
    myheaders = {
        "User-Agent": r"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0",
        "Accept": r"application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        "Content-Type": "application/json",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": r"http://risk.dev.fero.com.cn/index",
        "Cookie": r"btoken=oYm1JjwXyzpW6iMBP4kCzJ7l62HFZsm7srzxRdcrRkJzZyNZIjNXdZPsAXg2aW4l; empName=%E6%AF%95%E9%A3%9E%E9%A3%9E; empAccount=bifeifei"
    }

    myheaders2 = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        "Content-Type": "application/json",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "http://risk.dev.fero.com.cn/index"
    }

    myheaders3 = {
        "User-Agent": r"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0",
        "Accept": r"application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        "Host": "risk.dev.fero.com.cn",
        "Content-Type": "application/json",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": r"http://risk.dev.fero.com.cn/index",
        "Cookie": r"btoken=oYm1JjwXyzpW6iMBP4kCzJ7l62HFZsm7srzxRdcrRkJzZyNZIjNXdZPsAXg2aW4l; empName=%E6%AF%95%E9%A3%9E%E9%A3%9E; empAccount=bifeifei",
        "Connection": "keep-alive"
    }
    myheaders4 = {
        "User-Agent": r"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0",
        "Content-Type": "application/json"
    }
    # for i in range(1, 5):
    #
    # try:
    #     r1 = requests.post(requrl, data=json.dumps(reqparams), headers=myheaders)
    #     time.sleep(2)
    #     print r1.url
    #     print r1.json()
    # except:
    #     print "haha"
    # try:
    #     r2 = requests.post(requrl, data=json.dumps(reqparams), headers=myheaders2)
    #     time.sleep(2)
    #     r3 = requests.post(requrl, data=json.dumps(reqparams), headers=myheaders3)
    #     time.sleep(2)
    #
    #     print r2.url
    #     # print r2.text
    #     print r2.json()
    #
    #     print r3.url
    #     # print r2.text
    #     print r3.json()
    # except:
    #     print "except!!!"

if __name__=='__main__':
    # interfacetest()
    a = [i for i in range(66181)]
    b = ['a'+str(j) for j in range(66181)]
    print len(a)
    print len(b)
    c = zip(a, b)
    d = dict(c)
    # print c
    print len(c)
    print len(d)