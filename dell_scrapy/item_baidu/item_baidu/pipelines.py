# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class ItemBaiduPipeline(object):
    def process_item(self, item, spider):
        return item

class BaiduPipeline(object):
    def __init__(self):
        self.file = open('百度.json', 'w')

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(content)

        return item

    def write_close(self):
        self.file.close()