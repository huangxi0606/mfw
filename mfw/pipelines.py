# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from .sql import Sql
from .items import MfwItem

class MfwPipeline(object):
    def process_item(self, item, spider):
        # return item
        print('小幸运')
        if isinstance(item,MfwItem):
            title =item['title']
            ret =Sql.select_travels(title)
            print('无用')
            if ret[0]==1:
                print('已经存在')
                pass
            else:
                print('开始保存')
                # title, img, intro, addr, scan, comment, author, created, url, type, timeone, dayone, people, content, cost
                Sql.insert_travels(item['title'],item['img'],item['intro'],item['addr'],item['scan'],item['comment'],item['author'],item['created'],item['url'],item['type'],item['time'],item['day'],item['people'],item['content'],item['cost'])
                return item

