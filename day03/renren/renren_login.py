import requests
import js2py
from lxml import etree

ssion = requests.session()


headers = {
    "Accept" : "*/*",
    "Accept-Encoding" : "gzip, deflate",
    "Accept-Language" : "zh-CN,zh;q=0.9,en;q=0.8",
    "Connection" : "keep-alive",
    "Content-Type" : "application/x-www-form-urlencoded",
    "Host" : "activity.renren.com",
    "User-Agent" : "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Mobile Safari/537.36",
    "X-Requested-With" : "XMLHttpRequest"
}
# 给ssion对象添加一个固定的请求报头
ssion.headers = headers


#1. 发送GET请求： http://activity.renren.com/livecell/rKey
print("[INFO]: 正在发送请求 {}".format("http://activity.renren.com/livecell/rKey"))
response = ssion.get("http://activity.renren.com/livecell/rKey")
n = response.json()['data']

#    n = json.loads(response.content)['data']

# 2.  提供账户名和密码
phoneNum = "maozhaojun@live.com"
password = "alarmchime"

# 3. 执行js：
#     三个js文件： Bigint.js 、RSA.js 、Barrett.js
#     一段js代码：

# 创建一个js运行环境
context = js2py.EvalJs()

context.execute(open("Bigint.js", "r").read())
context.execute(open("RSA.js", "r").read())
context.execute(open("Barrett.js", "r").read())

# 添加运行时需要的 t 和 n
context.t = {"password" : password}
context.n = n

js_str = '''t.password = t.password.split("").reverse().join(""), setMaxDigits(130);
var o = new RSAKeyPair(n.e,"",n.n), r = encryptedString(o, t.password);
t.password = r, t.rKey = n.rkey'''

# 4. 提取js执行结果，获取 password 和 rkey 登录参数：
context.execute(js_str)

print(context.t.password)
print(context.t.rKey)




# 5. 发送登录的POST请求： http://activity.renren.com/livecell/ajax/clog
data = {
    "phoneNum": phoneNum,
    "password": context.t.password,
    "c1": "0",
    "rKey": context.t.rKey
}

response = ssion.post("http://activity.renren.com/livecell/ajax/clog", data=data)
print(response.json())



ssion.headers = {
    #"Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    #"Accept-Encoding" : "gzip, deflate",
    #"Accept-Language" : "zh-CN,zh;q=0.9,en;q=0.8",
    "Connection" : "keep-alive",
    "Host" : "www.renren.com",
    "Referer" : "http://www.renren.com/327550029",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}

urls = [
    "http://www.renren.com/327550029/profile",
    "http://www.renren.com/410043129/profile",
    "http://www.renren.com/349881827/profile"
]

for index, url in enumerate(urls):
    print("[INFO]: 正在发送请求 {}".format(url))
    response = ssion.get(url)

    html_dom = etree.HTML(response.content.decode("utf-8"))
    title = html_dom.xpath("//title/text()")[0]
    print(title)

    with open(title + ".html", "wb") as f:
        f.write(response.content)
