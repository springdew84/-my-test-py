#!/usr/local/bin/python3
# Filename: comparedata.py
# -*- coding: utf-8 -*-

import os


class Row:
    page_name = ''
    pv = ''
    uv = ''

    def __init__(self, page_name, pv, uv):
        self.page_name = page_name
        self.pv = pv
        self.uv = uv


date = "2019-06-29"
dirList = os.listdir(os.getcwd() + "/data")

for i in range(len(dirList)-1):
    file1path = "data/" + dirList[i] + "/" + date + ".txt"
    if not os.path.exists(file1path):
        continue
    file1 = open(file1path)
    for j in range(i+1, len(dirList)):
        file2Path = "data/" + dirList[j] + "/" + date + ".txt"
        file2 = open(file2Path)
        file2Rows = []
        for row2 in file2:
            row2 = row2.strip('\n')
            row2Array = row2.split("	")
            file2Rows.append(Row(row2Array[0], row2Array[1], row2Array[2]))

        print("-----[" + file1path + "] VS [" + file2Path + "]-----")

        for row1 in file1:
            row1 = row1.strip('\n')
            row1Array = row1.split("	")

            screen_exist = False
            for k in range(0, len(file2Rows)):

                if row1Array[0] == file2Rows[k].page_name:
                    screen_exist = True

                    if int(row1Array[1]) > int(file2Rows[k].pv):
                        print("screen:" + row1Array[0] + " pv missing")

                    if int(row1Array[2]) > int(file2Rows[k].uv):
                        print("screen:" + row1Array[0] + " uv missing")
                    break

            if not screen_exist:
                print("screen:" + row1Array[0] + " is not exist, file:" + file2Path)

