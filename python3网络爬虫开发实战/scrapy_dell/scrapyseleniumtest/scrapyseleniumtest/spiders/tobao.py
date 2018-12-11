# -*- coding: utf-8 -*-
import scrapy


class TobaoSpider(scrapy.Spider):
    name = 'tobao'
    allowed_domains = ['www.taobao.com']
    start_urls = ['http://www.taobao.com/']

    def parse(self, response):
        pass
