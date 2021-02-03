#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
import logging
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
kv = {'user_agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163',
      'Connection': 'keep-alive'}
row_num = 0

logging.info("start test.......")

with open('image-service-test-case.txt', 'r') as f:
    for line in f:
        row_num = row_num + 1
        try:
            url = line.replace("https", "http")
            url = url[0:len(url) - 1]
            if row_num % 2 == 0:
                logging.info(str(row_num) + ': url->' + url)
                url = url.strip("")
                request = urllib.request.Request(url, headers=kv)
                response = urllib.request.urlopen(request, data=None, timeout=600)
                logging.info("->status:" + str(response.status))
        except Exception as e:
            logging.exception('error', e)

logging.info("end test.......")
