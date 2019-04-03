# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TencentPipeline(object):
    def process_item(self, item, spider):
        #spider.logger.debug("xxxx")
        #spider.logger.info("xxxx")
        #spider.logger.warning("xxxx")
        # try:
        #     xxxx
        # except:
        #     spider.logger.error("xxxx")

        #spider.logger.critical("xxxx")


        return item
