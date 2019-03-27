# url = "https://www.neihan8.com/article/list_5_{}.html".format(page) page =1 page += 1


# page_pattern = re.compile('<div class="f18 mb20">(.*?)</div>')
# content_list = page_pattern.findall(html)
# div_list = html_dom.xpath("//div[@class='f18 mb20']")

# for div in div_list:
#     contentdiv.xpath(".//text()")


import re

import requests


class NeihanSpider(object):
    def __init__(self):
        self.base_url = "https://www.neihan8.com/article/list_5_{}.html"
        self.headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        self.page = 1

        # 匹配所有段子数据
        self.page_pattern = re.compile('<div class="f18 mb20">(.*?)</div>', re.S)
        # 清洗数据，去除无用字符
        self.content_pattern = re.compile("\s|<.*?>|&.*?;")


    def send_request(self, url):
        response = requests.get(url, headers=self.headers)
        return response


    def parse_response(self, response):
        #print(response.content)
        html = response.content.decode("gbk")
        # 匹配数据
        content_list = self.page_pattern.findall(html)
        return content_list


    def save_data(self, content_list):
        # for content in content_list:
        #     with open("duanzi.txt", "a") as f:

        with open("duanzi.txt", "a") as f:
            f.write("第{}页:\n".format(self.page))
            for content in content_list:
                # 清洗数据
                new_content = self.content_pattern.sub("", content)
                f.write(new_content)
                f.write("\n\n")


    def main(self):
        # while True:
        #     command = input("请输入回车继续采集（输入Q则退出):")
        #     if command == 'q':
        #         break
        while input("请输入回车继续采集（输入Q则退出):").upper() != 'Q':
            # 构建每一页的 url地址
            url = self.base_url.format(self.page)

            response = self.send_request(url)
            content_list = self.parse_response(response)
            self.save_data(content_list)

            self.page += 1



if __name__ == '__main__':
    spider = NeihanSpider()
    spider.main()
