#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-
__author__ = 'Aaron_chan'

from urllib.request import urlopen, HTTPError
from bs4 import BeautifulSoup
import re
import requests
from selenium import webdriver
import time



# try:
#     html = urlopen("http://zd.diyifanwen.com/zidian/bh/8.htm")
# except HTTPError as e:
#     print(e)
# else:
# # print(html.read())
#     ob = BeautifulSoup(html.read(), 'lxml')
#     # print(ob.a)
#     # print(ob.nonExistent.div)
#     worlds = ob.findAll('a', {'href': re.compile(r'http://zd.diyifanwen.com/zidian/[A-Z]/*.htm')})
#     for world in worlds:
#         print(world.text)
# url = "http://zd.diyifanwen.com/zidian/bh/8.htm"
url = "http://www.newhealth.com.cn/"
# html = urlopen(url)
# ob = BeautifulSoup(html, 'lxml')
# dl = ob.findAll('div', id="wordlistbox")
# print(dl)
# print(words)
# print(a_set)
# ob = BeautifulSoup(s, 'lxml')
# print(s)
# print(ob)

def selenium_scrap(url):
    stat_time = time.time()
    wd = webdriver.PhantomJS()
    wd.get(url)
    s = wd.page_source
    words = wd.find_elements_by_css_selector('a[href*="http://zd.diyifanwen.com/zidian/"]')
    a_set = set()
    for word in words:
        # print(word.text)
        if not word.text.isnumeric() and len(word.text) == 1:
            a_set.add(word.text)
            # with open('banihua.txt', 'a', encoding='utf-8') as f:
            #     f.write(word.text)
    end_time = time.time()
    runtime = end_time - stat_time
    print('耗时%s秒' % runtime)
    return a_set


def bs4_srcap(url):
    # html = urlopen(url)
    html = requests.get(url)
    # ob = BeautifulSoup(html.read(), 'lxml')
    # ob = BeautifulSoup(html.text, 'lxml')
    # print(html.text.encode('gbk').decode('gb2312'))
    # print(ob)
    # print(type(html.read()))
    print(type(html.text))


# print(selenium_scrap(url))
bs4_srcap(url)