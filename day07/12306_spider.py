#coding:utf-8

import re
import json
import time
import base64
from datetime import datetime

import requests

from process_captcha import get_captcha
from station_info import station_info_dict
from process_train import train_info


username= "15116964525"
password = "1234qwer5"

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
result = response.json()
print(result)


#------- 登陆成功 后 个人中心的请求处理-----------


# 登录后的请求
url = "https://kyfw.12306.cn/otn/passport?redirect=/otn/login/userLogin"
ssion.get(url)

#cookie 处理
url = "https://kyfw.12306.cn/passport/web/auth/uamtk"
response = ssion.post(url, data = {"appid" : "otn"})
print(response.json())
tk = response.json()['newapptk']

# 用户验证处理
url = "https://kyfw.12306.cn/otn/uamauthclient"
response = ssion.post(url, data= {"tk" : tk})
print(response.json())


# 进入到登录后的个人中心页面
url = "https://kyfw.12306.cn/otn/view/index.html"
ssion.get(url)

# 登录用户的验证信息
url = "https://kyfw.12306.cn/otn/login/conf"
response = ssion.post(url, data={})
print(response.json())

url = "https://kyfw.12306.cn/otn/index/initMy12306Api"
response = ssion.post(url, data={})
print(response.json())




#------- 用户提供出发时间、出发站和到达站，并提交请求获取车次信息

url = "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc"
ssion.get(url)


train_date = input("请输入出发时间（格式如: 2019-04-10): ")
from_station = input("请输入出发站站名:")
to_station = input("请输入到达站站名:")

# 提交 车次查询信息请求
url = "https://kyfw.12306.cn/otn/leftTicket/query?"
params = {
    # 出发时间
    "leftTicketDTO.train_date" : train_date,
    # 出发站
    "leftTicketDTO.from_station" : station_info_dict[from_station],
    # 结束站
    "leftTicketDTO.to_station" : station_info_dict[to_station],
    "purpose_codes" : "ADULT",
}

response = ssion.get(url, params=params)
result = response.json()["data"]["result"]

train_info_list = train_info(result)

#print(train_info_list)

print("可以选择的车次如下：")
for train_info in train_info_list:
    print(train_info['stationTrainCode'], end=", ")

index = int(input("请输入需要选择的下标（从0开始）："))
print("选择的车次信息：")
train_info = train_info_list[index]
print(train_info)



# 坐席类型与代号 的字典
seat_type_dict = {
    "erdengzuo": "O",  # 二等座
    "yingwo": "3",  # 硬卧
    "yingzuo": "1",  # 硬座
    "wuzuo": "1",  # 无座
    "ruanwo": "4",  # 软卧
    "ruanzuo": "2",  # 软座
    "dongwo": "F",  # 动卧
    "yidengzuo": "M",  # 一等座
    "gaojiruanwo": "6",  # 高级软座
    "shangwuzuo": "9",  # 商务座
    "tedengzuo": "P",  # 特等座
}

seat_type = input("请输入需要选择乘坐的坐席类型（拼音)：")
# 座位类型代号，用于后续提交购票时的表单数据
seat = seat_type_dict[seat_type]



### -- 开始预定车票
# 检查用户状态
url = "https://kyfw.12306.cn/otn/login/checkUser"
ssion.post(url, data = {"_json_att" : ""})


# 提交选票请求
url = "https://kyfw.12306.cn/otn/leftTicket/submitOrderRequest"
data = {
    "secretStr" :  train_info['secretStr'],
    "train_date" : train_date,
    "back_train_date" : train_date,
    "tour_flag" : "dc",
    "purpose_codes" : "ADULT",
    "query_from_station_name" : from_station,
    "query_to_station_name" : to_station,
    "undefined" : ""
}

response = ssion.post(url, data=data)
print(response.json())





# 获取一个加密的 token值
url = "https://kyfw.12306.cn/otn/confirmPassenger/initDc"
data = {"_json_att" : ""}
response = ssion.post(url, data=data)
#var globalRepeatSubmitToken = 'dd9c6abaa0dab67cdf17ed08c722cace'

# 从响应中提取 加密的token值
token = re.search("var globalRepeatSubmitToken = '(.*?)'", response.text).group(1)
key_check_isChange = re.search("key_check_isChange':'(.*?)'", response.text).group(1)
leftTicketStr = re.search("leftTicketStr':'(.*?)'", response.text).group(1)

# 获取所有乘车人信息
url  = "https://kyfw.12306.cn/otn/confirmPassenger/getPassengerDTOs"
data = {
    "_json_att" : "",
    "REPEAT_SUBMIT_TOKEN" : token,
}

response = ssion.post(url, data=data)
passenger_info_list = response.json()['data']['normal_passengers']

print("下列是所有乘车人姓名:")
#print(passenger_info_list)
for passenger_info in passenger_info_list:
    print(passenger_info['passenger_name'], end=", ")

index = int(input("请选择乘车人信息(下标从0开始)："))
# 选择的乘车人信息（从所有乘车人信息里根据下标选取）
passenger_info_dict = passenger_info_list[index]



# 检查提交的乘车人状态
url = "https://kyfw.12306.cn/otn/confirmPassenger/checkOrderInfo"

# 乘车人与坐席信息
passengerTicketStr = '%s,0,1,%s,%s,%s,%s,N' % (
            # 坐席类型代号
            seat,
            # 姓名
            passenger_info_dict['passenger_name'],
            # 证件类型编号（1 身份证）
            passenger_info_dict['passenger_id_type_code'],
            # 证件号码
            passenger_info_dict['passenger_id_no'],
            # 手机号
            passenger_info_dict['mobile_no'])
# 乘车人信息
oldPassengerStr = '%s,%s,%s,1_' % (
            # 姓名
            passenger_info_dict['passenger_name'],
            # 证件类型编号（1 身份证）
            passenger_info_dict['passenger_id_type_code'],
            # 证件号码
            passenger_info_dict['passenger_id_no'])



# oldPassengerStr = "靳文强,1,142303199512240614,1_"
# passengerTicketStr =  "O,0,1,靳文强,1,142303199512240614,18335456020,N"


data = {
    "_json_att":"", # 空值
    "bed_level_order_num":"000000000000000000000000000000",  # 固定值，含义位置
    "cancel_flag":"2",
    "oldPassengerStr": oldPassengerStr,
    "passengerTicketStr": passengerTicketStr,
    "randCode":"", # 空值
    "REPEAT_SUBMIT_TOKEN": token,
    "tour_flag":"dc",
    "whatsSelect":"1",
}

response = ssion.post(url, data=data)
print(response.json())






## -- 检查正在购票的队列人数（表示是否有余票可以购买）

week_name_list  = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
month_name_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# train_date = "2019-04-10"
# [int(n) for n in train_date.split("-")]
#         ["2019", "04", "10"]

year, month, day = map(int, train_date.split("-"))
week_index = datetime(year, month, day).weekday()

# 按指定个数获取 GMT时间格式
train_date = "{} {} {} {} 00:00:00 GMT+0800 (中国标准时间)".format(week_name_list[week_index], month_name_list[month-1], day, year)


url = "https://kyfw.12306.cn/otn/confirmPassenger/getQueueCount"
data = {
    "_json_att":"",
    "fromStationTelecode" : train_info['stationTrainCode'],
    "leftTicket" : train_info['leftTicket'],
    "purpose_codes" : "00",
    "REPEAT_SUBMIT_TOKEN" : token,
    "seatType" : seat,
    "stationTrainCode" :  train_info['stationTrainCode'],
    "toStationTelecode" : train_info['end_station'],
    "train_date" : train_date,
    "train_location": train_info['train_location'],
    "train_no": train_info["train_no"]
}

response = ssion.post(url, data=data)
print(response.json())



## 点击选座信息，并提交购票订单
url = "https://kyfw.12306.cn/otn/confirmPassenger/confirmSingleForQueue"
data = {
    "_json_att" : "",
    "choose_seats" : "1C",
    "dwAll" : "N",
    "key_check_isChange" : key_check_isChange,
    "leftTicketStr" : leftTicketStr,
    "oldPassengerStr" : oldPassengerStr,
    "passengerTicketStr" : passengerTicketStr,
    "purpose_codes" : "00",
    "randCode" : "",
    "REPEAT_SUBMIT_TOKEN" : token,
    "roomType" : "00",
    "seatDetailType" : "000",
    "train_location" : train_info['train_location'],
    "whatsSelect" : "1",
}

response = ssion.post(url, data=data)
print(response.json())


# 获取购票队列等待信息，同时在响应中提取 waitTime， ordId
url = "https://kyfw.12306.cn/otn/confirmPassenger/queryOrderWaitTime?"
params = {
    "random": str(int(time.time() * 1000)),
    "tourFlag":"dc",
    "_json_att" :"",
    "REPEAT_SUBMIT_TOKEN" : token,
}

response = ssion.get(url, params=params)
waitTime = response.json()['data']['waitTime']

if waitTime > -1:
    time.sleep(waitTime)
    response = ssion.get(url, params=params)

print(response.json())


# 购票请求，下单提交
# print("正在购票下单...")
# url = "https://kyfw.12306.cn/otn/confirmPassenger/resultOrderForDcQueue"
# data = {
#     "_json_att" : "",
#     "orderSequence_no":response.json()['data']['orderId'],
#     "REPEAT_SUBMIT_TOKEN": token,
# }
# response = ssion.post(url, data=data)
# print(response.json())
