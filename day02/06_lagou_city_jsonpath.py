import requests
from jsonpath import jsonpath


def send_request():
    url = "https://www.lagou.com/lbs/getAllCitySearchLabels.json"
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}


    response = requests.get(url, headers=headers)
    result = response.json()

    #print(result)
    city_list = jsonpath(result, "$..name")
    id_list = jsonpath(result, "$..id")
    # [xx, xx, xx]
    # [11, 22, 33]
    # print(city_list)
    # print(id_list)

    # item_list = [{id_list[index] : city} for index, city in enumerate(city_list)]
    # print(item_list)

    # zip() 合并 内置方法
    print(dict(zip(id_list, city_list)))


if __name__ == '__main__':
    send_request()
