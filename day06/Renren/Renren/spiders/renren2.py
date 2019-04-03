#coding:utf-8

import scrapy


class RenrenSpider(scrapy.Spider):
    name = "renren2"

    allowed_domains = ["renren.com"]

    #start_urls = []

    # 模拟登录请求：POST请求，如果登录成功scrapy会记录Cookie
    def start_requests(self):
        post_url = "http://www.renren.com/PLogin.do"

        #scrapy.Reqeust(url, callback)  GET请求
        # 表单数据
        formdata = {
            "email" : "mr_mao_hacker@163.com",
            "password": "ALARMCHIME"
        }

        # FormRequest就是scrapy的post请求
        yield scrapy.FormRequest(url=post_url, formdata=formdata, callback=self.parse)


    # scrapy发送其他页面的请求，会附带之前记录的Cookie
    def parse(self, response):

        friend_urls = [
            "http://www.renren.com/327550029/profile",
            "http://www.renren.com/410043129/profile",
            "http://www.renren.com/349881827/profile"
        ]
        for url in friend_urls:
            yield scrapy.Request(url, callback=self.parse_friend)

    # 解析需要登录权限才可以访问的页面响应内容
    def parse_friend(self, response):
        title = response.xpath("//title/text()").extract_first()
        print(title)
