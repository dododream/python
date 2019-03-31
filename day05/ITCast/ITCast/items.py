# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ItcastItem(scrapy.Item):
    # define the fields for your item here like:
    # 姓名
    name = scrapy.Field()
    # 职称
    title = scrapy.Field()
    # 简介
    info = scrapy.Field()
    # _id值
    _id = scrapy.Field()
