# 列表页： url = "http://tieba.baidu.com/f?"
#     params = {"kw" : xxx, "pn" : (page - 1) * 50}

#     提取详情页xpath("//a[@class='j_th_tit']/@href")

# 详情页： 提取图片的连接xpath("//img[@class='BDE_Image']/@src")

# 图片： 直接 按 wb 保存即可。


import requests
from lxml import etree


class TiebaSpider(object):
    def __init__(self):
        self.base_url = "http://tieba.baidu.com"
        self.headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

        self.tieba_name = input("请输入需要采集的贴吧名:")
        self.start_page = int(input("请输入需要采集的起始页:"))
        self.end_page = int(input("请输入需要采集的结束页:"))



    def send_request(self, url, params={}):
        """ 发送url请求，并返回响应"""
        print("[INFO]: send request [{}] <{}>".format("GET", url))
        response = requests.get(url, headers=self.headers, params=params)
        return response


    def parse_detail(self, response):
        """ 提取 并 返回所有连接详情页的连接 """
        html = response.content
        #print(len(html))
        html_dom = etree.HTML(html)

        url_list = html_dom.xpath("//a[@class='j_th_tit ']/@href")

        return url_list



    def parse_image(self, response):
        """ 提取 并 返回所有连接图片的连接 """
        html = response.content
        html_dom = etree.HTML(html)

        url_list = html_dom.xpath("//img[@class='BDE_Image']/@src")
        #print(url_list)
        return url_list


    def save_image(self, response, file_name):
        """ 保存所有图片数据 """
        print("[INFO] : Save image <{}>".format(file_name))
        with open("./Images/" + file_name, "wb") as f:
            f.write(response.content)


    def main(self):
        """ 调度中心，控制各个方法的执行并传递参数"""

        ## 第一级for： 处理所有列表页的请求
        for page in range(self.start_page, self.end_page + 1):
            pn = (page - 1) * 50

            params = {"kw" : self.tieba_name, "pn" : pn}
            url = self.base_url + "/f?"

            try:
                response = self.send_request(url, params)

                detail_url_list = self.parse_detail(response)
                ## 第二级for ： 处理所有详情页的请求
                for detail_url in detail_url_list:
                    response = self.send_request(self.base_url + detail_url)
                    image_url_list = self.parse_image(response)

                    ## 第三级for： 处理所有图片的请求
                    for image_url in image_url_list:
                        response = self.send_request(image_url)
                        # 保存图片数据
                        self.save_image(response, image_url[-15:])

            except Exception as e:
                print("[ERROR]: Bad Request {}".format(e) )


if __name__ == '__main__':
    spider = TiebaSpider()
    spider.main()

