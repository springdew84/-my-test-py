#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.0 Chrome/30.0.1599.101 Safari/537.36',
'Connection': 'keep-alive'
}
row_num = 0
client = requests.session()

with open('data.txt', 'r') as f:
    for line in f:
        row_num = row_num + 1
        try:
            url = line.replace("https", "http")
            url = url[0:len(url) - 1]
            if row_num % 2 == 0:
                url = url.replace(".webp", "")
                if row_num % 6 == 0:
                    url = url + '?from=pre_resize'
            # url = url.replace("http://imgcache.dealmoon.com", "http://img.it6.dealmoon.net")
            url = url.replace("http://imgcache.dealmoon.com", "http://118.31.171.76:8084")
            logging.info(str(row_num) + ': url->' + url)
            url = url.strip("")
            r = client.get(url, headers=headers)
            logging.info("->status:" + str(r.status_code))
            #time.sleep(3)
        except Exception as e:
            logging.exception('error', e)
