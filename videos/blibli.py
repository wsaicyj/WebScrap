#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-
__author__ = 'Aaron_chan'


import requests, json, re, os


#url = 'https://www.bilibili.com/v/cinephile/montage/?spm_id_from=333.83.primary_menu.77#/all/click/0/1/2018-03-22,2018-03-29'
#url = 'https://s.search.bilibili.com/cate/search?callback=jQuery1720010136889334537935_1522293738879&main_ver=v3&search_type=video&view_type=hot_rank&order=click&copy_right=-1&cate_id=183&page=2&pagesize=20&jsonp=jsonp&time_from=20180322&time_to=20180329&_=1522293739727'
#影视剪辑
#url = 'https://api.bilibili.com/x/web-interface/newlist?callback=jQuery172003168606167657728_1522295282771&rid=183&type=0&pn=1&ps=20&jsonp=jsonp&_=1522295283617'
#影视杂谈
#url = 'https://api.bilibili.com/x/web-interface/newlist?callback=jQuery17207030382340046122_1522296892120&rid=182&type=0&pn=2&ps=20&jsonp=jsonp&_=1522296892736'
#url = 'https://www.bilibili.com/v/cinephile/montage/?spm_id_from=333.83.primary_menu.77#/all/default'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.168 Safari/537.36',
#     'Referer': 'https://www.bilibili.com/v/cinephile/montage/?spm_id_from=333.83.primary_menu.77',
#     'Host': 'api.bilibili.com'
# }
# r = requests.get(url, headers=headers)
# html = r.text.encode('utf-8').decode('unicode_escape')
# html = r.text
# pattern = re.compile(r'"aid":(\d+),')
# aids = set(pattern.findall(html))
# vips = json.loads(html)
# print(type(aids))
# print(aids)

class GetBlibliVideos():
    '''爬取b站视频'''

    def __init__(self, url, headers, filepath, f_pn, l_pn):
        self.url = url
        self.headers = headers
        self.f_pn = f_pn    #首页
        self.l_pn = l_pn    #次页
        self.filepath = filepath

    def get_aids(self, flag):
        '''获取b站下视频的aid'''
        aids = set()
        for i in range(self.f_pn, self.l_pn):
            r = requests.get(self.url % i, headers=self.headers)
            html = r.text
            # print(html)
            if flag:
                pattern = re.compile(r'"aid":(\d+),')
            else:
                pattern = re.compile(r'"id":(\d+)')

            for aid in pattern.findall(html):
                aids.add(aid)
        # aids.remove('0')
        # list(aids)
        return aids


    def download_video(self, flag):
        '''下载b站视频'''
        aids = list(self.get_aids(flag))
        video_url = 'https://www.bilibili.com/video/av'
        num = len(aids)
        print('总共有%d部视频' % num)
        if not os.path.exists(self.filepath):
            os.mkdir(self.filepath)
            print('成功创建文件夹')
            for aid in aids:
                print('正在下载第%d部视频' % (aids.index(aid)+1))
                os.system('you-get -o %s %s%s' % (self.filepath, video_url, aid))
                print('第%d部视频已下载完毕' % (aids.index(aid)+1))
        else:
            for aid in aids:
                print('正在下载第%d部视频' % (aids.index(aid)+1))
                os.system('you-get -o %s %s%s' % (self.filepath, video_url, aid))
                print('第%d部视频已下载完毕' % (aids.index(aid)+1))



if __name__ == '__main__':

    movie_path = r'E:\b站视频\电影剪辑'
    food_path = r'E:\b站视频\美食'
    simle_path = r'E:\b站视频\搞笑'
    seedfood_path = r'E:\b站视频\海鲜'

    f_pn = 3
    l_pn = 5

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
    #影视剪辑
    url_movie = 'https://api.bilibili.com/x/tag/ranking/archives?callback=jQuery17209140340510768037_1522635041067&tag_id=105624&rid=183&type=0&pn=%r&ps=20&jsonp=jsonp&_=1522635058905'
    #美食圈
    url_food = 'https://api.bilibili.com/x/web-interface/newlist?callback=jQuery172029422949515626273_1522380074806&rid=76&type=0&pn=%d&ps=20&jsonp=jsonp&_=1522380075833'
    #搞笑
    url_smile = 'https://api.bilibili.com/x/web-interface/newlist?callback=jQuery17204101817794147882_1522641748126&rid=138&type=0&pn=%d&ps=20&jsonp=jsonp&_=1522641748640'
    #海鲜
    url_seedfood = u'https://search.bilibili.com/api/search?search_type=video&keyword=海鲜&from_source=banner_search&order=totalrank&duration=1&tids=0&page=%d'

    # b = GetBlibliVideos(url_movie, headers, movie_path, pn)
    # b = GetBlibliVideos(url_food, headers, food_path, pn)
    # b = GetBlibliVideos(url_smile, headers, simle_path, pn)
    # b.download_video(flag=True)    #视频下载

    # 海鲜搜索
    b = GetBlibliVideos(url_seedfood, seedfood_headers, seedfood_path, f_pn, l_pn)
    b.download_video(flag=False)