#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
import logging
import time

kv = {'user_agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163',
      'Connection': 'keep-alive'}
row_num = 0
data = []
with open('data.txt', 'r') as f:
    for line in f:
        data.append(line)
f.close()

data.reverse()
row_num = data.__len__()
for line in data:
    try:
        url = line.replace("https", "http")
        # url = line.replace("https://imgcache.dealmoon.com", "http://localhost:8084")
        url = url[0:len(url) - 1]
        print(str(row_num) + ':' + "start open: " + url)
        url = url.strip("")
        request = urllib.request.Request(url, headers=kv)
        response = urllib.request.urlopen(request, data=None, timeout=10)
        print("->status:" + str(response.status))
        # time.sleep(1)
        row_num = row_num - 1
    except Exception as e:
        logging.exception('error', e)
