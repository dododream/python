import requests


def login():
    # 这个是人人网一个隐藏接口，可以模拟登录，而且只需要账户名和密码即可
    url = "http://www.renren.com/PLogin.do"

    # 请求报头
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    # 表单数据
    data = {
        "email" : "mr_mao_hacker@163.com",
        "password": "ALARMCHIME"
    }

    # 创建一个可以保存会话的ssion对象（本质记录并换地Cookie）
    ssion = requests.session()

    ssion.headers = headers

    # 附带账户名和密码的 模拟登录请求， 如果登录成功则记录Cookie
    #requests.post(url, headers=headers, data=data)
    ssion.post(url, headers =headers, data=data)

    urls = [
        "http://www.renren.com/327550029/profile",
        "http://www.renren.com/410043129/profile",
        "http://www.renren.com/349881827/profile"
    ]

    for index, url in enumerate(urls):
        print("[INFO]: 正在发送请求 {}".format(url))
        response = ssion.get(url)

        with open(str(index) + ".html", "wb") as f:
            f.write(response.content)



if __name__ == '__main__':
    login()
