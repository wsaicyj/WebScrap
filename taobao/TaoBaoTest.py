#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-
__author__ = 'Aaron_chan'


from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from urllib import request
import os


#url = 'https://item.taobao.com/item.htm?spm=a219r.lm874.14.1.2c7a6dbcfWaDFy&id=523839458288&ns=1&abbucket=9'
url = 'https://item.taobao.com/item.htm?id=546332193454&ali_refid=a3_430582_1006:1105078849:N:%E9%BB%9B%E4%B8%9D%E5%B0%91%E5%A5%B3%E5%86%85%E8%A3%A4:9831ba60a817a7784ac3f11d456fa425&ali_trackid=1_9831ba60a817a7784ac3f11d456fa425&spm=a230r.1.14.1#detail'


def wd_js():
    wd = webdriver.PhantomJS()
    url_shop = 'https://shop100302658.taobao.com/category-699475496.htm?spm=a1z10.5-c-s.w5002-18224255204.3.50155e9etGX5EI&search=y&catName=%F7%EC%CB%BF%C9%D9%C5%AE%C5%AE%CA%BF%C4%DA%BF%E3'
    wd.get(url_shop)
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
    print(wd.title)

    #获取页数
    pn = wd.find_element_by_css_selector('.page-info')
    print(pn)

     #详情页图片
    # pics = wd.find_elements_by_css_selector('img[align="absmiddle"]')
    # for pic in pics:
    #     # print(pic.get_attribute('data-ks-lazyload'))
    #     # print(pics.index(pic))
    #     pic_url = pic.get_attribute('data-ks-lazyload')
    #     if pic_url:
    #         request.urlretrieve(pic_url, '%d.jpg' % pics.index(pic))

    # print(pics)
    wd.quit()

def wd_htmlunit():
    # wd = webdriver.Remote(command_executor="http://127.0.0.1:4444/wd/hub", desired_capabilities=DesiredCapabilities.HTMLUNIT)
    wd = webdriver.Remote(
        command_executor=' http://127.0.0.1:4444/wd/hub',
        desired_capabilities={'platform': 'ANY',
                              'browserName': 'htmlunit',
                              'version': '',
                              'javascriptEnabled': True
                              })
    wd.get(url)
    pics = wd.find_elements_by_css_selector('img[align="absmiddle"]')
    for pic in pics:
        print(pic.get_attribute('data-ks-lazyload'))


def get_shop():
    '''
    获取淘宝店铺
    :return:
    '''

    #url_shop = 'https://shop100302658.taobao.com/category-699475496.htm?spm=a1z10.5-c-s.w4002-18224255237.10.6fe35e9e7JKmht&_ksTS=1523519405354_198&callback=jsonp199&mid=w-18224255237-0&wid=18224255237&path=%2Fcategory-699475496.htm&catName=%F7%EC%CB%BF%C9%D9%C5%AE%C5%AE%CA%BF%C4%DA%BF%E3&catId=699475496&orderType=hotsell_desc'
    url_shop = 'https://shop100302658.taobao.com/category-699475496.htm?spm=a1z10.5-c-s.w4002-18224255237.99.47495e9eCj68lY&_ksTS=1523599975931_195&callback=jsonp196&mid=w-18224255237-0&wid=18224255237&path=%2Fcategory-699475496.htm&catName=%F7%EC%CB%BF%C9%D9%C5%AE%C5%AE%CA%BF%C4%DA%BF%E3&catId=699475496&orderType=hotsell_desc&pageNo=1'
    # 加启动配置
    option = webdriver.ChromeOptions()
    option.add_argument('disable-infobars')
    wd = webdriver.Chrome(chrome_options=option)
    # wd = webdriver.PhantomJS()
    wd.get(url_shop)
    # wd.implicitly_wait(5)
    html = wd.page_source
    # print(html)
    # print(wd.get_cookies())
    print(wd.title)

    ob = BeautifulSoup(html, 'lxml')
    #获取列表页数
    pages = ob.select('.page-info')
    # print(pn)
    page = pages[0].get_text()
    print(page)
    pn = page.split('/')
    num = pn['1']    #总页数
    print(num)
    # print(pn.get_text())
    #获取商品列表（商品名、商品地址）
    # goods = ob.select('.item-name')
    # print(len(goods))
    # for g in goods:
    #     # print('开始爬取第%d个商品' % goods.index(g))
    #     filepath = r'F:\淘宝'      #保存路径
    #     g_url = 'https://' + g['href']         #商品链接
    #     # print(g.get_text().trip())
    #     g_name = g.get_text()    #商品目录
    #     filepath = filepath + '\\' + g_name.strip()
    #     # print(filepath)
    #     # get_pic(g_url, filepath)



def get_pic(url, filepath):
    '''
    获取商品详情图片
    :return:
    '''
    wd = webdriver.PhantomJS()
    wd.get(url)
    html = wd.page_source

    ob = BeautifulSoup(html, 'lxml')
    pics = ob.select('img[align="absmiddle"]')

    if not os.path.exists(filepath):
        os.mkdir(filepath)      #创建商品目录
        print('成功创建%s文件夹' % filepath)

    for pic in pics:
        try:
            pic_url = pic['data-ks-lazyload']
            request.urlretrieve(pic_url, (filepath + '\\' + '%d.jpg' % pics.index(pic)))
            print('成功爬取第%d张图片' % pics.index(pic))
            # print(pic_url)
        except KeyError:
            continue
    wd.quit()




get_shop()
# wd_driver()