import re
s = "你好world, hello世界.?"
s = "你好world, 123, hello世界.?"

# Unicode字符集中， 第一个简体中文的Unicode值
print("\u4e00")
# Unicode字符集中， 最后一个简体中文的Unicode值
print("\u9fa5")

# 匹配所有Unicode中所有中文
pattern = re.compile("[\u4e00-\u9fa5]")
# 将中文替换为空
pattern.sub("", s)

# 匹配所有不是 Unicode中文
pattern = re.compile("[^\u4e00-\u9fa5]")
# 将非中文替换为空
pattern.sub("", s)

