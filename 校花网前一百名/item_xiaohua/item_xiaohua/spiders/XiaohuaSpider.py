import scrapy

from item_xiaohua.items import XiaohuaItem

class XiaohuaSpider(scrapy.Spider):

    name = "xiaohua"

    start_urls = ["http://www.xiaohuar.com/2014.html"]

    def parse(self, response):

        babes = response.xpath('//div[@class="demo clearfix"]/div/div')


        for babe in babes:

            item = XiaohuaItem()

            title = babe.xpath('.//div[@class="title"]/span/a/text()').extract()[0]
            item['title'] = title
            img = babe.xpath('.//div[@class="img"]/a/img/@src').extract()[0]
            item['img'] = img

            yield item
