#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-
__author__ = 'Aaron_chan'


import requests
from bs4 import BeautifulSoup

# url = 'http://list.iqiyi.com/www/1/----------2---11-1-1-iqiyi--.html'

# r = requests.get(url)
# html = r.text
# ob = BeautifulSoup(html, 'html5lib')
# vips = ob.select('a[rseat="bigTitle"]')
# for v in vips:
#     print(v.text)

# print(r.text)
def get_iqiyi_vip():
    pn = 31
    for i in range(1, pn):
        print('成功爬取第%d页全部电影名' % i)
        url = 'http://list.iqiyi.com/www/1/----------2---11-%d-1-iqiyi--.html' % i
        r = requests.get(url)
        html = r.text
        ob = BeautifulSoup(html, 'html5lib')
        vips = ob.select('a[rseat="bigTitle"]')
        for v in vips:
            with open('vip.txt', 'a') as f:
                f.writelines(v.text + '\n')


get_iqiyi_vip()