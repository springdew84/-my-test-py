#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import pymysql
import sys


reload(sys)
sys.setdefaultencoding('utf-8')


# 打开数据库连接
def connect_prod_db():
    return pymysql.connect(host='13.57.129.69',
                           port=3306,
                           user='cdoffice',
                           password='bookface06',
                           database='ugc',
                           charset='utf8')


def start():
    with open('result.txt', 'w') as f:
        for page_num in range(100):
            sql_str = ("select d.id,d.title,"
            "type," 
            "case type when 'local' then 'local折扣' when 'local_guide' then 'local攻略' when 'deal' then 'national折扣' when 'local_activity' then '支付活动' when 'guide' then '文章'  when 'post' then '晒货' else '' End as '类型说明',"
            "status,"
            "case status when 'prepublished' then '待发布' when 'published' then '发布' when 'hidden' then '隐藏' when 'cancel' then '取消' else status End as '状态说明',"
            "e.uname,"
            "d.relate_id,"
            "case d.is_expiration when 1 then '是' else '否' end,"
            "case `type`" 
            "when 'local' then concat('https://www.dealmoon.com/localdeals/',d.`id`,'.html') " 
            "when 'deal' then concat('https://www.dealmoon.com/cn/',d.`relate_id`,'.html') " 
            "when 'local_guide' then concat('https://www.dealmoon.com/localdeals/',d.`id`,'.html') " 
            "when 'local_activity' then concat('https://www.dealmoon.com/localdeals/',d.`id`,'.html') " 
            "when 'guide' then concat('https://www.dealmoon.com/localdeals/',d.`id`,'.html') " 
            "when 'post' then concat('https://www.dealmoon.com/localdeals/',d.`id`,'.html') " 
            "else '' end " 
            "from ugc.local_deal d left join dealmoon.editor e on d.last_editor_id=e.id "
            "where "
            "type in('local','local_guide','deal','local_activity','guide','post') "
            "order by d.id limit  " + str(page_num * 200) + ",200")

            prod_con = connect_prod_db()

            cur = prod_con.cursor()
            cur.execute(sql_str)
            rows = cur.fetchall()
            cur.close()
            prod_con.close()

            count = len(rows)
            print("row_num:" + str(page_num) + ",size:" + str(count))

            if count == 0:
                print("no data")
                break
            else:
                for i in range(count):
                    f.write(str(rows[i][0]) + "	" + str(rows[i][1]) + "	"
                            + str(rows[i][2]) + "	" + str(rows[i][3]) + "	"
                            + str(rows[i][4]) + "	" + str(rows[i][5]) + "	"
                            + str(rows[i][6]) + "	" + str(rows[i][7]) + "	"
                            + str(rows[i][8]) + "	" + str(rows[i][9]))
                    f.write('\n')


start()
