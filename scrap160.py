#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-
__author__ = 'Aaron_chan'

import requests, sys


url = 'https://www.91160.com/dep/show/depid-100000995.html'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'}
r = requests.get(url, headers=headers)
# print(r.content.decode('utf-8'))
print(sys.path)