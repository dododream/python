# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from datetime import datetime


from .items import TencentItem, DetailItem


class BaseInfoPipeline(object):
    def process_item(self, item, spider):
        item['spider'] = spider.name
        itme['time'] = str(datetime.now())

        return item

class TencentPipeline(object):
    def open_spider(self, spider):
        self.f = open("tencent.json", "w")

    def process_item(self, item, spider):
        if isinstance(item, TencentItem):
            json_str = json.dumps(dict(item), ensure_ascii=False) + "\n"
            self.f.write(json_str)

        return item

    def close_spider(self, spider):
        self.f.close()


class DetailPipeline(object):
    def open_spider(self, spider):
        self.f = open("detail.json", "w")

    def process_item(self, item, spider):
        if isinstance(item, DetailItem):
            json_str = json.dumps(dict(item), ensure_ascii=False) + "\n"
            self.f.write(json_str)

        return item

    def close_spider(self, spider):
        self.f.close()




