# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class ItemGanjiPipeline(object):
    def process_item(self, item, spider):
        return item

class GanjiPipeline(object):

    def process_item(self, item, spider):

        print(item['title'])

        with open('ganji.json', 'a', encoding='utf-8') as f:
            json.dump(dict(item), f, indent=5)

        return item
