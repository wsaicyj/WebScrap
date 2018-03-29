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
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.168 Safari/537.36',
    'Referer': 'https://www.bilibili.com/v/cinephile/montage/?spm_id_from=333.83.primary_menu.77',
    'Host': 'api.bilibili.com'
}
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

    def __init__(self, url, headers, filepath, pn):
        self.url = url
        self.headers = headers
        self.pn = pn
        self.filepath = filepath

    def get_aids(self):
        '''获取b站下最新投稿的视频aid'''
        aids = set()
        for i in range(1, self.pn):
            r = requests.get(self.url % i, headers=self.headers)
            html = r.text
            # print(html)
            pattern = re.compile(r'"aid":(\d+),')
            for aid in pattern.findall(html):
                aids.add(aid)
        # aids.remove('0')
        # list(aids)
        return aids

    def download_video(self):
        '''下载b站视频'''
        aids = list(self.get_aids())
        video_url = 'https://www.bilibili.com/video/av'
        num = len(aids)
        print('总共有%d部视频' % num)
        if not os.path.exists(self.filepath):
            os.mkdir(self.filepath)
            for aid in aids:
                print('正在下载第%d部视频' % (aids.index(aid)+1))
                os.system('you-get -o %s %s%s' % (self.filepath, video_url, aid))
                print('第%d部视频已下载完毕' % (aids.index(aid)+1))
        else:
            for aid in aids:
                print('正在下载第%d部视频' % (aids.index(aid)+1))
                os.system('you-get -o %s %s%s' % (self.filepath, video_url, aid))
                print('第%d部视频已下载完毕' % (aids.index(aid)+1))






# def get_aids(url, headers):
#     '''获取b站下的视频aid'''
#     r = requests.get(url, headers=headers)
#     html = r.text
#     pattern = re.compile(r'"aid":(\d+),')
#     aids = set(pattern.findall(html))
#     return aids
#
#
# def download_video():
#     '''下载b站视频'''
#     os.system('you-get https://www.bilibili.com/video/av21359106')


# download_video()


if __name__ == '__main__':

    filepath = r'E:\b站视频'

    pn = 2

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.168 Safari/537.36',
        'Referer': 'https://www.bilibili.com/v/cinephile/montage/?spm_id_from=333.83.primary_menu.77',
        'Host': 'api.bilibili.com'
    }
    #影视剪辑(全部)
    url_all = 'https://api.bilibili.com/x/web-interface/newlist?callback=jQuery17206022572212015742_1522296936675&rid=183&type=0&pn=%d&ps=20&jsonp=jsonp&_=1522296937215'
    #影视剪辑(电影剪辑)
    url_movie = 'https://api.bilibili.com/x/tag/ranking/archives?callback=jQuery17207954054307878193_1522310547386&tag_id=105624&rid=183&type=0&pn=%d&ps=20&jsonp=jsonp&_=1522310568974'
    b = GetBlibliVideos(url_movie, headers, filepath, pn)
    b.download_video()
    # print(b.get_aids())