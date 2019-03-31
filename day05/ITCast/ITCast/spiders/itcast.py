# scrapy genspider itcast itcast.cn

import scrapy

from ..items import ItcastItem


class ITCastSpider(scrapy.Spider):
    # 爬虫名
    name = "itcast"
    # 允许采集的域名范围(可选)
    allowed_domains = ['itcast.cn']
    # 起始url地址列表(必须)
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        div_list = response.xpath("//div[@class='li_txt']")

        for div in div_list:
            #item = {}
            # 每一条数据，用一个item对象表示
            item = ItcastItem()
            item['name'] = div.xpath("./h3/text()").extract_first()
            item['title'] = div.xpath("./h4/text()").extract_first()
            item['info'] = div.xpath("./p/text()").extract_first()

            yield item

        #yield scrapy.Request()


# engine.py

# response = downloader()
# for request_or_item in spider.parse(response):
#     if isinstance(request_or_item, scrapy.Item):
#         pipeline.process_item(request_or_item)

#     elif isinstance(request_or_item, scrapy.Reqeust):
#         scheduler.add_reqeust(request_or_item)

#     else:
#         raise TypeError("Not Support data type")




