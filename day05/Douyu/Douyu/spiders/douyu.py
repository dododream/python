# scrapy genspider douyu douyucdn.cn

import json

import scrapy

from ..items import DouyuItem


class DouyuSpider(scrapy.Spider):
    name = "douyu"

    allowed_domains = ['douyucdn.cn']

    base_url = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=100&offset={}"
    page = 0

    start_urls = [base_url.format(page)]


    def parse(self, response):
        data_list = json.loads(response.body)['data']

        if not data_list:
            return


        for data in data_list:
            item = DouyuItem()
            # 直播间url地址
            item['room_url'] = "http://www.douyu.com/" + data['room_id']
            # 主播图片
            item['image_src'] = data['room_src']
            # 昵称
            item['nick_name'] = data['nickname']
            # 所在城市
            item['anchor_city'] = data['anchor_city']
            #item['image_path'] = data['image_path']

            yield scrapy.Request(item['image_src'], meta={"item" : item}, callback=self.save_image)

        self.page += 100
        next_url = self.base_url.format(self.page)

        yield scrapy.Request(next_url, callback=self.parse)


    def save_image(self, response):
        item = response.meta['item']

        file_name = "/Users/Power/lesson_python/_23_1204/day05/Douyu/Douyu/Images/" + item['nick_name'] + ".jpg"

        with open(file_name, "wb") as f:
            f.write(response.body)

        item['image_path'] = file_name

        yield item



