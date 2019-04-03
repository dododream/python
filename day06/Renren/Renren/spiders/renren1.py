#coding:utf-8

import scrapy


class RenrenSpider(scrapy.Spider):
    name = "renren1"
    allowed_domains = ["renren.com"]

    start_urls = [
        "http://www.renren.com/327550029/profile",
        "http://www.renren.com/327550029/profile",
        "http://www.renren.com/327550029/profile",
        "http://www.renren.com/327550029/profile",
        "http://www.renren.com/327550029/profile",
        "http://www.renren.com/327550029/profile",
        "http://www.renren.com/410043129/profile",
        "http://www.renren.com/349881827/profile"
    ]

    headers = {
        #"Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        #"Accept-Encoding" : "gzip, deflate",
        #"Accept-Language" : "zh-CN,zh;q=0.9,en;q=0.8",
        #"Cache-Control" : "max-age=0",
        #"Connection" : "keep-alive",
        #"Host" : "www.renren.com",
        "Referer" : "http://renren.com/",
        # "Upgrade-Insecure-Requests" : "1",
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
    }

    cookies = {
        "anonymid" : "jtp3s6zf3s97ed",
        "_r01_" : "1",
        "_ga" : "GA1.2.1978216666.1553760551",
        "_uij" : "JTdCJTIydXNlcklkJTIyJTNBMzI3NTUwMDI5JTJDJTIydXNlck5hbWUlMjIlM0ElMjIlRTYlQUYlOUIlRTUlODUlODYlRTUlODYlOUIlMjIlMkMlMjJoZWFkRnVsbFVybCUyMiUzQSUyMmh0dHAlM0ElMkYlMkZoZG4ueG5pbWcuY24lMkZwaG90b3MlMkZoZG41MjElMkYyMDE5MDMyNiUyRjA5MzAlMkZoZWFkX2tnZ0lfMThjYjAwMDAyMjY3MTk4Ni5qcGclMjIlMkMlMjJnZW5kZXIlMjIlM0ElMjIlRTclOTQlQjclRTclOTQlOUYlMjIlMkMlMjJsb2dDb3VudCUyMiUzQTYxNSUyQyUyMmNvZGUlMjIlM0EwJTdE",
        "depovince" : "GW",
        "jebecookies" : "75ccdc8c-d7d9-45c1-89c8-94efc9f7542f|||||",
        "ick_login" : "5cfdc1e2-cf9f-422f-a54f-a34518e834a8",
        "_de" : "BF09EE3A28DED52E6B65F6A4705D973F1383380866D39FF5",
        "p" : "76439b2ffea3251142dce5701cdb50959",
        "first_login_flag" : "1",
        "ln_uact" : "mr_mao_hacker@163.com",
        "ln_hurl" : "http://hdn.xnimg.cn/photos/hdn521/20190326/0930/main_V1St_81d40000bf431986.jpg",
        "t" : "c74873a2f270d7285a30edb8ca284a0c9",
        "societyguester" : "c74873a2f270d7285a30edb8ca284a0c9",
        "id" : "327550029",
        "xnsid" : "1ea79812",
        "ver" : "7.0",
        "loginfrom" : "null",
        "JSESSIONID" : "abc0xehw0ztxf9PIgwHNw",
        "wp_fold" : "0"
    }


    # 重写start_reqeusts方法，给start_urls的每个请求添加一个cookies和headers
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, cookies=self.cookies, headers=self.headers, dont_filter=True)
    # 1. dont_filter表示请求是否经过调度器指纹过滤，默认为False表示记录指纹并过滤
    # 2. 可以在构建请求时手动改为 dont_filter=True，表示该请求不做记录和过滤
    # 3. 通常用于配合time.sleep() 定时抓取某个固定页面的增量数据。


    def parse(self, response):
        title = response.xpath("//title/text()").extract_first()
        print(title)
