# # 导入链接提取器
# from scrapy.linkextractors import LinkExtractor
# # 导入CrawlSpider和Rule规则类
# from scrapy.spiders import CrawlSpider, Rule


# class TencentSpider(CrawlSpider):
#     name = "tencent3"
#     allowed_domians = ['hr.tencent.com']
#     start_urls = ['xxx']

#     rules = [
#         # 如没有callback，表示不需要提取数据，则默认follow=True，表示需要提取链接
#         # 如有callback，表示需要提取数据，则默认follow=False，表示不需要提取链接
#         Rule(LinkExtractor(allow=r"start=\d+")),
#         Rule(LinkExtractor(allow=r"position_detail\.php\?id=\d+"), callback="parse_detail"),
#     ]

#     def parse_detail(self, response):

#         link_extractor = LinkExtractor(allow=r'xxx')
#         link_list = link_extractor.extract_links(response)

#         for link in link_list:
#             print(link.url)



# -*- coding: utf-8 -*-

# CrawlSpider + Request : 将不同的页面数据，保存在同一个 item 中

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ..items import TencentItem


class TencentSpider(CrawlSpider):
    name = 'tencent3'
    allowed_domains = ['hr.tencent.com']
    # 程序启动后，第一个请求是start_urls里的请求，这个响应默认没有回调函数，但是它必须经过每一个Rule进行链接提取。
    start_urls = ["https://hr.tencent.com/position.php?&start=0"]

    # rules是一个列表/元组，可以存储多种不同的Rule规则：
    rules = (
        # 第一次的Rule提取的是 start_urls里的响应，并提取了 8 个链接，Rule会构建请求发送，返回的响应：
        # 1. 如果有callback，交给callback解析；没有callback不解析响应
        # 2. 如果follow=False，则不做后续链接提取；
        #    如果follow=True，则响应继续经过每一个Rule的linkextractor提取新的链接。

        # 取列表页的链接
        Rule(LinkExtractor(allow=r'start=\d+'),  callback="parse_page", follow=True),
        # 取详情页的链接
        #Rule(LinkExtractor(allow=r'position_detail\.php\?id=\d+'),  callback="parse_detail", follow=False)
    )


    def parse_page(self, response):
        tr_list = response.xpath("//tr[@class='even'] | //tr[@class='odd']")

        # print("===" * 10)
        # print(len(tr_list))
        # print("===" * 10)

        self.logger.info("===" * 10)
        self.logger.info("Hello World")
        self.logger.info(len(tr_list))

        for tr in tr_list:
            # 每一条职位，对应一个item对象存储
            item = TencentItem()
            # 职位名
            item['position_name'] = tr.xpath("./td[1]/a/text()").extract_first()
            # 详情连接
            item['position_link'] = "https://hr.tencent.com/" + tr.xpath("./td[1]/a/@href").extract_first()
            # 职位类别
            item['position_type'] = tr.xpath("./td[2]/text()").extract_first()
            # 招聘人数
            item['people_number'] = tr.xpath("./td[3]/text()").extract_first()
            # 工作地点
            item['work_location'] = tr.xpath("./td[4]/text()").extract_first()
            # 发布时间
            item['publish_times'] = tr.xpath("./td[5]/text()").extract_first()

            yield item
