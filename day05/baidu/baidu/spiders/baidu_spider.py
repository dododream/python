# -*- coding: utf-8 -*-
import scrapy


# scrapy.Spider
class BaiduSpiderSpider(scrapy.Spider):

    # 必须提供的唯一爬虫名
    name = 'baidu_spider'
    # 允许采集的域名范围 baidu.com
    allowed_domains = ['baidu.com']
    # 第一批需要发送的url地址
    start_urls = ['http://www.baidu.com/', 'http://news.baidu.com/']

    def parse(self, response):
        title = response.xpath("//title/text()").extract_first()

        with open(title + ".html", "wb") as f:
            f.write(response.body)

