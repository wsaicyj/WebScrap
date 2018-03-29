#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-
__author__ = 'Aaron_chan'

import requests, json

ks_videos = []


def get_video():
    url = 'http://180.186.38.200/rest/n/feed/hot?mod=HUAWEI(PRA-AL00X)&lon=113.270916&country_code=cn&did=ANDROID_d62943e5c4816937&net=WIFI&app=0&oc=HUAWEI&ud=0&c=HUAWEI&sys=ANDROID_7.0&appver=5.6.0.5908&ftt=&language=zh-cn&iuid=DuFj6ep83UHzHtLDxNFJnW8FQ0A5ijbUm0nXcSmvPgwbu7xrQZjnmqiJRFxCAESjPW/gBkKv4gT0vCaEmnSUFJPQ&lat=23.115109&ver=5.6&max_memory=384'
    data = {
        'type': 7,
        'page': 1,
        'coldStart': 'false',
        'count': 20,
        'pv': 'false',
        'id': 35,
        'refreshTimes': 13,
        'pcursor': '',
        'source': 1,
        'client_key': '3c2cd3f3',
        'os': 'android',
        # 'sig': 'd0c81adf81514d772af97c3c896f4779',
        'sig': 'a04331be8774732016fcfab845e30457',
    }

    headers = {
        'User-Agent': 'kwai-android',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    r = requests.post(url, data=data, headers=headers)
    html = r.text
    # print(type(html))
    videos = json.loads(html)
    # print(videos)
    # print(len(videos['feeds']))
    str_gxmov = 'http://gxmov.a.yximgs.com'
    str_jsmov2 = 'http://jsmov2.a.yximgs.com'
    for v in videos['feeds']:
        # print(v['main_mv_urls']['url'])
        try:
            for u in v['main_mv_urls']:
                # requests.post(u['url'])
                # print('正在下载视频。。。')
                if (str_gxmov not in u['url']) and (str_jsmov2 not in u['url']):
                    ks_videos.append(u['url'])
                # print(type(u['url']))
                # print(len(u['url']))
        except KeyError:
            continue



            # print(type(videos))
            # print(type(videos['feeds']))
            # print(videos['feeds'])
            # print(r.text)


get_video()
print(ks_videos)
# print(len(ks_videos))
# s = 'http://gxmov.a.yximgs.com/upic/2018/03/26/20/BMjAxODAzMjYyMDAxMTdfNzg2MDUyN181NjM0MjgyNjIwXzFfMw==_b_Bd2c397a7fdb584aa270aec059d6af9dd.mp4?tag=1-1522139115-h-0-rxjcugeusi-ab8af2eb96540a55'
# str = 'http://gxmov.a.yximgs.com'
#
# print(str not in s)