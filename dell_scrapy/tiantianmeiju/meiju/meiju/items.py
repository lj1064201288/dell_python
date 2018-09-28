# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MeijuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class MeijuItems(scrapy.Item):
    name = scrapy.Field()
    href = scrapy.Field()
    tv = scrapy.Field()
    state = scrapy.Field()
    time = scrapy.Field()
