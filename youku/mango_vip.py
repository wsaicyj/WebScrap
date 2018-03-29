#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-
__author__ = 'Aaron_chan'


import requests
from bs4 import BeautifulSoup

def get_mango_vip(url):

    '''获取芒果TV VIP免费电影名'''

    pn = 14

    for i in range(1, pn):
        # url = url % i
        r = requests.get(url % i)

        html = r.text
        ob = BeautifulSoup(html, 'html5lib')
        contents = ob.select('a.u-title')

        for c in contents:
            try:
                with open('vip.txt', 'a') as f:
                    f.writelines(c.text + '\n')
            except UnicodeEncodeError:
                continue

        print('成功爬取第%d页全部电影名' % i)





vip_b2 = 'https://list.mgtv.com/3/a4-a3-------2835073-2-%d--b2-.html?channelId=3'     #vip免费
vip_b3 = 'https://list.mgtv.com/3/a4-a3-------2835073-2-%d--b3-.html?channelId=3'     #vip用券
vip_b4 = 'https://list.mgtv.com/3/a4-a3-------2835073-2-%d--b4-.html?channelId=3'     #vip点播

get_mango_vip(vip_b2)
get_mango_vip(vip_b3)
get_mango_vip(vip_b4)
