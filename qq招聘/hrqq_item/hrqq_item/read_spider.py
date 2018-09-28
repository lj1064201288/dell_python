import json

with open('qq招聘.json', 'r') as r:
    datas = json.load(r)

for data in datas:
    print(data)
