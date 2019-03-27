import time
import urllib.parse

import requests
from jsonpath import jsonpath


def send_request():
    # url
    url = "https://fanyi.qq.com/api/translate"

    # headers
    headers = {
        "Accept" : "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding" : "gzip, deflate, br",
        "Accept-Language" : "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection" : "keep-alive",
        # 1. 表示传递的表单数据的字节长度
        "Content-Length" : "281",
        # 2. 表示传递的表单数据类型是 urlencode编码字符串
        "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie" : "fy_guid=e76f8fef-53c8-4b32-aaf2-3d21eb0288df; gr_user_id=c0a1cf7a-5479-4fc0-9a44-0b67b4ac68ff; grwng_uid=332768af-7822-4242-95a8-8d08440d6291; pgv_pvid=1765002192; pac_uid=0_e6e69de3645c8; qtv=2e85bb0d8599fc8d; qtk=L0oIpEAiOLPEG6FKBLPu9o56aGJc2rred6H3dJDZ4EQ6O+i0u38ywcjwahYIWQvl0K0K7lT5lcv7NjKtLxnfSoSbaRoHCrjJ6VYymzjw+IEOsv6mDmJKLKqsIgFBpqEVmssaG0cApWet+h2vxaFx+A==; openCount=1; 9c118ce09a6fa3f4_gr_session_id=f1e350b1-3619-49be-967f-4526bfd6c110; 8c66aca9f0d1ff2e_gr_session_id=25aba013-b28d-4811-bf9a-f09a9c3a6792; 8c66aca9f0d1ff2e_gr_session_id_25aba013-b28d-4811-bf9a-f09a9c3a6792=true",
        "Host" : "fanyi.qq.com",
        "Origin" : "https://fanyi.qq.com",
        "Referer" : "https://fanyi.qq.com/",
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
        #3. 表示该请求是一个 ajax 请求
        "X-Requested-With" : "XMLHttpRequest"
    }

    # params、 formdata
    data = {
        "source" : "auto",
        "target" : "auto",
        "sourceText" : input("请输入需要翻译的文本："),
        "qtv" : "2e85bb0d8599fc8d",
        "qtk" : "L0oIpEAiOLPEG6FKBLPu9o56aGJc2rred6H3dJDZ4EQ6O+i0u38ywcjwahYIWQvl0K0K7lT5lcv7NjKtLxnfSoSbaRoHCrjJ6VYymzjw+IEOsv6mDmJKLKqsIgFBpqEVmssaG0cApWet+h2vxaFx+A==",
        "sessionUuid" : "translate_uuid"+ str(int(time.time() * 1000))
    }

    # 如果网站非常严格，检查了Content-Length值是否是合理的长度，可以手动处理表单数据的长度
    # form_data_str = urllib.parse.urlencode(data)
    # headers['Content-Length'] = len(form_data_str)

    # 发送 附带表单数据的 post请求
    response = requests.post(url, headers=headers, data=data)
    # 获取响应的json字符串，并转为对应的Python数据类型
    result = response.json()
    #result = json.loads(response.content)

    # 根据字典下标取值
    #trans_text = result['translate']['records'][0]['targetText']
    trans_text = jsonpath(result, "$..targetText")   [0]

    print(trans_text)


if __name__ == '__main__':
    send_request()
