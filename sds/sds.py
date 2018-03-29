#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-
__author__ = 'Aaron_chan'


'''六度分隔理论'''

from bs4 import BeautifulSoup
import requests, re
import random, datetime

url = 'https://en.wikipedia.org'

# html = requests.get(url)
# ob = BeautifulSoup(html.text, 'html5lib')
#
# for link in ob.find('div', {"id": "bodyContent"}).findAll('a', href=re.compile("^(/wiki/)((?!:).)*$")):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])

random.seed(datetime.datetime.now())
def getLinks(articlUrl):
    html = requests.get(url + articlUrl)
    ob = BeautifulSoup(html.text, 'html5lib')
    return ob.find('div', {"id": "bodyContent"}).findAll('a', href=re.compile("^(/wiki/)((?!:).)*$"))


article_url = '/wiki/Kevin_Bacon'
links = getLinks(article_url)
# num = len(links)
# print(links)
while len(links) > 0:
    new_article = links[random.randint(0, len(links)-1)].attrs['href']
    print(new_article)
    # num -= 1
    links = getLinks(new_article)
    # print(links)