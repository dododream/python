import re
import json

import requests

url = "https://www.12306.cn/index/script/core/common/station_name_v10026.js"


headers = {
    "Host": "www.12306.cn",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8"
}

js_str = requests.get(url, headers=headers).text

station_str = re.search("'(.*?)'", js_str).group(1)[1:]

station_list = station_str.split("@")

station_info_dict = {station.split("|")[1] : station.split("|")[2] for station in station_list}

with open("station_info.py", "w") as f:
    f.write("station_info_dict = ")
    f.write(json.dumps(station_info_dict, ensure_ascii=False))




