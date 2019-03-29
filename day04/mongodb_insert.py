import pymongo
client = pymongo.MongoClient(host='127.0.0.1', port=27017)

for data in client.test.stu.find():
    print(data)

# 强转为列表
list(client.test.stu.find())
stu = client.test.stu

# 插入一条
item = {"_id" : 4, "name" : "赵云", "age" : 32, "hometown" : "蜀"}
stu.insert(item)

# 插入多条
item_list = [{"_id" : 5, "name" : "马超", "age" : 30, "hometown" : "蜀"}, {"_id" : 6, "name" : "黄忠", "age" : 60, "hometown" : "蜀"}]
stu.insert(item_list)


%hist -f mongodb_insert.py
