import json

str = '''
[{
    'name':'Bod',
    'gender':'male',
    'birthday':'1992-10-18'
}]
'''

try:
    data = json.loads(str)
except Exception as e:
    print(e)
# 如果使用的是单引号,那么会报错,出现解析失败的提示

# 文本读取
with open('data.json', 'r') as file:
    str = file.read()
    data = json.loads(str)
    print(data)