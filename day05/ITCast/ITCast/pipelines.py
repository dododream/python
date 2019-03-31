# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

class ItcastMongoPipeline(object):
    #def __init__(self):
    def open_spider(self, spider):
        self.client = pymongo.MongoClient()
        self.teacher = self.client.newitcast.teacher
        self._id = 0

    def process_item(self, item, spider):
        item['_id'] = self._id
        self.teacher.insert(dict(item))
        self._id += 1
        return item

    #def __del__(self):
    def close_spider(self, spider):
        pass



# pipeline = ItcastPipeline()
# pipeline.open_spider()

# pipeline.process_item(item, spider)
# pipeline.process_item(item, spider)
# pipeline.process_item(item, spider)
# pipeline.process_item(item, spider)
# pipeline.process_item(item, spider)
# pipeline.process_item(item, spider)

# pipeline.close_spider()
