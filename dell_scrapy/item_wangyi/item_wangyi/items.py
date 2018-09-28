# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ItemWangyiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class WangyiItem(scrapy.Item):

    title = scrapy.Field()
    href = scrapy.Field()
    position = scrapy.Field()
    work_type = scrapy.Field()
    work_location = scrapy.Field()
    num = scrapy.Field()
    time = scrapy.Field()

