#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-
__author__ = 'Aaron_chan'


import requests, json


def get_videos():

    url = 'https://app.2or3m.com/app/fenzhongkeji/recommend/getHomeRecommendation.json?userid=555955&currentPage=15221337337619815&type=0&isJPush=1&adid=&advertisementID=0&fzuid=555955'

    # data1 = 'clienttimestamp=1522133982628&clientsign=173aeb6c15e97babc4fdc1a7216d0f40&clientdevicetoken=555955&clientuserid=555955&clientphone=&clientlat=113.277048&clientlng=23.121571&clientimei=6637b1f0-4bfb-3e2b-ac29-1c0e5ada23aa&clientosversion=24&clientappkey=0ce6e205f4774b6eb732eeee5588ecde&clientos=android&clientappversion=3.5.6&clientver=201705&clientscreenwidth=1080&clientnetworktype=WIFI&clientchannel=huawei&clientscreenheight=1812&clientapptype=1'

    data = {
        'clienttimestamp': '1522133732485',
        'clientsign': '833c0fd30ccee8db1cab4ce3dc720eb2',
        'clientdevicetoken': '555955',
        'clientuserid': '555955',
        'clientphone': '',
        'clientlat': '113.277048',
        'clientlng': '23.121571',
        'clientimei': '6637b1f0-4bfb-3e2b-ac29-1c0e5ada23aa',
        'clientosversion': '24',
        'clientappkey': '0ce6e205f4774b6eb732eeee5588ecde',
        'clientos': 'android',
        'clientappversion': '3.5.6',
        'clientver': '201705',
        'clientscreenwidth': '1080',
        'clientnetworktype': 'WIFI',
        'clientchannel': 'huawei',
        'clientscreenheight': '1812',
        'clientapptype': '1',
    }


    headers = {
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'User-Agent': 'okhttp/3.3.1',
        'Accept-Encoding': 'gzip',
        'Connection': 'Keep-Alive',
        'Host': 'app.2or3m.com'
    }
    r = requests.post(url, data=data)
    # r = requests.post(url, data=data, verify=False)
    # r = requests.post(url, data=data, headers=headers)
    html = r.text
    # print(type(html))
    print(r.text)




get_videos()