# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json


class MeijuPipeline(object):
    def process_item(self, item, spider):
        return item


class MeijuPipline(object):

    def __init__(self):
        self.file = open('meiju.json', 'w')

    def process_item(self, item, spider):
        # print(item['name'])
        # print(item['href'])
        # print(item['tv'])

        content = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(content)
        return item

    def close_spider(self, spider):
        self.file.close()