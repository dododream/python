import requests


url = "http://www.baidu.com/"

error_urls = []

try:
    # 设置访问超时时限，如果在规定事件没有响应，则抛出异常
    #response = requests.get(url, timeout=0.003)
    response = requests.get(url, timeout=3)
except:
    # 如果请求出现一次，则记录该请求的url地址
    error_urls.append(url)

print(error_urls)
print(response)
