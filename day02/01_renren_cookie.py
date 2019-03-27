import requests

def send_request():
    urls = [
        "http://www.renren.com/327550029/profile",
        "http://www.renren.com/410043129/profile",
        "http://www.renren.com/349881827/profile"
    ]

    ### 1. headers中的Cookie

    # Cookie池构建多个用户的cookie， 并且定期维护cookie
    # 并给每个cookie添加索引，对于失效的cookie进行修改维护
    # Cookie 池 也是爬虫非常常用的一种抓取方案（直接获取需要登录才能访问的页面数据）
    # headers = {
    #     "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    #     "Accept-Encoding" : "gzip, deflate",
    #     "Accept-Language" : "zh-CN,zh;q=0.9,en;q=0.8",
    #     "Cache-Control" : "max-age=0",
    #     "Connection" : "keep-alive",
    #     # 包含了登录状态的cookie，可以直接访问需要登录才可以访问的页面
    #     # Cookie属于个人隐私，不要轻易暴露。
    #     "Cookie" : "xxxx",
    #     "Host" : "www.renren.com",
    #     "Referer" : "http://www.renren.com/327550029",
    #     "Upgrade-Insecure-Requests" : "1",
    #     "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"
    # }



    ### 2. cookies参数
    headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"
    }

    cookies = {
        "anonymid" : "jtp3s6zf3s97ed",
        "depovince" : "GW",
        "_r01_" : "1",
        "ick_login" : "785696c7-437d-4ab6-ab46-05c9c892122e",
        "jebecookies" : "1d92d6cc-8009-4515-804f-a1b71a5df62c|||||",
        "_de" : "BF09EE3A28DED52E6B65F6A4705D973F1383380866D39FF5",
        "p" : "896d9458e12e9999125b88f0acd0b01f9",
        "first_login_flag" : "1",
        "ln_uact" : "mr_mao_hacker@163.com",
        "ln_hurl" : "http://hdn.xnimg.cn/photos/hdn121/20190306/2055/main_2vBS_0a7c00002444195a.jpg",
        "t" : "bad40552417099988d509bdb57fe61289",
        "societyguester" : "bad40552417099988d509bdb57fe61289",
        "id" : "327550029",
        "xnsid" : "48610933",
        "ver" : "7.0",
        "loginfrom" : "null",
        "JSESSIONID" : "abcd1CWjS6Ejhc-CVN3Mw",
        "wp_fold" : "0"
    }

    for index, url in enumerate(urls):
        print("[INFO]： 正在发送请求 {}".format(url))
        # 第一种用法：将Cookie放到请求报头的headers中（更简单）
        #response = requests.get(url, headers=headers)
        # 第二种用法：单独添加cookies参数，处理cookie（更方便管理）
        response = requests.get(url, headers=headers, cookies=cookies)


        with open(str(index) + ".html", "wb") as f:
            f.write(response.content)



if __name__ == '__main__':
    send_request()
