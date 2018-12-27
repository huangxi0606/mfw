# -*- coding: utf-8 -*-
from mfw.items import MfwItem
import csv

class MfwCsvPipeline(object):
    def process_item(self, item, spider):
        print('街灯')
        if isinstance(item, MfwItem):
            with open('mfw.csv', 'a',encoding='GBK') as csvfile:
                writer = csv.writer(csvfile, delimiter=' ')
                writer.writerow([item['title'], item['img'], item['intro'], item['addr'], item['scan'], item['comment'], item['author'], item['created'], item['url'], item['type'], item['time'], item['day'], item['people'], item['content'], item['cost'] ])
                return item