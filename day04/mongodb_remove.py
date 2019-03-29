import pymongo
client = pymongo.MongoClient()
stu = client.test.stu

# 删除一条数据
stu.delete_one({"_id" : 3})

# 删除多条数据
stu.delete_many({"_id" : 3})

%hist -f mongodb_remove.py
