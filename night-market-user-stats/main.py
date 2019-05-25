#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import jieba
import difflib

class Row:
    rownum = 0  #行号
    data = ''  #行数据
    coupons = ''
    vouchers = ''

    def __init__(self, rownum, data):
        self.rownum = rownum
        self.data = data

    def detail(self):
        print("rownum:" + str(self.rownum) + " data:" + self.data + " coupons:" + self.coupons
              + " vouchers:" + self.vouchers)


class CompaleRow:
    data = ''  # 行数据
    id = ''
    businessIds = ''

    def __init__(self, rownum, data, id, businessIds):
        self.rownum = rownum
        self.id = id
        self.businessIds = businessIds
        self.data = data

    def detail(self):
        print("rownum:" + str(self.rownum) + " data:" + self.data + " id:" + self.id + " businessIds:" + self.businessIds)


#读取文本文件
file = open("data.txt")
file_local = open("local.txt")
file_voucher = open("user.txt")
index = 1
data = []
data_local = []
data_voucher = []

for line in file:
    line = line.strip('\n')
    row = Row(index, line)
    data.append(row)
    #row.detail()
    index = index + 1
file.close()

index = 1
for line in file_local:
    line = line.strip('\n')
    rowDataArray = line.split()
    row = CompaleRow(index, line, rowDataArray[1], rowDataArray[2])
    data_local.append(row)
    index = index + 1
file.close()

index = 1
for line in file_voucher:
    line = line.strip('\n')
    rowDataArray = line.split()
    row = CompaleRow(index, line, rowDataArray[1], rowDataArray[2])
    data_voucher.append(row)
    index = index + 1
file.close()

count = data.__len__()
count_local = data_local.__len__()
count_voucher = data_voucher.__len__()

for i in range(count):
    lineDataArray = data[i].data.split()
    businessId = lineDataArray[0]

    for j in range(count_local):
        if data_local[j].businessIds.find("," + businessId + ",") != -1:
            data[i].coupons = data[i].coupons + data_local[j].id + ","

    if data[i].coupons != '':
        data[i].coupons = data[i].coupons.rstrip(",")

    for k in range(count_voucher):
        if data_voucher[k].businessIds.find("," + businessId + ",") != -1:
            data[i].vouchers = data[i].vouchers + data_voucher[k].id + ","

    if data[i].vouchers != '':
        data[i].vouchers = data[i].vouchers.rstrip(",")

    data[i].detail()

#写新的文件
with open('result.txt', 'w') as f:
    for i in range(count):
        f.write(data[i].data + "	" + str(data[i].coupons) + "	" + str(data[i].vouchers))
        f.write('\n')
