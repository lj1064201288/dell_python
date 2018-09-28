# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class ItemWangyihrPipeline(object):
    def process_item(self, item, spider):
        return item


class WangyiHrPipeline(object):

    def __init__(self):
        self.filename = open('网易招聘.json', 'w')

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + ',\n'
        self.filename.write(content)

        return item

    def close(self, spider):
        self.filename.close()