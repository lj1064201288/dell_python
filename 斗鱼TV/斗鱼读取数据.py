import json

if __name__ == '__main__':

    filename = "斗鱼.json"
    with open(filename, 'r', encoding='utf-8') as r:
        datas = json.load(r)

    print(len(datas))
    for data in datas:
        print(data)