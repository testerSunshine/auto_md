import time
import os
import re
from datetime import datetime

def recodeInfo(info):
    now_time = str(datetime.now().strftime('%Y-%m-%d-%H-%M-%S')).split(' ')[0]
    fpath = os.path.join(os.getcwd(), now_time)
    fp = fpath + '.txt'
    print fp
    with open(fp, 'a') as f:
        # if
        if isinstance(info,list):
            for i in info:
                f.writelines(i)
                # f.writelines(i)
        elif isinstance(info,str):
            f.writelines(info)
        else:
            f.writelines(type(info))
def recodeStartTime(info):
    s = info[0]
    # s = r"<p class='attribute'><strong>Start Time:</strong> 2016-12-01 10:16:59</p>"
    st = re.search(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", s).group()
    try:
        st = datetime.strptime(st, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d-%H-%M-%S")
    except:
        st = "None"
    #print st
    recodeInfo(st)
#recodeStartTime("dd")
# def recodeInfo(now_time):
#     with open(os.path(os.getcwd(),""))