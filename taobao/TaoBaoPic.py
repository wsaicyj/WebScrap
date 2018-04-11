#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-
__author__ = 'Aaron_chan'



from selenium import webdriver
import time
from xml import etree
import lxml


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
        """获取淘宝店铺页面代码
        """

        self.driver.get(self.site_url)
        time.sleep(self.sleep_time)
        content = self.driver.page_source.encode('utf-8')
        print(self.driver.title)
        # 保存html代码debug
        # self.saveHtml('taobaoshop', content)

        # 分析该页面的每个宝贝
        self.getItem()

    def getItem(self):
        """爬取当前页面的每个宝贝，
           提取宝贝名字，价格，标题等信息
        """

        html = self.driver.page_source.encode('utf-8')
        selector = etree.HTML(html)
        itemList = selector.xpath("//div[@class='item3line1']")

        # 循环遍历该页所有商品
        index = 0
        for item3line1 in itemList:
            dl = item3line1.xpath("./dl")
            for item in dl:
                link = 'https:' + item.xpath("./dt/a/@href")[0]
                photo = 'https:' + item.xpath("./dt/a/img/@src")[0]
                title = item.xpath("./dd/a/text()")[0]

                res = {
                    'link': link,
                    'photo': photo,
                    'title': title
                }

                # 进入宝贝详情页 开始爬取里面的图片资料
                self.getItemDetail(link, '')

        # 获取分页信息
        pagination = selector.xpath("//div[@class='pagination']/a[contains(@class, 'J_SearchAsync') and contains(@class, 'next')]/@href")
        print(pagination)
        print('正在准备切换分页')
        if len(pagination) == 0:
            print('没有下一页了')

        else:
            print('加载下一页内容')
            self.site_url = 'https:' + pagination[0]
            print(self.site_url)
            self.getPage()

    def getItemDetail(self, link, save_img_path):
        """从宝贝的详情链接里 爬取图片
        Arguments:
            link {String} -- [宝贝详情链接]
        """
        newDriver = webdriver.Chrome()
        newDriver.get(link)
        time.sleep(self.sleep_time)

        print(newDriver.title)

        img_dir_path = save_img_path + newDriver.title.encode('utf-8')
        if True == self.mkdir(img_dir_path):
            print('创建宝贝目录成功')

        html = newDriver.page_source.encode('utf-8')
        selector = etree.HTML(html)

        # 封面图
        J_ULThumb = selector.xpath("//div[@class='tb-gallery']/ul/li")
        index = 0
        for li in J_ULThumb:
            # 替换图片 从50*50 至 400 * 400
            if len(li.xpath("./div/a/img/@data-src")) < 1:
                continue
            small_pic = li.xpath("./div/a/img/@data-src")[0]
            common_pic = 'https:' + small_pic.replace('50x50', '400x400')
            thumb_title = str('封面图') + str(index)
            print(thumb_title)
            # self.saveImg(img_dir_path, common_pic, thumb_title.decode('utf-8'))
            index += 1

        # 爬取里面所有图片
        all_img = selector.xpath("//div[@id='J_DivItemDesc']//descendant::img/@src")
        print(all_img)
        index = 0
        for img in all_img:
            # imglink = ''
            if img.startswith('http') is True:
                imglink = img
            else:
                imglink = 'https:' + img

            self.saveImg(img_dir_path, imglink, str(index))
            index += 1

        newDriver.quit()



if __name__ == '__main__':
    pass
