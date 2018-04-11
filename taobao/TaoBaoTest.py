#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-
__author__ = 'Aaron_chan'


from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


url = 'https://item.taobao.com/item.htm?spm=a219r.lm874.14.1.2c7a6dbcfWaDFy&id=523839458288&ns=1&abbucket=9'


def wd_js():
    wd = webdriver.PhantomJS()
    wd.get(url)
    html = wd.page_source
    print(html)
    ob = BeautifulSoup(html, 'html5lib')
    pics = ob.select('img[align="absmiddle"]')
    for pic in pics:
        print(pic.attrs['src'])
        print(pic)
        print(pic.attrs['data-ks-lazyload'])
        print(pic)


def wd_driver():
    wd = webdriver.Chrome()
    wd.get(url)
    pics = wd.find_elements_by_css_selector('img[align="absmiddle"]')
    for pic in pics:
        print(pic.get_attribute('data-ks-lazyload'))
    # print(pics)
    wd.quit()

def wd_htmlunit():
    wd = webdriver.Remote(command_executor="http://127.0.0.1:4446/wd/hub", desired_capabilities=DesiredCapabilities.HTMLUNIT)
    wd.get(url)
    pics = wd.find_elements_by_css_selector('img[align="absmiddle"]')
    for pic in pics:
        print(pic.get_attribute('data-ks-lazyload'))


wd_htmlunit()
# wd_driver()