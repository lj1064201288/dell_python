# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
import pymongo

class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item

class TextPipeline(object):
    def __init__(self):
        self.limit = 50

    def process_item(self, item, spider):
        if item['text']:
            if len(item['text']) > self.limit:
                item['text'] = item['text'][0:self.limit].rstrip() + '...'
                return item
            else:
                return DropItem('Missing Text')

class MongoPipeline(object):
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        """
        这是一个类方法,用classmethod标识, 是一种依赖注入的方式
        它的参数就是crawler,通过crawler我们可以拿到全局配置信息
        在全局配置setting.py中,我们可以定义MONGO_URI和MONGO_DB来指定MongoDB连接需要的地址和数据库名称
        拿到配置信息之后返回类对象即可,所以这个方法的定义主要用来获取setting.py中的配置的
        :param crawler:
        :return:
        """
        return cls(
            mongo_uri = crawler.settings.get('MONGO_URI'),
            mongo_db = crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spier):
        """
        当Spider开启时,这个方法被调用
        :param spier:
        :return:
        """
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        name = item.__class__.__name__
        print(dict(item))
        self.db[name].insert(dict(item))
        return  item

    # 当Spider关闭时,这个方法调用
    def close_spider(self, spider):
        self.client.close()
