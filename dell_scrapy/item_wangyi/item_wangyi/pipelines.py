# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class ItemWangyiPipeline(object):
    def process_item(self, item, spider):
        return item


class WangyiPipeline(object):

    def __init__(self):
        self.filename = open('网易招聘.json', 'w')

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.filename.write(content)

    def close(self, spider):
        self.filename.close()

