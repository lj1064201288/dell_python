import json

if __name__ == '__main__':

    filename = "meiju.json"

    with open(filename, 'r', encoding='utf') as r:

        datas = json.load(r)

    for data in datas:
        print(data)