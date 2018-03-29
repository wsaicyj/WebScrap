#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-
__author__ = 'Aaron_chan'

import requests
from bs4 import BeautifulSoup

url = 'http://www.biqiuge.com/book/4772/'

r = requests.get(url)
html_contents = r.text.encode('ISO8859-1').decode('gbk')
# print(html_contents)
ob = BeautifulSoup(html_contents, 'html5lib')
# print(ob.findAll('dd'))
contents = ob.findAll('dd')
for content in contents:
    print(content.text)
    # text = content.text
    # href = content.a.get('href')
    # print('%s:%s' % (text,url+href))
    # print(type(content.text))