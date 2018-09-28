import scrapy

from item_ganji.items import GanjiItem

class GanjiSpider(scrapy.Spider):

    name = 'ganji'

    start_urls = ['http://cd.ganji.com/site/s/_python/']

    def parse(self, response):

        positions = response.xpath('//div[@class="job-wanted"]/dl')

        print(len(positions))

        for position in positions:

            item = GanjiItem()

            title1 = position.xpath('./dt[@class="f-introd"]/a/span[@class="f_c_red"]/text()').extract()
            title2 = position.xpath('./dt[@class="f-introd"]/a/text()').extract()[0]
            title = str(title1) + title2
            if len(title):
                item['title'] = title
            else:
                item['title'] = 'No'
            item['href'] = position.xpath('./dt[@class="f-introd"]/a/@href').extract()[0]
            item['time'] = position.xpath('./dd[@class="j-time"]/text()').extract()[0]
            item['address'] = position.xpath('./dd[@class="addr"]/a/text()').extract()[0]

            yield item



