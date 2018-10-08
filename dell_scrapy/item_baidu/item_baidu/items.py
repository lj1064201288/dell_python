# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ItemBaiduItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ItemBaidu(scrapy.Item):
    postId = scrapy.Field()
    name = scrapy.Field()
    publishDate = scrapy.Field()
    postType = scrapy.Field()
    education = scrapy.Field()
    recruitNum = scrapy.Field()
    serviceCondition = scrapy.Field()
    workContent = scrapy.Field()
    workPlace = scrapy.Field()
    workYears = scrapy.Field()