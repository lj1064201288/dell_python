# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Join, Compose
from scrapyuniversal.items import NewsItem


class ChinaSpider(CrawlSpider):
    name = 'china'
    allowed_domains = ['tech.china.com']
    start_urls = ['https://tech.china.com/articles/']

    rules = (
        Rule(LinkExtractor(allow=r'article\/.*\.html',
                           restrict_xpaths='//div[@id="left_side"]//div[@class="con_item"]'),
             callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths='//div[@id="pageStyle"]//a[contains(.,"下一页")]'))
    )

    def parse_item(self, response):
        item = NewsItem()
        item['title'] = response.xpath('//h1[@id="chan_newsTitle"]/text()').extract_first()
        item['url'] = response.url
        item['text'] = ''.join(response.xpath('//div[@id="chan_newsDetail"]//text()').extract()).strip()
        item['datetime'] = response.xpath('//div[@id="chan_newsInfo"]/text()').re_first('(\d+-\d+-\d+\s\d+:\d+:\d+)')
        item['source'] = response.xpath('//div[@id="chan_newsInfo"]/text()').re_first(' 来源：(.*)').strip()
        item['website'] = '中华网'

        yield item

    # def parse_item(self, response):
    #     loader = ChinaLoader(item=NewsItem(), response=response)
    #     loader.add_xpath('title', '//h1[@id="chan_newsTitle"]/text()')
    #     loader.add_xpath('url', response.url)
    #     loader.add_xpath('text', '//div[@id="chan_newsDetail"]//text()')
    #     loader.add_xpath('datetime', '//div[@id="chan_newsInfo"]/text()', re='(\d+-\d+-\d+\s\d+:\d+:\d+)')
    #     loader.add_xpath('source', '//div[@id="chan_newsInfo"]/text()', re='来源：(.*)')
    #     loader.add_xpath('website', '中华网')
    #
    #     yield loader.load_item()



# class Newsloader(ItemLoader):
#     default_output_processor = TakeFirst()
#
# class ChinaLoader(Newsloader):
#     text_out = Compose(Join(), lambda s: s.strip())
#     source_out = Compose(Join(), lambda s: s.strip())
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
