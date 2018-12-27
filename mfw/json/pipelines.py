# -*- coding: utf-8 -*-
from mfw.items import MfwItem
import json

class MfwJsonPipeline(object):
    def process_item(self, item, spider):
        data = [{
            'title ':item['title'],
            'img ':item['img'],
            'intro ':item['intro'],
            'addr ':item['addr'],
            'scan ':item['scan'],
            'comment ':item['comment'],
            'author ':item['author'],
            'created ':item['created'],
            'url ':item['url'],
            'type ':item['type'],
            'time ':item['time'],
            'day ':item['day'],
            'people ':item['people'],
            # 'content ':item['content'],
            'cost ':item['cost'],
        }]
        with open('data1.json', 'a', encoding='utf-8') as file:
            file.write(json.dumps(data, indent=2, ensure_ascii=False))
            return item