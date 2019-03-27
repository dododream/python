import requests

def send_request(keyword):
    # 固定的url地址部分
    base_url = "https://www.baidu.com/s?"

    # 请求报头
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    # 查询字符串参数
    params = {"wd" : keyword}

    # 发送附带请求报头和 查询字符串的请求
    response = requests.get(base_url, headers=headers, params=params)

    # query_str = urllib.parse.urlencode(params)

    print(response.content)


    with open("baidu.html", "wb") as f:
        f.write(response.content)


if __name__ == '__main__':
    keyword = input("请输入需要查询的关键字:")
    send_request(keyword)

