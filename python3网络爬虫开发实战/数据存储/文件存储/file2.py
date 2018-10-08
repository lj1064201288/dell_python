# 先导入json库
import json

str = """
[{
    "name":"Bob",
    "gender":"male",
    "birthday":"19992-10-18"
},
{
    "name":"Selina",
    "gender":"female",
    "birthday":"1995-10-18"
}]
"""

# 这里使用loads()方法将字符串转化为JSON对象,由于最外层是中括号,所以最终的类型是列表的类型
print(type(str))
data = json.loads(str)
print(data)
print(type(data))
print(data[0]['name'])
print(data[0].get('name'))

# 推荐使用get()方法,因为如果键名不存在也不会报错,会返回None,另外，get()方法还可以传入第二个参数可以直接添加一个键值对
print(data[0].get("age"))
print(data[0].get('age', 25))
print(data)