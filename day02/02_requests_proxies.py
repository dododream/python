import random

import requests


def send_request():
    url = "http://www.httpbin.org/ip"
    #url = "http://www.baidu.com/"

    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    # response = requests.get(url)
    # print(response.json())

    # 构建代理池，随机选择使用
    proxy_list = [
        # 免费代理：没有账户名和面膜
        #{"http" : "http://182.254.158.143:16816"},
        # 验证代理：需要提供账户名和密码，否则会报407（requests默认没有使用代理）
        {"http" : "http://maozhaojun:ntkn0npx@182.254.158.143:16816"},

        {}
    ]

    proxies = random.choice(proxy_list)


    response = requests.get(url, proxies=proxies)
    #print(response.json())
    print(response.content)



if __name__ == '__main__':
    send_request()
