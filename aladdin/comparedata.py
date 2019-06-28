#!/usr/local/bin/python3
# Filename: comparedata.py
# -*- coding: utf-8 -*-

import os

date = "2019-06-28"
dirList = os.listdir(os.getcwd() + "/data")

for i in range(len(dirList)-1):
    file1path = "data/" + dirList[i] + "/" + date + ".txt"
    file1 = open(file1path)
    for j in range(i+1, len(dirList)):
        file2Path = "data/" + dirList[j] + "/" + date + ".txt"
        file2 = open(file2Path)

        print("-----[" + file1path + "] VS [" + file2Path + "]-----")
        for row1 in file1:
            row1 = row1.strip('\n')
            row1Array = row1.split()

            screen_exist = False
            for row2 in file2:
                row2 = row2.strip('\n')
                row2Array = row2.split()

                if row1Array[0] == row2Array[0]:
                    screen_exist = True

                    if int(row1Array[1]) > int(row2Array[1]):
                        print("screen:" + row1Array[0] + " pv missing")

                    if int(row1Array[2]) > int(row2Array[2]):
                        print("screen:" + row1Array[0] + " uv missing")
                    break

            if not screen_exist:
                print("screen:" + row1Array[0] + " is not exist, file:" + file2Path)


