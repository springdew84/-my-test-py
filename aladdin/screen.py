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
date_list = ['2019-06-27', '2019-06-28', '2019-06-29', '2019-06-30', '2019-07-01']
# 每页返回数据数量
page_size = 40

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
    'ev_paras_name': 'screenName',
    'date': '1',
    'event_key': '570689a10947285271dd6d929836eeda',
    'currentPage': 1,
    'total': page_size,
    'prop': '',
    'order': '',
    'token': 'CJPsLYJYFXYReWlsZhI0s5zCFDIFGhHnLBzYLWGPK44ZMZTf%2BmW9Cf8GwSjnveBbUbXiqlqtXmFqXiM9g4Jz6TOSePVg%2B1bxq4tJzM8f%2FL7WLn8QAPJMcj9eIW%2BZSZWzWuXTY3%2BpzCU2DDqn2mLmQRvg6HzcvvybG%2FGPIYqk%2BmbWpjpkoCKtS%2FTNcqltjPk7AbbCz3%2BkxWFOQZE8C6t%2F%2FSsQ77I4Es5CaFrAoqdmAJI%3D',
    'app_key': '950d22e7df9e789fe673540daea89c54',
    'is_demo': 0
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


def get_data(dir_name, date_str, form):
    form.__setitem__("date", date_str + "~" + date_str)

    file_name = dir_name + "/" + date_str + '.txt';
    print(">>>open file:" + file_name)
    f = open(file_name, 'w')

    for page_index in range(1, 50):
        form.__setitem__("currentPage", page_index)
        data = urllib.parse.urlencode(form).encode(encoding='utf-8')
        request = urllib.request.Request(event_paras_details_list, data=data, headers=headers)
        response = urllib.request.urlopen(request)

        json_str = response.read().decode('utf-8')

        json_obj = json.loads(json_str)

        assert len(json_obj) == 4

        print("get page:" + str(page_index) + ",page size:" + str(len(json_obj['data'])) + ",count:" + str(json_obj['count']))

        for i in range(len(json_obj['data'])):
                f.write(json_obj['data'][i]['ev_paras_value'].replace(" ", "$$") + "	" + json_obj['data'][i]['ev_paras_count'] + "	" + json_obj['data'][i]['ev_paras_uv'])
                f.write('\n')
        if len(json_obj['data']) < page_size:
            break
        else:
            time.sleep(1)

    f.close()


def get_dir():
    dir_name = "data/" + time.strftime("%Y%m%d%H", time.localtime())
    if os.path.exists(dir_name):
        print("dir [" + dir_name + "] exists")
    else:
        os.mkdir(dir_name)
        print("mkdir [" + dir_name + "] success")
    return dir_name


if __name__ == "__main__":
    path_name = get_dir()

    for date in date_list:
        print(">>>start pull, date:" + date)
        get_data(path_name, date, form_data)

    print(">>>get screen success")
