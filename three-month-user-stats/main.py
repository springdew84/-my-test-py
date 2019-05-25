#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql

result_data = []

# 打开数据库连接
def connect_prod_db():
    return pymysql.connect(host='184.169.240.38',
                           port=3306,
                           user='cdoffice',
                           password='dbookface06',
                           database='ddm_ucenter',
                           charset='utf8')


def connect_st1_db():
    return pymysql.connect(host='47.88.59.171',
                           port=3306,
                           user='ddm',
                           password='dbookface06',
                           database='ddiscover',
                           charset='utf8')



class User:
    user_id = ''
    user_name = ''
    email = ''
    city = ''
    create_time = ''

    def __init__(self, user_id, user_name, email, city, create_time):
        self.user_id = user_id
        self.user_name = user_name
        self.email = email
        self.city = city
        self.create_time = create_time

    def detail(self):
        print("user_id:" + str(self.user_id) + ",user_name:" + str(self.user_name) +
              ",email:" + str(self.email) + ",city:" + str(self.city) + ",create_time:" + str(self.create_time))

def query_user(user_ids):
    sql_str = ("SELECT `ID`, `NAME`, `EMAIL`, FROM_UNIXTIME(CREATE_TIME,'%%Y-%%m-%%d') "
               "FROM user WHERE id in (%s)" % user_ids)

    prod_con = connect_prod_db()

    cur = prod_con.cursor()
    cur.execute(sql_str)
    rows = cur.fetchall()
    cur.close()
    prod_con.close()

    count = len(rows)

    #print("query data size:" + str(count))

    data = []

    for i in range(count):
        temp_user = User(rows[i][0], rows[i][1], rows[i][2], "", rows[i][3])
        data.append(temp_user)

    return data

def start():
    with open('result.txt', 'w') as f:

        for row_num in range(157):
            if row_num < 63:
                continue

            sql_str = ("select user_id,city from local_visit_user_temp order by user_id limit " + str(row_num*500) + ",500")

            prod_con = connect_st1_db()

            cur = prod_con.cursor()
            cur.execute(sql_str)
            rows = cur.fetchall()
            cur.close()
            prod_con.close()

            count = len(rows)
            print("row_num:" + str(row_num) + ",size:" + str(count))

            if count == 0:
                print("no data")
                break
            else:
                user_ids = ''
                for i in range(count):
                    if user_ids == '':
                        user_ids = str(rows[i][0])
                    else:
                        user_ids = user_ids + "," + str(rows[i][0])

                print("userIds:" + user_ids)
                user_array = query_user(user_ids)

                for i in range(count):
                    for j in range(len(user_array)):
                        if rows[i][0] == user_array[j].user_id:
                            user_array[j].city = rows[i][1]
                            result_data.append(user_array[j])

                            f.write(str(user_array[j].user_id) + "	" + str(user_array[j].user_name) + "	"
                                    + str(user_array[j].email) + "	" + str(user_array[j].city) + "	"
                                    + str(user_array[j].create_time))
                            f.write('\n')
                            break


start()