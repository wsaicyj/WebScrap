#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-
__author__ = 'Aaron_chan'


import pymysql

# conn = pymysql.connect(host='192.168.3.123', user='root', password='root', db='ltsh', charset='utf8')
# cur = conn.cursor()
# cur.execute("Use ltsh")
# cur.execute("select * from cms_category")
# print(type(cur.fetchall()))
# cur.close()
# conn.close()

def conn(host, user, pwd, db, charset):
    conn = pymysql.connect(host=host, user=user, password=pwd, db=db, charset=charset)
    return conn

def select(conn):
    cur = conn.cursor()
    cur.execute("Use ltsh")
    cur.execute("select * from cms_category")
    # print(type(cur.fetchall()))
    print(cur.fetchall())
    cur.close()


def conn_close(conn):
    conn.close()

conn = conn('192.168.3.123', 'root', 'root', 'ltsh', 'utf8')
select(conn)
conn_close(conn)
