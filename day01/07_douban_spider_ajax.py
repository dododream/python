#import json
import requests


# json\xml\html\txt

def send_request():
    url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action="

    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    start = 0
    while True:
        # 构建查询字符串
        params = {"start" : start, "limit" : 100}
        # 发送请求
        response = requests.get(url, params=params, headers=headers)

        # 获取json字符串转为对应的Python数据类型
        movie_list = response.json()
        #movie_list = json.loads(response.content)

        # 当网页没有数据时，则退出循环（ []、{} ）
        if not movie_list:
            break

        for movie in movie_list:
            print(movie['title'])

        start += 100


if __name__ == '__main__':
    send_request()
