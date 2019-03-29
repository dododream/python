

--------------------------------------------------------

第一天：

--------------------------------------------------------




Python课程就业方向：
1. Web - Python高级、Flask、Django
2. 数据科学：
    -1. 数据采集系统：数据采集、数据提取、数据入库（爬虫系统）
    -2. 数据分析： 数据入库后 - 数据脱敏、清洗、数据计算、数据分析、数据可视化
    -3. AI： 数据建模、数据训练（数据挖掘、推荐系统、机器学习、深度学习）

#大数据 ： 对海量数据的存储、查询检索的一套技术。 Java
#数据分析 ： 对数据的分析、计算处理。   Scala、 R+MATLAB
#Python 开源免费的，大量中小企业公司都是用开源产品来处理数据。
#图灵测试。


1. 爬虫是如何采集网页数据的：

    网页的三大特征:
    -1. 每个网页都有自己的 URL（统一资源定位符）地址来进行网络定位。
    -2. 每个网页都使用 HTML（超文本标记语言）来描述页面信息。
    -3. 网页都使用 HTTP（超文本传输协议）来传递 HTML数据。


    爬虫的设计流程：
    -1. 爬虫通过网页的 URL地址，发送对应的HTTP请求给网站服务器。
    -2. 网站服务器返回对应的 HTTP 响应给爬虫，爬虫提取响应中的 HTML 数据内容。
    -3. 通过相关的HTML解析工具，提取HTML里的数据：
        -a. 如果是需要保存的目标数据，则根据需求保存数据（入库：txt、json、csv、mysql、redis、mongodb）
        -b. 如果是需要继续抓取的新的 URL地址，则从第一步重新开始执行。
    -4. 当所有的URL地址全部抓取完毕，程序结束。

    爬虫的主要两个瓶颈：硬件瓶颈（CPU、内存）、带宽瓶颈（网速）

    90%的网站没有反爬
    10%的网站有反爬 -> 90%的反爬可以通过更改IP代理解决
                  -> 10%的高级反爬：验证码、JS加密、动态渲染

    毛主席说过：战略上藐视，战术上重视。
    只要是用户可以访问的网络数据，爬虫都可以爬下来。


    Baidu每天处理的用户数据量大约 20EB


    1 bytes = 8 bit
    1024 bytes = 1KB
    1024 KB = 1 MB
    1024 MB = 1 GB
    1024 GB = 1 TB
    1024 TB = 1 PB
    1024 PB = 1 EB
    1024 EB = 1 ZB

    搜索引擎的排名算法：page rank（Google）、超链分析（Baidu）




2. 什么是字符编码？

    -1 计算机里的所有数据，本质都是二进制数。

        # 纸带打孔机、汇编、C - C++、Java、C#、Python
        #               Lisp

        二进制： 01100001
        十进制： 97
        ASCII编码表： a


        1. ASCII 美国标准信息交换码，用来表示英文字母、数字和常用符号，总共 128 个字符（0~127）

        2. 后来计算机开始普及全球，每个国家都有自己的语言符号，ASCII 编码就不满足其他国家的需求。
        于是各个国家开始制定自己的编码（但是都是在 ASCII 基础上进行扩展）

            欧洲：Latin-1 （ 0~256）ISO-8859-1
            简体中文：gb2312->gbk->gb18030  （一个汉字占 2 个字节）
            繁体中文：Big5
            日文：Shift-JIS

        3. 编码不一致，导致文件交流不方便，为了解决整个问题，国际标准组织指定了一个编码：Unicode
            Unicode 又名万国码，包含了世界上所有国家的文字符号。但是有个缺点，浪费空间（汉字占4个字节等等）

        4. 于是在Unicode基础上进行了升级：utf-8 （可变长的Unicode），可以根据文本类型指定不同的编码（在utf-8里一个汉字占 3 个字节，一个字母占 1 个字节），utf-8 是目前世界上最流行的编码。

            在所有的Linux系统终端默认编码，都是utf-8，90%以上的网页字符串，都是utf-8。


    -2 爬虫程序需要处理的编码场景：

        1. 发送请求获取网页响应（不同的网页有不同的编码）
        2. 数据处理过程中不同的字符串需要编码统一（编码要统一处理）
        3. 将处理结果保存起来（保存数据库、文件中要编码统一）

        如果编码不统一，会导致 "乱码"（按照其他编码表显示这个字符）


    -3. Python中如何处理字符串编码统一：

        1. Python3的字符串 类型和编码 对应：

            str 数据类型： Unicode 编码字符串
            bytes 数据类型： 非Unicode编码 字符串（其他编码字符串、图片音视频数据等）


            （了解）python2中的字符串类型和编码对应：
            unicode 数据类型： Unicode 字符串
            str 数据类型： 非Unicode字符串（其他编码字符串、图片音视频数据等）


        2. 字符串如何转码（编码统一）

            口诀：任何操作系统的 任何编程语言 的任何编码，都可以和 Unicode互相转换。

            gbk_str 转为 Unicode 转为 utf8_str：

            # 先将gbk字符串 通过 decode() 解码为 Unicode字符串
            unicode_str = gbk_str.decode("gbk")
            # 再将Unicode字符串 通过 encode() 编码为 utf-8字符串
            utf8_str = unicode_str.encode("utf-8")


        3. 终端、代码中创建的字符串编码

            -1. Python3 和 iPython3 创建的字符串 是 Unicode 编码，str 类型的字符串

            -2. Python2 根据使用的操作系统来定，Linux 是 utf-8、 简体中文Windows下 GBK(可以通过 chcp 65001修改为 utf-8)

                注意：在iPython2 下创建的字符串，默认全部都是 utf-8


        4. 将 Unicode 字符串数据保存在本地文件时

            Python3保存Unicode 字符串到本地文件时的编码，有三种处理方式：

            unicode_str = ""

            1.  直接保存Unicode字符串到本地文件时，解释器编码会参与工作:

                -1 Python3 默认的解释器编码是 utf-8，所以会把Unicode字符串按utf-8转码再保存文件，所以默认文件编码为 utf-8

                    with open("test.txt", "w") as f:
                        f.write(unicode_str)

                -2 Python2 默认的解释器编码是 ascii，所以会把Unicode字符串按 ascii 转码再保存文件（可能会导致 无法处理中文转码，UnicodeEncodeError）

                    import sys
                    reload(sys)
                    sys.setdefaultencoding("utf-8")

                    with open("test.txt", "w") as f:
                        f.write(unicode_str)


            2. 保存非 Unicode字符串到本地文件，手动对Unicode字符串进行转码再写入

                Python2 和 Python3 语法一致。
                with open("test.txt", "wb") as f:
                    f.write(unicode_str.encode("utf-8"))
                    #f.write(unicode_str.encode("gbk"))


            3. 通过 open() 的encoding 参数指定编码，再写入Unicode字符串

                -1. Python3 的 open()方法 有 encoding 参数。

                    with open("test.txt", "w", encoding="utf-8") as f:
                        f.write(unicode_str)


                -2 Python2 的 open() 方法 没有 encoding参数，但是通过codecs模块的open方法，可以指定encoding参数。

                    import codecs
                    with codecs.open("test.txt", "w", encoding="utf-8") as f:
                        f.write(unicode_str)



        5. 文件编码
            文件没有 Unicode 编码，必须转码后再使用（utf-8、gbk）

            当写入一个字符串到文件中时，文件编码 等于 该字符串编码。
                如果写入了不同 编码到同一个文件中，会导致文件编码被修改为最后一次写入的字符串编码。
                同时导致之前的数据不可逆的丢失。


        6. 网页编码
            /html/head/meta/charset 指定的，不同的网页可能不一样，会影响爬虫获取的数据编码。


        7. 代码文件头部编码声明
            默认Python2的 代码文件头部编码声明是 ASCII，在python2的代码不能写非ASCII字符，否则会报错，所以需要提前加上下面这行代码。
            # -*- coding:utf-8 -*_

            Python 3默认的代码文件头部编码声明是 utf-8，不需要手动修改了。


适合程序员的两种字体：Consolas、Manaco
删除 "C:\Users\Power\AppData\Roaming"下的 Sublime Text 3，并直接粘贴新的进去。


Chrome抓包工具中获取的请求报头 快速转换字典：
匹配：''' ^(.*?):\s(.*?)$ '''
替换：''' "\1" :  "\2", '''



NetScape 网景 Mozilla 浏览器 -> Frame
Microsoft 微软 IE 1.0 浏览器 -> Frame 添加了Mozilla前缀

三流公司 做产品
二流公司 做设计
一流公司 做标准

Mozilla 基金会  Firefox 支持内核 Gecko
Linux 借鉴了Gecko-> KTHML 内核
Apple 借鉴了KHTML-> Webkit Safari
Google 借鉴了Webkit -> Chrome



案例：百度贴吧页面分析

    固定url地址部分
        http://tieba.baidu.com/f?

    表示贴吧名
        kw=美食

    百度贴吧页码值计算：
        page =1  pn = 0
        page =2  pn = 50
        page =3  pn = 100

        pn = (page - 1) * 50





--------------------------------------------------------

第二天：

--------------------------------------------------------



对于爬虫来说：网页通常分为两种 静态页面； 动态页面

    1. 静态页面：数据内容直接保存在html中。
        url变化内容也会变化。

    2. 动态页面：数据不是直接保存在html里的，而是通过 ajax 请求获取数据再渲染的。
        url不变但内容会变化。
        记住：动态页面必须要抓包，找到浏览器和服务器之间到底偷偷传递了什么文件。

    抓包：抓取网络数据包。



C10K



代理API：http://kps.kdlapi.com/api/getkps/?orderid=975140257435034&num=1&pt=1&sep=1
账户：maozhaojun
密码：ntkn0npx




网络数据加密：
1. md5 / sha1 不可逆加密算法：  结果是十六进制数
    import hashlib
    md5_obj = hashlib.md5()
    sha1_obj = hashlib.sha1()

    md5_obj.update("非Unicode字符串")
    sha1_obj.update("非Unicode字符串")

    md5_obj.hexdigest()
    sha1_obj.hexdigest()


2. base64 ： 可逆的一种编码方式
    import base64
    b64data = base64.b64encode() # 对字符串 或 文件数据进行编码
    base64.b64decode(b64data) # 对base64数据解码，复原回原本的数据

3. rsa 非对称加密 /aes 对称加密

    客户端和服务器端数据加密： 公钥和私钥


4. Unix 时间戳
    表示 从 1970年1月1日到现在的总秒数，通常有两种值：
    10 位： 单位是秒；13 位 ：单位是毫秒。

    秒： int(time.time())
    毫秒： int(time.time() * 1000)




Requests模块有两种发送请求的方式：

    # 普通请求发送方式，不会保存Cookie
    requests.get()
    requests.post()


    # 创建一个可以保存Cookie 的 session对象
    ssion = requests.session()
    # 通过session对象发送请求，可以记录并传递Cookie
    ssion.get()
    ssion.post()


爬虫的标准模拟登录流程：

    模拟登录的目的：为了登录成功并保存Cookie，再用于发送其他需要登录后才能访问的页面请求。

    1. 发送登录页面的 get 请求，获取登录参数
    2. 发送登录的 post 请求，提交登录参数 和 账户密码，实施模拟登录（如果登录成功则记录Cookie）
    3. 附带登录的Cookie，发送其他页面的请求，提取需要的数据。

        模拟登录实际开发很少使用（通过Cookie池代理），但是面试会经常问。









HTML DOM 是HTML的树形结果概念。


        HTML

head            body
title      a p div br   属性值、文本内容
                        href src
meta




lxml/ XPATH

XPATH 提取数据定律：

    1. xpath表达式的匹配结果，一定是一个列表
        匹配成功返回所有数据的列表，没有匹配成功返回空列表

    2. xpath表达式提取的数据（属性值、文本值），结果一定是一个Unicode字符串
        url_list = xpath("//div[@id='u1']/a/@href")
        text_list = xpath("//div[@id='u1']/a/text()")

    3. 如果没有提取数据，返回所有标签结点的对象（Element对象），该对象可以继续调用xpath向下取值。
        a_list = xpath("//div[@id='u1']/a")

        item_list = []

        for a in a_list:
            item = {}
            item['text'] = a.xpath("./p/text()")[0]
            try:
                item['src'] = a.xpath("./img/@src")[0]
            except:
                item['src'] = None

            item['src'] = a.xpath("./img/@src")[0] if a.xpath("./img/@src") else None

            item_list.append(item)
            # [{}, {}, {}, {}]

xpath ： XML Path Language，是一种专门提取xml文档数据的语法。

html : 网页字符串，字符串本身不支持xpath提取数据，所以需要通过lxml转换

lxml ： 作用是将html字符串，转换为可以调用xpath方法的 对象lxml.ElementTree


# BeautifulSoup4、Pyquery

# 从lxml类库中，导入 etree模块
from lxml import etree

html = requests.get(url).content

# etree模块有个HTML类，接收网页字符串，并返回一个 DOM 对象
html_dom = etree.HTML(html)

# 读取本地文件，并转为 HTML DOM对象
#html_dom = etree.parse("./baidu.html")

# 将DOM对象复原回网页字符串
#html = etree.tostring(html_dom)

# DOM对象可以调用xpath方法，提取网页的数据
url_list = html_dom.xpath("//div[@id='u1'][1]/a/@href")


著名技术问答网站："https://www.stackoverflow.com/"





import re

re.match() :
    从字符串的第一个字符开始匹配，如果匹配成功返回Match对象，该对象可以通过 group()提取数据
    如果第一个字符不符合匹配，则返回 None
re.search()
    从字符串的第一个字符开始匹配，如果匹配成功返回Match对象，该对象可以通过 group()提取数据
    如果第一个字符不符合匹配，继续从第二个开始，直到最后一个字符为止，如果一种没有匹配，则返回 None

    match 和 search 都只匹配一次

re.findall() ： 返回字符串里所有符合匹配的结果，如果匹配成功，返回列表；如果不成功，返回空列表

re.sub("re表达式", "字符串", "替换后的字符") ： sub替换字符串指定字符，替换后返回一个新字符
re.split() ： 对字符串按指定字符进行分隔，返回分隔后的列表


str <-> list

list = str.split()
str = "".join(list)

str.replace()
str.find()


re.findall(r"\d+", html)
re.findall(r"\d+", html)
re.findall(r"\d+", html)
re.findall(r"\d+", html)
re.findall(r"\d+", html)


pattern = re.compile(r"\d+")
pattern.findall(html)
pattern.findall(html)
pattern.findall(html)
pattern.findall(html)
pattern.findall(html)
pattern.findall(html)


"\d+\n\t"

忽略Python字符串里的转义字符




import json

# 将python对象转为json字符串
json_str = json.dumps(python_obj)
# 将json字符串转为python对象
python_obj = json.loads(json_str)
# 将python对象转为json字符串 并保存到 文件中
json.dump(python_obj, open("xxx.json", "w"))
# 读取文件的json字符串，并转为对应的Python对象
python_obj = json.load(open("xxx.json", "r"))



代码
git clone https://github.com/dododream/python.git





--------------------------------------------------------

第三天：

--------------------------------------------------------





from selenium import webdriver

driver = webdriver.Chrome()
#driver = webdriver.PhantomJS()

driver.get("http://www.baidu.com/")

html = driver.page_source

driver.quit()

html_obj = etree.HTML(html)


# 32 位： 最大的内存寻址范围是 2 的 32次方
# 64 位： 最大的内存寻址范围是 2 的 64次方


ChromeDriver的作用是：可以调用电脑上的真实Chrome浏览器。

Chrome默认是有界面的浏览器，所以支持复杂的鼠标和键盘事件（比PhantomJS更方便）
Chrome也支持无界面（headless）模式：节省内容，程序运行速度更快

from selenium import webdriver

options = webdriver.ChromeOptions()

options.add_argument("--headless")
# 无界面模式（更节约资源）
driver = webdriver.Chrome(chrome_options=options)
# 有界面模式（支持复杂的鼠标键盘事件）
driver = webdriver.Chrome()

# 获取渲染后的网页源码，可以通过xpath提取数据
html = driver.page_source




"https://www.douyu.com/directory/all"



#定位到 所有主播的大项
ul_element = xpath("//ul[@class='layout-Cover-list']")[1]
# 提取所有主播的每一个主播信息，并返回列表（一页120个）
div_list = ul_element.xpath('.//div[@class="DyListCover-content"]')

for div in div_list:
    category_name = div.xpath(".//span[@class='DyListCover-zone']")[0]
    room_name = div.xpath('.//h3[@class="DyListCover-intro"]')[0]
    people_number = xpath('.//span[@class="DyListCover-hot"]')[0]
    directory_name = xpath('.//h2[@class="DyListCover-user"]')[0]





Sublime Text3 最好用的两个快捷键：

ctrl + d ； 向后选中
shift + 鼠标右键拖动： 块选中



Python第三方模块安装方式：
    1. 在线安装： pip install xxxx
    2. 离线包安装: pip install xxxx_1.23.whl
    3. 源码安装： python setup.py install


fake_useragnet : "https://pypi.org/project/fake-useragent/"


网站反爬顾忌： 误伤真实用户
爬虫爬取数据： 爬虫道德（尽量降低对方服务器负载，也可以保护自身）


验证码的三种解决办法：
    1. 手动打码：将验证码图片下载下来，手动打开并输入正确的验证码，提交请求参数。
    2. OCR（光学字符识别系统）：读取图片上的文字，并返回一个字符串（识别会有精确度问题）
        # Google处理的 Tesseract OCR
    3. 打码平台：将验证码图片上传给打码平台处理，打码平台返回验证结果（收费）


#Python解释器的小整数对象池 ： -5 ~ 256 之间 如果值相同则id相同





1. 发送GET请求： http://activity.renren.com/livecell/rKey

    n = json.loads(response.content)['data']

2.  提供账户名和密码
    phoneNum: mr_mao_hacker@163.com
    password： ALARMCHIME

3. 执行js：
    三个js文件： Bigint.js 、RSA.js 、Barrett.js
    一段js代码：
'''
t.password = t.password.split("").reverse().join(""), setMaxDigits(130);
var o = new RSAKeyPair(n.e,"",n.n), r = encryptedString(o, t.password);
t.password = r, t.rKey = n.rkey'''

4. 提取js执行结果，获取 password 和 rkey 登录参数：

    phoneNum: mr_mao_hacker@163.com
    password: 83ac1c99378609e178cab3ece815d36c12b5ca094300333e83ea5436b6109fb2
    c1: 0
    rKey: 56c61d35789ce0326162a224b59725f3

5. 发送登录的POST请求： http://activity.renren.com/livecell/ajax/clog








--------------------------------------------------------

第四天：

--------------------------------------------------------


计算机速度最快： CPU -> 寄存器 -> 缓存L1/L2/L3 -> 内存 -> 硬盘 -> 网卡 -> BIOS

                                        机械硬盘： 5400/ 80MB/s 7200 100MB/s

LMAP: Linux + MySQL + Apache + PHP/Python
      Windows Server + SQL Server + ASP.net

SQL（MySQL、Oracle、DB2） 应用场景：
1. 高度事务性场景、银行、物流、贸易，需要大量原子性操作。
2. 需要持久化存储的 "冷数据"（硬盘成本低）
3. 存储对安全性要求高的数据（SQL成熟稳定）
4. 需要通过统一的 SQL 语句处理的场景
5. 业务需要明确的多表结构关系设计和字段设计（需要经验丰富的架构师）


NoSQL(内存+硬盘) 应用场景：
1. 灵活的数据结构，也需要事先设计表结构关系
2. 设计存储"热数据"，IO要求高的场景（基于内存，速度快）
3. 高度伸缩性，更容易扩展集群搭建
4. 适合互联网时代多变的数据类型存储。



上： 用户（高并发的IO读写）

中： NoSQL 支持

下： SQL （持久化存储）


（Ubuntu 16）第一种： sudo apt-get install -y mongodb-org
（Ubuntu 18）第二种： sudo apt install mongodb


开启MongoDB服务： sudo mongod
（第一次使用需要事先手动创建 /data/db 目录， sudo mkdir -p /data/db/  sudo chmod 777 /data/db）

开启MongoDB shell客户端： mongo

# 查看当前所在数据库
> db

# 查看所有的数据库
> show dbs

# 切换到指定数据库
> use youyuan

# 查看当前数据库下所有集合（类似于SQL的table)
> show collections

# 查看当前数据下 指定集合 的所有数据
> db.beijing_mm.find()

# 删除当前数据库下 指定的集合
> db.beijing_mm.drop()

#删除当前数据库
> db.dropDatabase()



一、 MongoDB的数据 增加  insert()

    # 第一种： 直接写入一条文档
    > db.stu.insert({ "_id" : 1, "name" : "刘备", "age" : 40, "hometown" : "蜀" })

    # 第二种： 先创建一个空的文档，依次添加数据，最后统一写入
    > data = {}
    > data._id = 2
    > data.name = "关羽"
    > data.age = 38
    > data.hometown = "蜀"
    > db.stu.inesrt(data)



二、 MongoDB的数据 删除 remove()

    1. remove() 默认删除所有符合条件的 文档数据
        > db.stu.remove({age : 35})


    2. remove() 通过第二个参数 {justOne : true} 来删除第一条符合条件的文档数据
        > db.stu.remove({age : 38}, {justOne : true})


    3. remove() 通过空的参数，可以删除当前集合下所有文档数据
        > db.stu.remove({})
        > db.stu.drop() # 删除集合效果相同

    # 在Python中 delete_one 和 delete_many

三、 MongoDB的数据 修改更新 update()
    update() 至少需要提供两个参数：
        第一个参数表示 匹配的条件
        第二个参数表示 修改的数据
        第三个参数{multi : true} 表示处理所有文档数据（默认只处理第一条文档）

    1. update()  默认将匹配的文档数据，全部替换为 第二个参数的文档数据，但是_id 不变
        > db.stu.update({name : "刘备"}, {age : 38, hometown : "蜀国"})

    2. update() 通过 $set 修饰符，可以 修改/添加 特定的字段
        # 只修改 刘备的 age 为40，并新增gender 为 true
        > db.stu.update({name : "刘备"}, {$set : {age : 40, gender : true}})

    3. 默认update() 只处理第一条文档，通过 {multi : true} 处理所有文档
        > db.stu.update({hometown : "蜀"}, {$set : {gender : true}}, {multi : true})


