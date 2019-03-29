import pymongo
client = pymongo.MongoClient()
stu = client.test.stu

# 更新一条
stu.update_one({"hometown":"蜀"}, {"$set" : {"gender" : False}})

# 更新多条
stu.update_many({"hometown":"蜀"}, {"$set" : {"gender" : False}})


%hist -f mongodb_update.py
