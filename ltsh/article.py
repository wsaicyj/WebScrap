#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-
__author__ = 'Aaron_chan'


import requests
from bs4 import BeautifulSoup
import re


url = "http://home.gdzjdaily.com.cn/local/2016/07/2016-07-1460596.html"
html = requests.get(url)
# c_html = html.text.encode('ISO8859-1').decode('utf-8')
html_content = html.content.decode('utf-8')
# print(html.encoding)
# ob = BeautifulSoup(c_html, 'html5lib')
ob = BeautifulSoup(html_content, 'html5lib')
# head_tag = ob.head
# for child in head_tag.descandants:
#     print(child)
# print(head_tag)
# print(type(head_tag))
# print(head_tag.contents)
# print(ob.h1)
# print(ob.findAll('span', {'style': re.compile(".*")}))
# contents = ob.findAll(class_='article_cont')
# contents = ob.find_all(class_='article_cont')
# print(contents)
# contents = ob.findAll('span', {'style': re.compile(".*")})
# print(contents)
# for content in contents:
    # print(content)
    # print(type(content))
    # print(content.attrs)
    # print(content.string)
    # print(content.name)
    # print(content['style'])

# for content in contents:
#     print(content.text)
# print(ob.p.span)
# print(ob.findAll('p', {'class': 'MsoNormal'}))
# print(ob.findAll(text='宋体'))
# print(ob.find_all('span', style_='FONT-FAMILY'))
# print(ob.find_all('p', class_='MsoNormal'))
# contents = ob.find_all('p', class_='MsoNormal')
# print(contents)
# for content in contents:
#    for string in content.stripped_strings:
#        print(string)