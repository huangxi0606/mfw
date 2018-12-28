#!/usr/bin/env python
# -*- coding:utf-8 -*-
from mfw.items import MfwItem
import pickle
from redis import StrictRedis
# byte_data = pickle.dumps(dic) 序列化
# obj = pickle.loads(byte_data) 反序列化
class MfwRedisPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, MfwItem):
            data = [{
                'title ': item['title'],
                'img ': item['img'],
                'intro ': item['intro'],
                'addr ': item['addr'],
                'scan ': item['scan'],
                'comment ': item['comment'],
                'author ': item['author'],
                'created ': item['created'],
                'url ': item['url'],
                'type ': item['type'],
                'time ': item['time'],
                'day ': item['day'],
                'people ': item['people'],
                # 'content ':item['content'],
                'cost ': item['cost'],
            }]
            data_us=pickle.dumps(data)
            redis = StrictRedis(host='localhost', port=6379, db=6, password='')
            redis.lpush("data",data_us)
            return item