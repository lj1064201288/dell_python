import  json

data = [{
    'name':'刘俊',
    'gender':'男',
    'birthday':'1996-2-24'
}]

with open('data.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(data, indent=2, ensure_ascii=False))