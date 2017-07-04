# -*- coding: utf8 -*-
from PO import readConfig
from PO.apkBase import *


def get_all_device_info():
    """
    获取手机全部信息
    :return 设备信息
    """
    device_info = {}
    adb = ADB()
    readConfigLocal = readConfig.ReadConfig()
    devices_name = adb.get_device_name()  # 获取手机型号
    devices_size = adb.get_screen_resolution()  # 屏幕分辨率
    android_version = adb.get_android_version()  # android版本
    devices_disk = adb.get_disk()  # 获取磁盘信息
    wifi_name = adb.wifi_name()  # 获取wifi名称
    if wifi_name is None:
        wifi_name = '未连接'
    device_battery_temp = adb.get_battery_temp()  # 电池温度
    if 'nt' == os.name:
        app_path = readConfigLocal.getAppiumValue('appPathWin')
    elif 'posix' == os.name:
        app_path = readConfigLocal.getAppiumValue('appPathLinux')
    package_name = ApkInfo(app_path).get_apk_pkg()  # 包名
    app_name = ApkInfo(app_path).get_apk_name()  # 包名
    app_size = ApkInfo(app_path).get_apk_size()  # app大小
    app_version = ApkInfo(app_path).get_apk_version()  # app版本
    sdk_version = adb.get_sdk_version()  # sdk版本
    device_info = {'devices_name': str(devices_name),
                   'devices_size': str(devices_size).replace(',', '*').replace(' ', '').replace('(', '').replace(')', ''),
                   'android_version': str(android_version),
                   'devices_disk': str(devices_disk),
                   'wifi_name': str(wifi_name),
                   'device_battery_temp': str(device_battery_temp),
                   'package_name': str(package_name),
                   'app_name': str(app_name),
                   'app_size': str(app_size),
                   'app_version': str(app_version),
                   'sdk_version': str(sdk_version)}
    return device_info

# devices_name = get_all_device_info()['app_name']
# print devices_name


