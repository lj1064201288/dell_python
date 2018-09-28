import json

if __name__ == '__main__':

    filename = "扇贝单词.json"

    with open(filename, 'r', encoding='utf-8') as r:
        datas = json.load(r)

    for data in datas:
        print(data)