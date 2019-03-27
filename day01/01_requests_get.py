import requests

# 发送请求的url地址（通常用http即可）
url = "http://www.baidu.com/"

# 发送url地址请求，并获取对应的响应 response对象
response = requests.get(url)

# 返回响应的url地址
# response.url


# 返回响应 Unicode编码的字符串 （str ： 网页Unicode字符串)
unicode_str = response.text

# 返回响应 非Unicode编码的字符串 ( bytes : 网页原始编码字符串、图片、音频、视频、其他二进制数据 )
non_unicode_str = response.content

# reqeusts模块猜测的编码并进行解码，可能不准
#response.text

# 返回Unicode编码字符串， 手动按网页的 charset 值 通过 decode() 解码处理（一定正确）
#response.content.decode()

with open("xxx.html", "w") as f:
    f.write(unicode_str)


with open("xxx.html", "wb") as f:
    f.write(non_unicode_str)




