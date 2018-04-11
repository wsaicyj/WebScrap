#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-
__author__ = 'Aaron_chan'


import requests, re


# url = 'https://search.bilibili.com/api/search?search_type=video&keyword=%E6%B5%B7%E9%B2%9C&from_source=banner_search&order=totalrank&duration=1&tids=0&page=1'
url = u'https://search.bilibili.com/api/search?search_type=video&keyword=海鲜&from_source=banner_search&order=totalrank&duration=1&tids=0&page=1'
r = requests.get(url)

html = r.text

pattern = re.compile(r'"id":(\d+)')
ids = pattern.findall(html)
print(ids)