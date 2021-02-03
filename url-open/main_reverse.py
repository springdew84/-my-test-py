#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
import logging
import time
#logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

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

for r in range(0, row_num):
    try:
        # print(row_num-r)
        line = data[r]
        url = line.replace("https", "http")
        # url = line.replace("https://imgcache.dealmoon.com", "http://localhost:8084")
        url = url[0:len(url) - 1]
        url = url.strip("")
        # url = url.replace("http://imgcache.dealmoon.com", "http://img.it6.dealmoon.net")
        url = url.replace("http://imgcache.dealmoon.com", "http://118.31.171.76:8084")
        logging.info(str(row_num-r) + '/' + str(r) + '/' + str(row_num) + ': url->' + url)
        request = urllib.request.Request(url, headers=kv)
        response = urllib.request.urlopen(request, data=None, timeout=90)
        logging.info("->status:" + str(response.status))
        #time.sleep(2)
    except Exception as e:
        logging.exception('error', e)
