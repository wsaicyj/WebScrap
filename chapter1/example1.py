#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-
__author__ = 'Aaron_chan'

from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError

# html = urlopen("http://www.zjfgj.cn/bit-xxzs/xmlpzs/webissue.asp")
# html = urlopen("http://pythonscraping.com/pages/page1.html")
# html = urlopen("http://www.baidu.com")
# html = urlopen("http://zd.diyifanwen.com/zidian/bh/8.htm")
# bsOjbect = BeautifulSoup(html.read(), 'lxml')
# print(bsOjbect.h1)
# print(bsOjbect.title)

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        bsOjbect = BeautifulSoup(html.read(), 'lxml')
        title = bsOjbect.body.h1
    except AttributeError as e:
        print(e)
        return None
    return title

url = "http://pythonscraping.com/pages/page1.html"
title = getTitle(url)
if title == None:
    print("Title could not found")
else:
    print(title)