# -*- coding: utf-8 -*-
import os
import pylab as pl
import time
from PO import apkBase
from PO import readConfig
from PO.apkBase import ADB

flag = '_CPU_MEN'
def create_file(type):
    '''
    创建pre text文件夹
    :param type: 1为创建图片，2为txt
    :return:
    '''
    now = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))
    day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    run_path = os.getcwd()
    if 'TestCase' in run_path:
        run_path = os.path.join(run_path, os.pardir, os.pardir, os.pardir)

    pre_img_file = os.path.abspath(os.path.join(run_path, 'Result', day, "pre"))
    if os.path.exists(pre_img_file):
        if type == 1:
            filename_img = os.path.join(pre_img_file, '%s.png' % now)
            return filename_img
        if type == 2:
            filename_txt = os.path.join(pre_img_file, 'cpu_men.txt')
        return filename_txt
    else:
        # print "create path!!!"
        os.makedirs(pre_img_file)
        if type == 1:
            filename_img = os.path.join(pre_img_file, '%s.png' % now)
            return filename_img
        if type == 2:
            filename_txt = os.path.join(pre_img_file, 'cpu_men.txt')
        return filename_txt

def write_cpu_men():
    """
    获取cpu men ，并写入txt文件
    :return cpu,men 写入log跟踪
    """
    # print "exec write_cpu_men!!!!!!!!!!!!!!!!!!!!!!!!"
    readConfigLocal = readConfig.ReadConfig()
    if 'nt' == os.name:
        app_path = readConfigLocal.getAppiumValue('appPathWin')
    elif 'posix' == os.name:
        app_path = readConfigLocal.getAppiumValue('appPathLinux')
    myInit = apkBase.ApkInfo(apkpath=r"%s" % app_path)
    adb = ADB()
    cpu = adb.get_cpu(myInit.get_apk_pkg())
    men = adb.get_mem(myInit.get_apk_pkg())
    content = [str(cpu), ',', str(men), ',']
    content = ''.join(content)
    my_filepath = create_file(type=2)
    # print 'my_file:isExist:', os.path.exists(my_filepath)
    with open(my_filepath, 'a+') as f:
        # print 'my_file:isExist:', os.path.exists(my_filepath)
        f.writelines(content)
    return str(cpu), str(men)

def data_marker(cpu, mem, path):
    """
    生成性能图片
    :param cpu: cpu列表
    :param mem: 内存列表
    :param path: 存储的文件路径
    :return:
    """
    # print "exec data_marker!!!!!!!!!!!!!!!!!!!!!!!!"
    pl.plot(cpu, 'r')
    pl.plot(mem, 'g')

    pl.title('performance')
    pl.xlabel('second')
    pl.ylabel('percent')

    pl.plot(cpu, color="red", linewidth=2.5, linestyle="-", label="cpu")
    pl.plot(mem, color="blue", linewidth=2.5, linestyle="-", label="mem")
    pl.legend(loc='upper left')
    pl.xlim(0.0, len(mem))   # 设置最大值范围
    pl.ylim(0.0, 100.0)
    pl.savefig(path)
    # print path
    # pl.show() #调出GUI实时查看
    pl.close()  # 必须关闭,不然值会在内存中不销毁

def get_cpu_men():
    """
    获取txt文件的cpu men，调用pylab生成性能线图
    :return 图片文件生成路径
    """
    # print "exec get_cpu_men!!!!!!!!!!!!!!!!!!!!!!!!"
    cpu_list = [0]
    men_list = [0]
    image_path = create_file(type=1)
    cpu_men_info_path = create_file(type=2)
    time.sleep(1)
    # print "wanto get sucessfully!"
    read_txt = open(cpu_men_info_path, 'r')
    s_cpu_men = read_txt.read().strip(' ').rstrip(',').split(',')
    read_txt.close()
    for i in range(1, len(s_cpu_men), 2):
        cpu_list.append(int(s_cpu_men[i]))
    for i in range(0, len(s_cpu_men), 2):
        men_list.append(int(s_cpu_men[i]))
    # data_marker(cpu_list, men_list, create_file(type=1))
    data_marker(cpu_list, men_list, image_path)
    print flag+image_path   #用于生成图片路径

    if os.path.exists(cpu_men_info_path):  # 读写完成，删除文件
        time.sleep(1)   #防止异步延迟
        os.remove(cpu_men_info_path)
    # return image_path