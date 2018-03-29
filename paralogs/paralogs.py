#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-
__author__ = 'Aaron_chan'

import pymysql, datetime

f = open('haima.access-2017-12-12.log')
res = {}
for l in f:
    arr = l.split(' ')
    # print(arr)
    ip = arr[0]
    url = arr[6]
    status = arr[8]
    #ip、status、url当key，每次统计+1
    res[(ip, url, status)] = res.get((ip, url, status), 0) + 1
    # print(res[(ip, url, status)])
f.close()
# print(res)

#生成临时的list
res_list = [(k[0], k[1], k[2], v) for k, v in res.items()]
# print(res_list)
# for s in res_list:
#     print(s[0], s[1], s[2], s[3])


# print(datetime.datetime.utcnow())

#按照统计数量排序，打印前10
# for k in sorted(res_list, key=lambda x: x[3], reverse=True)[:10]:
#     print(k)

host = '192.168.3.123'
user = 'root'
pwd = 'root'
db = 'myapp'
charset = 'utf8'


# conn = pymysql.connect(host=host, user=user, password=pwd, db=db, charset=charset)
# conn.autocommit(True)
# cur = conn.cursor()
# cur.execute("Use myapp")
# for s in res_list:
#     sql = 'insert logs_analysis_log values (%s, "%s","%s",%s,%s )' % (1, s)
#     try:
#         cur.execute(sql)
#     except Exception as e:
#         print(e)
# cur.close()
