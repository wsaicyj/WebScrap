#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-
__author__ = 'Aaron_chan'

from .blibli import GetBlibliVideos


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.168 Safari/537.36',
    'Referer': 'https://www.bilibili.com/v/cinephile/montage/?spm_id_from=333.83.primary_menu.77',
    'Host': 'api.bilibili.com'
}

seedfood_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.168 Safari/537.36',
    # 'Referer': 'https://www.bilibili.com/v/cinephile/montage/?spm_id_from=333.83.primary_menu.77',
    'Host': 'search.bilibili.com'
}



def seafood_download():
    '''
    搜索海鲜然后下载
    :return:
    '''
    # 海鲜
    url_seedfood = u'https://search.bilibili.com/api/search?search_type=video&keyword=海鲜&from_source=banner_search&order=totalrank&duration=1&tids=0&page=%d'
    # 美食搜索
    url_food = u'https://search.bilibili.com/api/search?search_type=video&keyword=美食&from_source=banner_search&order=totalrank&duration=1&tids=0&page=%d'
    seedfood_path = r'E:\b站视频\海鲜'
    f_pn = 6
    l_pn = 7
    b = GetBlibliVideos(url_seedfood, seedfood_headers, seedfood_path, f_pn, l_pn)
    b.download_video(flag=False)


def movie_downlaod():
    '''
    视频下载
    :return:
    '''
    movie_path = r'E:\b站视频\电影剪辑'
    f_pn = 1
    l_pn = 2
    # 影视剪辑
    url_movie = ''
    b = GetBlibliVideos(url_movie, headers, movie_path, f_pn, l_pn)
    b.download_video(flag=True)    #视频下载


def simle_downlaod():
    '''
    搞笑视频下载
    :return:
    '''
    simle_path = r'E:\b站视频\搞笑'
    # 搞笑
    url_smile = ''
    f_pn = 1
    l_pn = 2
    # 影视剪辑
    url_movie = ''
    b = GetBlibliVideos(url_smile, headers, simle_path, f_pn, l_pn)
    b.download_video(flag=True)    #视频下载


def food_downlaod():
    '''
    美食视频下载
    :return:
    '''
    food_path = r'E:\b站视频\美食'
    # 美食
    url_food = ''
    f_pn = 1
    l_pn = 2
    # 影视剪辑
    url_movie = ''
    b = GetBlibliVideos(url_food, headers, food_path, f_pn, l_pn)
    b.download_video(flag=True)    #视频下载