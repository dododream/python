# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuItem(scrapy.Item):
    # 房间url
    room_url = scrapy.Field()
    # 图片连接
    image_src = scrapy.Field()
    # 昵称
    nick_name = scrapy.Field()
    # 所在城市
    anchor_city = scrapy.Field()
    # 图片在本地的路径
    image_path = scrapy.Field()
