import json


if __name__ == '__main__':

    filename = "豆瓣图书python.json"

    with open(filename, 'r', encoding='utf-8') as r:

        datas = json.load(r)

    n = 0

    for data in datas:
        print(data)
        n += 1

    print(n)
