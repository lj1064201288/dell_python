import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.text

collection = db.students
student = {
    'id':"20171114",
    'name':'liujun',
    'age': '20',
    'gender':'male'
}

result = collection.insert(student)
print(result)