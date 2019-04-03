
import scrapy


class TencentItem(scrapy.Item):
    # 职位名
    position_name = scrapy.Field()
    # 详情链接
    position_link = scrapy.Field()
    # 职位类别
    position_type = scrapy.Field()
    # 招聘人数
    people_number = scrapy.Field()
    # 工作地点
    work_location = scrapy.Field()
    # 发布事件
    publish_times = scrapy.Field()


class DetailItem(scrapy.Item):
    # 职位职责
    position_zhize = scrapy.Field()
    # 职位要求
    position_yaoqiu = scrapy.Field()


class AllItem(scrapy.Item):
    # 职位名
    position_name = scrapy.Field()
    # 详情链接
    position_link = scrapy.Field()
    # 职位类别
    position_type = scrapy.Field()
    # 招聘人数
    people_number = scrapy.Field()
    # 工作地点
    work_location = scrapy.Field()
    # 发布事件
    publish_times = scrapy.Field()
    # 职位职责
    position_zhize = scrapy.Field()
    # 职位要求
    position_yaoqiu = scrapy.Field()

    # 爬虫名（数据源）
    spider = scrapy.Field()
    # 爬取时间
    time = scrapy.Field()
