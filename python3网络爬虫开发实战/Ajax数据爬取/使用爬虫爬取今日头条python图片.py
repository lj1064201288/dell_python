import os
import time
import requests
from hashlib import md5
from multiprocessing.pool import Pool
from urllib.parse import urlencode


def get_page(offset):

    prams = {
        "offset": 0,
        "format": "json",
        "keyword": "python图片",
        "autoload": "true",
        "count": 20,
        "cur_tab": 3,
        "from": "gallery"
    }

    url = "https://www.toutiao.com/search_content/?" + urlencode(prams)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()

    except ConnectionError:
        print("获取页面内容失败.")
    except Exception as e:
        print(e)

def get_parse(json):
    if json.get('data'):
        items = json.get('data')
        for item in items:
            title = item.get('title')
            images = item.get('image_list')
            for image in images:
                yield{
                    'image':"https:" + image.get('url'),
                    'title': title
                }

def save_image(item):
    img_path = "img1" + os.path.sep + item.get('title')

    if not os.path.exists(img_path):
        os.makedirs(img_path)

    try:
        response = requests.get(item.get('image'))
        if response.status_code == 200:
            file_path = img_path + os.path.sep + md5(response.content).hexdigest() + ".jpg"
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
                    print("Downloaded image is:{0}".format(file_path))
            else:
                print("Already Downloaded:", file_path)
    except requests.ConnectionError:
        print("Failed to save Image item {0}".format(item))


def main(offset):
    json = get_page(offset)
    for item in get_parse(json):
        print(item)
        save_image(item)

GROUP_START = 0
GROUP_END = 3

if __name__ == '__main__':

    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main, groups)
    pool.close()
    pool.join()







