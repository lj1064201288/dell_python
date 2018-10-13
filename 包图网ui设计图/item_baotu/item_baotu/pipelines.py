# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import requests
from hashlib import md5

class ItemBaotuPipeline(object):
    def process_item(self, item, spider):
        return item

class BaotuPipeline(object):

    def process_item(self, item, spider):

        content = dict(item)

        file_path = "img" + os.path.sep + content['title']
        if not os.path.exists(file_path):
            os.makedirs(file_path)

        try:
            response = requests.get('https:' + content['img'])

            if response.status_code == 200:
                print(response)
                img_path = file_path + os.path.sep + md5(response.content).hexdigest() + '.png'
                if not os.path.exists(img_path):
                    with open(img_path, 'wb') as f:
                        f.write(response.content)
        except requests.ConnectionError:
            print("Error")

        return item


