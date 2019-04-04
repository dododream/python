#coding:utf-8

import re
import json
import time
import base64

import requests

from process_captcha import get_captcha


username= "18335456020"
password = "13753885935JWQ"

# 创建session对象，用来保存Cookie会话
ssion = requests.session()

ssion.headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}

# 处理前置Cookie
url = "https://www.12306.cn/index/"
ssion.get(url)

# 前置Cookie处理
url = "https://kyfw.12306.cn/otn/HttpZF/GetJS"
ssion.get(url)

# 前置Cookie处理
url = "https://kyfw.12306.cn/otn/login/userLogin"
ssion.get(url)

# 前置Cookie处理
url = "https://kyfw.12306.cn/otn/passport?redirect=/otn/login/userLogin"
ssion.get(url)

# 前置Cookie处理
url = "https://kyfw.12306.cn/passport/web/auth/uamtk"
response = ssion.post(url, data={"appid" : "otn"})
print(response.json())
print("--" * 10)


# 前置Cookie处理
url = "https://kyfw.12306.cn/otn/HttpZF/logdevice?algID=stlPYD4gpV&hashCode=BV1VUAalJflc9BGJsDoJzfV89vQ2WRAF2JZmPiOu9fc&FMQw=0&q4f3=zh-CN&VPIf=1&custID=133&VEek=unknown&dzuS=0&yD16=0&EOQP=629e410049ce6e9622598e273c4148f5&lEnu=184419499&jp76=52d67b2a5aa5e031084733d5006cc664&hAqN=Win32&platform=WEB&ks0Q=d22ca0b81584fbea62237b14bd04c866&TeRS=810x1251&tOHY=24xx840x1251&Fvje=i1l1o1s1&q5aJ=-8&wNLf=99115dfb07133750ba677d055874de87&0aew=Mozilla/5.0%20(Windows%20NT%2010.0;%20Win64;%20x64)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/73.0.3683.86%20Safari/537.36&E3gR=d591107e7085c8fc4f1221d9fdca3fc9&timestamp={}".format(int(time.time() * 1000))

response = ssion.get(url)
result = json.loads(re.search("'(.*?)'", response.text).group(1))
print(result)

# 给ssion对象添加Cookie（通过json文件中提取并设置）
ssion.cookies.set("RAIL_EXPIRATION", result['exp'])
ssion.cookies.set("RAIL_DEVICEID", result['dfp'])

print("--" * 10)

# 前置Cookie处理
url = "https://kyfw.12306.cn/otn/login/conf"
response = ssion.post(url, data={})
print(response.json())
print("--" * 10)

# 前置Cookie处理
url = "https://kyfw.12306.cn/otn/index12306/getLoginBanner"
response = ssion.get(url)
print(response.json())
print("--" * 10)

# 前置Cookie处理
url = "https://kyfw.12306.cn/passport/web/auth/uamtk-static"
ssion.post(url, data={"appid" : "otn"})
print(response.json())
print("--" * 10)

# 获取ssion中已经保存的的Cookie
print(ssion.cookies.get_dict())



# 获取验证码图片
url = "https://kyfw.12306.cn/passport/captcha/captcha-image64?login_site=E&module=login&rand=sjrand&{}&_={}".format(int(time.time() * 1000), int(time.time() * 1000))

response = ssion.get(url)
image_base64_str = response.json()['image']
image_bytes = base64.b64decode(image_base64_str)

print("保存验证码图片...")
with open("captcha.jpg", "wb") as f:
    f.write(image_bytes)

# 预先设置的坐标值
answer_index_dict = {
    "1" : "32,35,",
    "2" : "102,33,",
    "3" : "171,35,",
    "4" : "247,31,",
    "5" : "33,105,",
    "6" : "105,102,",
    "7" : "177,108,",
    "8" : "250,110,",
}

# 获取验证码编号
captcha_type = int(input("请选择验证码处理模式：输入 1 打码平台, 其他表示手动处理："))
if captcha_type == 1:
    answer_index = get_captcha("./captcha.jpg")
else:
    answer_index = input('请输入验证码的编码（连续输入数字 135) ： ')

print("验证码编号为 : {}".format(answer_index))

# 根据验证码编号 计算验证码的坐标值
answer = ""
for index in answer_index:
    answer += answer_index_dict[index]
answer = answer[:-1]
print(answer)


# 验证码answer值校验
url = "https://kyfw.12306.cn/passport/captcha/captcha-check?answer={}&rand=sjrand&login_site=E&_={}".format(answer, int(time.time() * 1000))
response = ssion.get(url)
print(response.json())


# 模拟登录
url = "https://kyfw.12306.cn/passport/web/login"
data= {
    "username" : username,
    "password" : password,
    "appid" : "otn",
    "answer" : answer
}
response = ssion.post(url, data=data)
print(response.json())


#------- 登陆成功 -----------
