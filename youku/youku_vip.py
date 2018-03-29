#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-
__author__ = 'Aaron_chan'


import requests, json


def get_youku_vip(url):
    '''获取VIP电影名'''
    r = requests.get(url)
    html = r.text.encode('utf-8').decode('unicode_escape')
    vip = json.loads(html)
    # print(vip)
    sn = vip['result']['result']
    # print(sn)
    for s in sn:
        with open('vip.txt', 'a') as f:
            f.writelines(s['showname'] + '\n')


# url = 'https://vip.youku.com/ajax/filter/filter_data?tag=10005&pl=30&pt=1&ar=0&mg=0&y=0&cl=1&o=3&pn=20'
# get_youku_vip(url)

page = 79
for i in range(1, page):
    try:
        print('成功爬取第%d页全部电影名' % i)
        url = 'https://vip.youku.com/ajax/filter/filter_data?tag=10005&pl=30&pt=1&ar=0&mg=0&y=0&cl=1&o=3&pn=%d' % i
        get_youku_vip(url)
    except json.decoder.JSONDecodeError:
        continue

