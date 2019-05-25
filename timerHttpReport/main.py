#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib
import threading

data = ['2018-11-17', '2018-11-18', '2018-11-20', '2018-11-22', '2018-11-23', '2018-11-28', '2018-11-29', '2018-12-01']
url = 'https://biz.dealmoon.com/api/mall/v1/data-center/stats-task/ga-metrics-day-pull/'
count = data.__len__()

target = str(url) + data[0]
req = urllib.request.urlopen(target)
print(req)

# def fun_timer():
#     global index
#     index = 0
#     print('hello timer' + data[index])   #打印输出
#     target = str(url) + date
#
#     global timer  #定义变量
#     timer = threading.Timer(3, fun_timer)   #60秒调用一次函数
#     #定时器构造函数主要有2个参数，第一个参数为时间，第二个参数为函数名
#     timer.start()    #启用定时器
#
# timer = threading.Timer(1, fun_timer)  # 首次启动
# timer.start()

# for date in data:
#     print(str(index) + ':' + str(url) + date)
#     target = str(url) + date
#     # req = urllib.request.urlopen(index)
#     print(target)
#     print('\n')
#     index = index+1


