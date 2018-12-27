# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MfwItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    img = scrapy.Field()
    intro = scrapy.Field()
    addr = scrapy.Field()
    scan = scrapy.Field()
    comment= scrapy.Field()
    author =scrapy.Field()
    created=scrapy.Field()
    url =scrapy.Field()
    type =scrapy.Field()
    time =scrapy.Field()
    day = scrapy.Field()
    people = scrapy.Field()
    content = scrapy.Field()
    cost =scrapy.Field()
    # pass
