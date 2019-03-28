# Python自带的测试模块

import time
import unittest
import json

from selenium import webdriver
from lxml import etree

# 继承与unittest的测试用例，表示创建一个测试用例
class DouyuSpider(unittest.TestCase):
    #def __init__(self)
    # 和 构造方法一样，用于初始化操作
    def setUp(self):
        # self.num = 1234
        self.driver = webdriver.PhantomJS()
        self.start_url = "https://www.douyu.com/directory/all"
        self.item_list = []
        self.page = 1

    # 中间的测试方法名，必须以 test开头
    def testDouyu(self):
        # print(self.num)
        # 打开网页
        self.driver.get(self.start_url)

        while True:
            # 获取网页渲染后的源码（字符串是 Unicode 类型)
            html = self.driver.page_source

            html_dom = etree.HTML(html)

            # 定位到 所有主播的大项
            ul_element = html_dom.xpath("//ul[@class='layout-Cover-list']")[1]

            # 提取所有主播的每一个主播信息，并返回列表（一页120个）
            div_list = ul_element.xpath('.//div[@class="DyListCover-content"]')


            for div in div_list:
                item = {}
                item['category_name'] = div.xpath(".//span[@class='DyListCover-zone']/text()")[0]
                item['room_name'] = div.xpath('.//h3[@class="DyListCover-intro"]/text()')[0]
                #print(item)
                try:
                    item['people_number'] = div.xpath(".//span[@class='DyListCover-hot']/text()")[0]
                except:
                    item['people_number'] = 0
                #print(item)
                item['directory_name'] = div.xpath('.//h2[@class="DyListCover-user"]/text()')[0]

                #print(item)
                self.item_list.append(item)

            # 在网页里查找最后一页的特征字符串，如果找到了返回小标，则不是-1，就退出循环
            if html.find("dy-Pagination-disabled dy-Pagination-next") != -1:
                break
            else:
                self.driver.find_element_by_class_name(" dy-Pagination-next").click()

            # if not html.find("dy-Pagination-disabled dy-Pagination-next") != -1:
            #     self.driver.find_element_by_class_name(" dy-Pagination-next").click()

            #如果带宽不稳定，多提供一秒渲染时间，数据才可以正常提取
            time.sleep(1)
            self.page += 1
            print(self.page)

    # 析构方法
    #def __del__(self)
    def tearDown(self):
        # print("delete num")
        # del(self.num)
        #print(self.item_list)


        # json_str = json.dumps(self.item_list, ensure_ascii=False)

        # with open("douyu.json", "w") as f:
        #     f.write(json_str)
        json.dump(self.item_list, open("douyu.json", "w"), ensure_ascii=False)


if __name__ == '__main__':
    unittest.main()
