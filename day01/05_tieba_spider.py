import requests


class TiebaSpider(object):
    def __init__(self):
        self.base_url = "http://tieba.baidu.com/f?"
        self.headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

        self.tieba_name = input("请输入需要采集的贴吧名:")
        self.start_page = int(input("请输入需要采集的起始页:"))  # 5
        self.end_page = int(input("请输入需要采集的结束页:"))    # 10


    def send_request(self, params):
        """ 发送请求，返回响应"""

        print("[INFO] : 正在发送请求..")
        response = requests.get(url=self.base_url, params=params, headers=self.headers)

        return response

    # def parse_response(self):
    #     pass

    def save_data(self, response, file_name):
        """ 接收响应，保存数据"""
        html = response.content

        with open(file_name, "wb") as f:
            f.write(html)


    def main(self):
        """ 调度中心，控制方法的调用和参数的传递"""
        for page in range(self.start_page, self.end_page + 1):
            pn = (page - 1) * 50
            # 构建查询字符串
            params = {"kw" : self.tieba_name, "pn" : pn}

            try:
                # 发送请求，获取响应
                response = self.send_request(params)
                # 构建文件名
                file_name = self.tieba_name + str(page) + ".html"
                # 保存响应数据
                self.save_data(response, file_name)

            except Exception as e:
                print("[ERROR] : 请求处理失败, {}".format(e))

        print("[INFO] : 谢谢使用!")


if __name__ == '__main__':
    spider = TiebaSpider()
    spider.main()



# 卖油翁：我亦无他，唯手熟尔。
