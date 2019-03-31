# scrapy genspider tencent1 hr.tencent.com

import scrapy
from ..items import TencentItem

class TencentSpider(scrapy.Spider):

    name = "tencent1"

    allowed_domains = ["hr.tencent.com"]

    # 固定url地址部分
    base_url = "https://hr.tencent.com/position.php?start="
    # 页码自增量
    page = 0

    start_urls = [base_url + str(page)]

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

        # 构建下一页的url地址
        if self.page < 3100:
            self.page += 10
            next_url = self.base_url + str(self.page)

            # url 表示发送请求的url地址
            # callback 表示请求发送成功后，返回的响应交给callback指定的 parse 进行解析（response做为参数传递给parse)
            yield scrapy.Request(url=next_url, callback=self.parse)

        # 2 mins



# ----


# def 下载器(url):
#     return response

# def parse(response):
#     return item

# def 管道(item):
#     pass

# def 引擎():
#     response = send_request(xxx)

#     item = parse_response(response)

#     save_data(item)


