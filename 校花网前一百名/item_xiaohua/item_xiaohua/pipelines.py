# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import requests
from hashlib import md5

class ItemXiaohuaPipeline(object):
    def process_item(self, item, spider):
        return item

class XiaohuaPipeline(object):


    def process_item(self, item, spider):

        content = dict(item)
        file_path = "img" + os.path.sep + content['title']
        if not os.path.exists(file_path):
            os.makedirs(file_path)

        url = "http://www.xiaohuar.com"
        try:
            if url not in content['img']:
                response = requests.get(url + content['img'])
                if response.status_code == 200:
                    img_path = file_path + os.path.sep + md5(response.content).hexdigest() + ".jpg"
                    if not os.path.exists(img_path):
                        with open(img_path, 'wb') as f:
                            f.write(response.content)
            if url in content['img']:
                response = requests.get(content['img'])
                if response.status_code == 200:
                    img_path = file_path + os.path.sep + md5(response.content).hexdigest() + ".jpg"
                    if not os.path.exists(img_path):
                        with open(img_path, 'wb') as f:
                            f.write(response.content)
        except requests.ConnectionError:
            print("Error")

        return item