# scrapy genspider tencent1 hr.tencent.com

import scrapy
from ..items import TencentItem

class TencentSpider(scrapy.Spider):

    name = "tencent2"

    allowed_domains = ["hr.tencent.com"]

    start_urls = ["https://hr.tencent.com/position.php?start=0"]

    def parse(self, response):

        tr_list = response.xpath("//tr[@class='even'] | //tr[@class='odd']")

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

        # 通过提取下一页连接的方式，处理多页采集，并在最后一页不再提取
        if not response.xpath("//a[@class='noactive' and @id='next']"):
            next_url = "https://hr.tencent.com/" + response.xpath("//a[@id='next']/@href").extract_first()

            yield scrapy.Request(url=next_url, callback=self.parse)
