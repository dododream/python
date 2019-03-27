import requests


def send_request(url):

    response = requests.get(url)

    print(response.url)

    # 猜测网页的编码，可能猜不准
    print(response.encoding)

    # 如果猜不准，直接通过 encoding指定正确的编码
    response.encoding = "utf-8"
    # response.text 是通过 response.encoding 进行解码后的数据
    print(response.text)


    print(response.content)

    if response.status_code == 200:
        print("OK")

    # 响应报头（服务器给客户端）
    print(response.headers)

    # 响应对象 对应的请求对象 的url
    print(response.request.url)
    # 响应对象 对应的请求对象 的请求报头
    print(response.request.headers)
    # 响应对象 对应的请求对象 的请求方法
    print(response.request.method)

    # 获取响应的cookie
    print(response.cookies)
    # 响应对象 对应的请求对象的 cookie
    print(response.request._cookies)


if __name__ == '__main__':
    url = "http://www.baidu.com/"
    send_request(url)
