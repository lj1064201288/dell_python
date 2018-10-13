import re
import scrapy
from item_baotu.items import BaotuItem

class BaotuSpider(scrapy.Spider):

    name = "baotu"

    start_urls = ["https://ibaotu.com/ui/15-0-0-0-0-1.html"]

    allowed_domains = ['ibaotu.com']

    def parse(self, response):

        item = BaotuItem()

        contents = response.xpath('//div[@class="bt-list ad-list"]/ul/li')

        for content in contents:
            title = content.xpath('./div[@class="hover-pop"]/div/a[@class="tit-name"]/text()').extract()[0]
            img = content.xpath('./a/img/@data-url').extract()[0]

            if title:
                item['title'] = title
            if img:
                item['img'] = img

            curpage = re.findall('\d+', response.url)
            page = int(curpage[-1]) + 1
            new_url = re.sub('(\d+).html', str(page) + '.html', response.url)
            if page <= 10:
                yield scrapy.Request(new_url, callback=self.parse)

            yield item