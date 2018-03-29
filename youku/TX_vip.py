#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-
__author__ = 'Aaron_chan'


import  requests, json, re

# url = 'https://list.video.qq.com/fcgi-bin/list_common_cgi?otype=json&novalue=1&platform=1&version=10000&intfname=web_vip_movie_new&tid=687&appkey=c8094537f5337021&appid=200010596&type=1&sourcetype=1&itype=-1&iyear=-1&iarea=-1&iawards=-1&sort=17&pagesize=30&offset=0&callback=jQuery19107680377117880124_1521526646809&_=1521526646811'
#
# r = requests.get(url)
# html = r.text
# pattern = re.compile(r'"title":"(.*?)"')
#
# vip = pattern.findall(html)
# print(len(vip))
# print(vip)

# html = json.loads(r.text)

# print(r.text)

def get_tx_vip():
    '''
    爬取腾讯vip视频电影名
    :return:
    '''
    pn = 75
    for i in range(pn):
        print('成功爬取第%d页全部电影名' % i)
        i *= 30
        url = 'https://list.video.qq.com/fcgi-bin/list_common_cgi?otype=json&novalue=1&platform=1&version=10000&intfname=web_vip_movie_new&tid=687&appkey=c8094537f5337021&appid=200010596&type=1&sourcetype=1&itype=-1&iyear=-1&iarea=-1&iawards=-1&sort=17&pagesize=30&offset=%d&callback=jQuery19107680377117880124_1521526646809&_=1521526646811' % i
        r = requests.get(url)
        html = r.text
        pattern = re.compile(r'"title":"(.*?)"')
        vip = pattern.findall(html)
        for v in vip:
            # tx_v.append(v)
            try:
                with open('vip.txt', 'a') as f:
                    f.writelines(v + '\n')
            except UnicodeEncodeError:
                continue


get_tx_vip()

