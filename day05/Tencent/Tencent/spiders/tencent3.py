# scrapy genspider tencent1 hr.tencent.com

import scrapy
from ..items import TencentItem

class TencentSpider(scrapy.Spider):

    name = "tencent3"

    allowed_domains = ["hr.tencent.com"]

    #start_urls = [base_url + str(page)]

    # 就所有需要发送的url地址，全部保存到start_urls中，这样可以充分利用scrapy的高并发。
    start_urls = ["https://hr.tencent.com/position.php?start=" + str(page) for page in range(0, 3101, 10)]

    # 这个方法是继承scrapy.Spider父类的方法，爬虫启动后，会第一时间调用 start_requests生成器，将statr_urls列表里的每个url构建请求对象，并全部放入调度器中。
    # 同时注意：start_urls里的请求默认不过滤（不记录请求指纹，重复的也可以发，而且不受allowed_domians过滤）
    # 该方法可以重写，子类覆盖父类的同名方法（用来给每个请求添加cookies，或者post请求）

    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield scrapy.Request(url, callback=self.parse, dont_filter=True)

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


        # 2 mins

