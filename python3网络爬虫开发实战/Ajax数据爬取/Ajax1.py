'''
已经分析过Ajax请求的逻辑,首先,实现方法get_page()来加载单个Ajax请求的结果,其中唯一变化的参数是offset,所以将它当做参数传递

'''

import os
import requests
from hashlib import md5
from urllib.parse import urlencode
from multiprocessing.pool import Pool

def get_page(offset):
    params = {
        "offset": offset,
        "format": "json",
        "keyword":"街拍",
        "autoload": "true",
        "count": "20",
        "cur_tab": "1",
        "from":"search_tab"
    }

    url = "https://www.toutiao.com/search_content/?" + urlencode(params)

    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None

def get_images(json):
    if json.get('data'):
        data = json.get('data')
        for item in data:
            if item.get('cell_type') is not None:
                continue
            title = item.get('title')
            images = item.get('image_list')
            for image in images:
                yield{
                    "image": 'https:' + image.get('url'),
                    "title": title
                }

def save_image(item):
    img_path = "img" + os.path.sep + item.get('title')
    if not os.path.exists(img_path):
        os.makedirs(img_path)

    try:
        response = requests.get(item.get('image'))
        if response.status_code == 200:
            file_path = img_path + os.path.sep + '{file_name}.{file_suffix}'.format(file_name=md5(response.content).hexdigest(), file_suffix='jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
                    print("Downloaded image path is %s" %file_path)
            else:
                print('Already Downloaded', file_path)
    except requests.ConnectionError:
        print('Failed to Save Image，item %s' % item)

def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        print(item)
        save_image(item)

GROUP_START = 0
GROUP_END = 7

if __name__ == '__main__':

    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END+1)])
    pool.map(main, groups)
    pool.close()
    pool.join()

