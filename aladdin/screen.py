#!/usr/local/bin/python3
# Filename: screen.py
# -*- coding: utf-8 -*-

import urllib.request
import urllib.parse
import json
import time
import os

# 访问数据事件Screen链接
event_paras_details_list = 'http://betaapi.aldwx.com//Main/action/Event/Event/event_paras_details_list'
# 查询的日期
date = '2019-06-28'
# 每页返回数据数量
pageSize = 40

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'passport.lianjia.com',
    'Pragma': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36'
}

form_data = {

}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'http://tongji.aldwx.com',
    'Pragma': 'no-cache',
    'Referer': 'http://tongji.aldwx.com/publice/incid-analy/incid-deta?evName=screenEvent&key=default&value=default&model=%E5%85%A8%E9%83%A8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Upgrade-Insecure-Requests': '1',
    'X-Requested-With': 'XMLHttpRequest',
}

# 写新的文件
form_data.__setitem__("date", date + "~" + date)

dirName = "data/" + time.strftime("%Y%m%d%H", time.localtime())
if os.path.exists(dirName):
    print("dir [" + dirName + "] exists")
else:
    os.mkdir(dirName)
    print("mkdir [" + dirName + "] success")

with open(dirName + "/" + date + '.txt', 'w') as f:
    for pageIndex in range(1, 50):
        form_data.__setitem__("currentPage", pageIndex)
        data = urllib.parse.urlencode(form_data).encode(encoding='utf-8')
        request = urllib.request.Request(event_paras_details_list, data=data, headers=headers)
        response = urllib.request.urlopen(request)

        jsonStr = response.read().decode('utf-8')

        jsonObj = json.loads(jsonStr)

        assert len(jsonObj) == 4

        print("get page:" + str(pageIndex) + ",page size:" + str(len(jsonObj['data'])) + ",count:" + str(jsonObj['count']))

        for i in range(len(jsonObj['data'])):
                f.write(jsonObj['data'][i]['ev_paras_value'].replace(" ", "$$") + "	" + jsonObj['data'][i]['ev_paras_count'] + "	" + jsonObj['data'][i]['ev_paras_uv'])
                f.write('\n')
        if len(jsonObj['data']) < 40:
            break
        else:
            pageIndex = pageIndex + 1
            time.sleep(1)
print("get screen success")
