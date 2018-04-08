#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-
__author__ = 'Aaron_chan'



from selenium import webdriver
import time

class TaoBaoPic():

    '''
    https://www.jianshu.com/p/64430f5c6a9a
    '''

    def __init__(self):
        self.sit_url = ''
        self.driver = webdriver.Chrome()
        self.sleep_time = 10
        self.save_img_path = ''


    def getPage(self):
        '''
        获取淘宝店铺页面代码
        :return:
        '''
        self.driver.get(self.sit_url)
        time.sleep(self.sleep_time)