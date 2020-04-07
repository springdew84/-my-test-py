#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#import xlrd
import jieba
import difflib

#通过xlrd读取excel

# data = xlrd.open_workbook('test.xlsx')
# table = data.sheets()[0] # 打开第一张表
# nrows = table.nrows      # 获取表的行数
# for i in range(nrows):   # 循环逐行打印
#     if i == 0 or i == 1: # 跳过第一行
#         continue
#     print(table.row_values(i)[:6]) # 取前6列

class Row:
    rownum = 0  #行号
    data = ''  #行数据
    terms = []  #词项
    key = ''  #关键字
    flag = False #标记
    city = ''
    hasFamily = 0
    groupId = 0
    ratio = 0.0

    def __init__(self, rownum, data, terms, key, flag, city):
        self.rownum = rownum
        self.data = data
        self.terms = terms
        self.key = key
        self.flag = flag
        self.city = city

    def detail(self):
        print("rownum:" + str(self.rownum) + " data:" + self.data + " terms:" + str(self.terms) + " key:"
              + self.key + " flag:" + str(self.flag))

#读取文本文件
file = open("test.txt")
index = 1
data = []
#过滤掉的关键字
key_filter = {"菜系", "菜", "店", "餐", "吧", "料理", "食品"}
citySet = set() #城市

for line in file:
    line = line.strip('\n')
    lineDataArray = line.split()
    categoryName = lineDataArray[5]
    citySet.add(lineDataArray[1])

    for k in key_filter:
        categoryName = categoryName.replace(k, "")

    #分词
    term = jieba.cut(categoryName, cut_all=True, HMM=True)

    row = Row(index, line, list(term), categoryName, False, lineDataArray[1])
    data.append(row)
    row.detail()

    index = index + 1
file.close()

count = data.__len__()
groupId = 0

# difflib相似度分析
for cityName in citySet:
    for i in range(count):
        if data[i].flag or cityName != data[i].city:
            continue
        else:
            groupId = groupId + 1
            data[i].groupId = groupId
            data[i].ratio = 2.0
            for j in range((i+1), count):
                if data[j].flag or cityName != data[j].city:
                    continue
                else:
                    seq = difflib.SequenceMatcher(None, data[i].key, data[j].key)
                    ratio = round(seq.ratio(), 2)
                    if ratio > 0:
                        data[i].detail()
                        data[j].detail()

                        print("groupId:" + str(groupId) + " city:" + data[i].city + " ratio:" + str(ratio) + " " + data[i].key + " vs " + data[j].key)

                        data[j].flag = True
                        data[j].groupId = groupId
                        data[j].ratio = ratio
                        #有相似的分类
                        data[i].hasFamily = 1
                        data[j].hasFamily = 1

#写新的文件
with open('r.txt', 'w') as f:
    for i in range(count):
        f.write(data[i].data + "	" + str(data[i].groupId) + "	" + str(data[i].hasFamily) + "	" + str(data[i].ratio))
        f.write('\n')
