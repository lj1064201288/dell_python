# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class HrqqItemPipeline(object):
    def process_item(self, item, spider):
        return item

class QqItemPipeline(object):

    def __init__(self):
        self.file = open('qq招聘.json', 'w')

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + ',\n'
        self.file.write(content)

        return item

    def colse(self, spider):
        self.file.close()
