import random

import requests


# User-Agent池
# 代理IP池
# Cookie池

def send_request(url):

    ### 1. 没有添加请求报头，默认发送请求会暴露爬虫身份。
    # response = requests.get(url)
    # print(response.content)



    ### 2. 只包含了 User-Agent，可以伪装成一个浏览器
    headers = {
        # User-Agent 表示客户端身份
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"
    }


    # response = requests.get(url, headers=headers)
    # print(response.content)


    ### 3.  User-Agent 池随机切换使用
    # USER_AGENT_LIST = [
    #     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    #     "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    #     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    #     "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6"
    # ]

    # user_agent = random.choice(USER_AGENT_LIST)

    # headers = {"User-Agent" : user_agent}

    # response = requests.get(url, headers=headers)
    # print(response.request.headers)


    ### 4. 将所有请求报头全部添加，我们就是一个标准的浏览器请求
    headers = {
        "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Encoding" : "gzip, deflate, br",
        "Accept-Language" : "zh-CN,zh;q=0.9,en;q=0.8",
        "Cache-Control" : "max-age=0",
        "Connection" : "keep-alive",
        "Cookie" : "BAIDUID=11B445D89B86EE68539ED2CE0E08ACEF:FG=1; BIDUPSID=11B445D89B86EE68539ED2CE0E08ACEF; PSTM=1552984881; BD_UPN=12314753; H_PS_PSSID=1469_21109_28723_28557_28697_28585_28603_28606; delPer=0; BD_CK_SAM=1; PSINO=7; BD_HOME=0",
        "Host" : "www.baidu.com",
        "Upgrade-Insecure-Requests" : "1",
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"
    }
    # 附带了所有请求报头的请求，认为我们是一个标准的浏览器请求。
    response = requests.get(url, headers=headers)
    print(response.content)


if __name__ == '__main__':
    url = "http://www.baidu.com/"
    send_request(url)
