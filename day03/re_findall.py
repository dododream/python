html = "balabala <div id='123'>Hello 123 world</div> --balabalba-- <div id='123'>Hello 456 world</div> balabala"
import re

#.* 默认贪婪模式，会进行可的多匹配，返回的结果是只有一个结果
pattern1 = re.compile("<div id='123'>.*</div>")
pattern1.findall(html)

# .*? 表示非贪婪模式，尽可能的少匹配，返回多条结果（但是结果会包含前置和后置的内容）
pattern2 = re.compile("<div id='123'>.*?</div>")
pattern2.findall(html)

# 通过 () 表示只取出中间的数据， 前置和后置不取了。
pattern3 = re.compile("<div id='123'>(.*?)</div>")
pattern3.findall(html)

# 特殊版的html，内容有换行符
html = "balabala <div id='123'>Hello 123 world</div> --balabalba-- <div id='123'>Hello 456 \nworld</div> balabala"
pattern3.findall(html)

# 正则里的 . 用来匹配除换行符之外的任意字符，但是可以通过 re.S 启用DOTALL模式，让. 也可以匹配换行符
pattern4 = re.compile("<div id='123'>(.*?)</div>", re.S)
pattern4.findall(html)


# 预定义字符：

# .  除换行符外的任意字符
# \d 数字
# \D 非数字
# \w 字母数字下划线
# \W 非字母数字下划线
# \s 空白符(空格、\r、\n)
# \S


# 数量词：
# *  零次或无限次
# +  一次或无限
# ?  零次或一次
# {4}
# {3, 5}

# Python的re默认是贪婪模式， 在任何数量词后加 ? 表示非贪婪模式 , *? +? ?? {3,5}?


# 逻辑表达式：
# |

# ()  : 1. 在match、search、findall匹配结果里，可以提取 () 里的数据
#       2. 在 sub() 表示分组， 取分组用 \1  \2  表示第一组和第二组

# re.S 表示启用DOTALL
# re.I 表示忽略字母大小写



