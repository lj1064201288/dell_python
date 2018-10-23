import pymongo

client = pymongo.MongoClient(host="localhost", port=27017)
# 指定数据库
db = client.test
# db = client['test']
# 这两种方式都是等价的

# 指定一个集合的名称为students,与指定数据库类似,指定集合也有两种方式
collection = db.students
# collection = db["students"]

# 插入数据

student1 = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}
#result = collection.insert(student1)
#print(result)
# 也可以多条属性同时插入,只需要以列表的形式传递即可
student2 = {
    'id':'20170202',
    'name':'Mike',
    'age': 21,
    'gender':'male'
}

result = collection.insert([student1, student2])
print(result)

# 官方目前已经不推荐使用insert()方法了,但是继续使用也没有什么问题
# 推荐使用insert_one()和insert_many()方法分别插入单条记录和多条记录

result = collection.find_one({'name': 'Mike'})
print(type(result))
print(result)

# 计数
print("***" * 50)
count = collection.find().count()
print(count)