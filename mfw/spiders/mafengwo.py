# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import requests
from urllib import parse
from mfw.items import MfwItem
from bs4 import BeautifulSoup


Header = {
    "Host":"www.mafengwo.cn",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language":"zh-CN,zh;q=0.9",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36",
}

class MafengwoSpider(scrapy.Spider):
    name = 'mafengwo'
    # allowed_domains = ['http://www.mafengwo.cn']
    base_url = ['http://www.mafengwo.cn']
    # PROXY_POOL_URL = 'http://127.0.0.1:5000/get'
    # MAX_COUNT = 5
    # proxy = None  # 建立一个全局的变量，来存代理
    # str_count = 0
    # def get_proxy(self):#获得代理
    #     try:
    #         response = requests.get(self.PROXY_POOL_URL)
    #         if response.status_code == 200:
    #             return response.text
    #         return None
    #     except ConnectionError:
    #         print('获取代理时发生异常')
    #         return None
    # def get_html(self, url, count=1):# count默认值为1，如果有赋值则不使用默认值
    #     try:
    #         if self.proxy==None :# 如果代理不存在
    #             self.proxy = self.get_proxy()
    #         proxies = {
    #             'http': 'http://' + self.proxy,
    #             'https': 'https://' + self.proxy
    #         }
    #         print('使用了代理：', self.proxy)
    #         response = requests.get(url, allow_redirects=False, proxies='http://' + self.proxy,meta=Header)#可以设定超时时间30s
    #         print(response.status_code)
    #         if response.status_code == 200:
    #             return response.text
    #         else:
    #             # 更换代理，重新访问
    #             print('302/403等错误')
    #             self.proxy = self.get_proxy()#获得新代理
    #             if self.proxy:
    #                 print('Using Proxy', self.proxy)
    #                 count = count + 1
    #                 return self.get_html(url, count)#更改后的代理，也可能不能用
    #             else:
    #                 print('Get Proxy Failed')
    #                 return None# 没有可用代理的时候返回none
    #     except ConnectionError as e:
    #         print('Error Occurred', e.args)# 输出错误信息
    #         self.proxy = self.get_proxy()
    #         count += 1
    #         return self.get_html(url, count)
    def start_requests(self):
        dicts = [
            '台湾',
            '土耳其'
        ]
        for dict in dicts:
            mfwItem = MfwItem()
            mfwItem['type'] = dict
            dict = parse.quote(dict)
            print(dict)
            print('huangxi')
            for i in range(1, 49):
                url ="http://www.mafengwo.cn/search/s.php?q="+ dict +"&p=" +str(i)+ "&t=info&kt=1"
                # print(url)

        # url ='http://www.mafengwo.cn/search/s.php?q=%E5%9C%9F%E8%80%B3%E5%85%B6&p=1&t=info&kt=1'

                yield Request(url=url,callback=self.parse, meta ={'headers': Header,'mfwItem':mfwItem})

    def parse(self, response):
        # print('luckly')
        # print(response.meta['mfwItem']['type'])
        mfwItem = MfwItem()
        soup = BeautifulSoup(response.text, "lxml")
        for all in soup.find_all("div", class_="clearfix"):
            if all.find("h3"):
                title = all.find("h3").text.replace('\n', '').replace(',', '').strip()
                mfwItem['title']=title
                intro = all.find("p", class_="seg-desc").text
                mfwItem['intro'] = intro
                url = all.find("h3").a['href']
                mfwItem['url'] = url
                img = all.find("div", class_="flt1").find('img').get('src')
                mfwItem['img'] = img
                mfwItem['type'] = response.meta['mfwItem']['type']
                for ul in all.find_all(class_='seg-info-list'):
                    if ul.select('li'):
                        addr =ul.select('li')[0].get_text().replace('\n', '').replace(',', '').strip()
                        mfwItem['addr'] = addr
                        scan = ul.select('li')[1].get_text().replace('\n', '').replace(',', '').strip()
                        mfwItem['scan'] = scan
                        # print(ul.select('li')[2].get_text())
                        # print(ul.select('li')[3].get_text())
                        if len(ul.select('li')) > 4:
                            # print(ul.select('li')[4].get_text())
                            comment = ul.select('li')[2].get_text().replace('\n', '').replace(',', '').strip()
                            mfwItem['comment'] = comment
                            author = ul.select('li')[3].get_text().replace('\n', '').replace(',', '').strip()
                            mfwItem['author'] = author
                            created = ul.select('li')[4].get_text().replace('\n', '').replace(',', '').strip()
                            mfwItem['created'] = created
                        else:
                            author = ul.select('li')[2].get_text().replace('\n', '').replace(',', '').strip()
                            mfwItem['author'] = author
                            created = ul.select('li')[3].get_text().replace('\n', '').replace(',', '').strip()
                            mfwItem['created'] = created
        # yield mfwItem
        yield Request(url=url, callback=self.get_content, meta={'mfwItem': mfwItem})

    def get_content(self, response):
        # print("anpu")
        soup = BeautifulSoup(response.text, "html.parser")
        # print(soup.find("li", class_="time").text)
        # print(soup.find("li", class_="day").text)
        # print(soup.find("li", class_="people").text)
        # print(soup.find("li", class_="cost").text)
        # print(soup.find("div", class_="_j_content_box").text.replace('\n', '').replace(' ', ''))
        mfwItem = MfwItem()
        if soup.find("li", class_="time"):
            mfwItem['time'] =soup.find("li", class_="time").text
        else:
            mfwItem['time'] = 'wu'
        if soup.find("li", class_="day"):
            mfwItem['day'] =soup.find("li", class_="day").text
        else:
            mfwItem['day'] = 'wu'
        if soup.find("li", class_="people"):
            mfwItem['people'] =soup.find("li", class_="people").text
        else:
            mfwItem['people'] = 'wu'
        if soup.find("li", class_="cost"):
            mfwItem['cost'] =soup.find("li", class_="cost").text
        else:
            mfwItem['cost'] = 'wu'
        if soup.find("div", class_="_j_content_box"):
            mfwItem['content'] =soup.find("div", class_="_j_content_box").text.replace('\n', '').replace(' ', '')
        else:
            mfwItem['content']='wu'
        # print('huangxi')
        # if(response.meta['mfwItem']):
        # print(mfwItem)
        # return mfwItem
        # print(response.text)
        # print(response.meta['mfwItem'])
        if response.meta['mfwItem']['addr']:
            mfwItem['addr'] =response.meta['mfwItem']['addr']
        if response.meta['mfwItem']['author']:
            mfwItem['author'] =response.meta['mfwItem']['author']
        if response.meta['mfwItem']['comment']:
            mfwItem['comment'] =response.meta['mfwItem']['comment']
        else:
            mfwItem['comment'] = 0
        if response.meta['mfwItem']['created']:
            mfwItem['created'] =response.meta['mfwItem']['created']
        if response.meta['mfwItem']['img']:
            mfwItem['img'] =response.meta['mfwItem']['img']
        if response.meta['mfwItem']['intro']:
            mfwItem['intro'] =response.meta['mfwItem']['intro']
        if response.meta['mfwItem']['scan']:
            mfwItem['scan'] =response.meta['mfwItem']['scan']
        if response.meta['mfwItem']['title']:
            mfwItem['title'] =response.meta['mfwItem']['title']
        if response.meta['mfwItem']['url']:
            mfwItem['url'] =response.meta['mfwItem']['url']
        if response.meta['mfwItem']['type']:
            mfwItem['type'] =response.meta['mfwItem']['type']
        yield mfwItem
        return mfwItem
        # print('huangxi')

