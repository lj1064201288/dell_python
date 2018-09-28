import scrapy

from meiju.items import MeijuItems

class MeijuSpider(scrapy.Spider):

    name = 'meiju'

    start_urls = ['http://www.meijutt.com/new100.html']

    def parse(self, response):

        movies = response.xpath('//ul[@class="top-list  fn-clear"]/li')

        print(len(movies))

        for movie in movies:

            item = MeijuItems()

            item['name'] = movie.xpath('./h5/a/@title').extract()[0]
            item['href'] = movie.xpath('./h5/a/@href').extract()[0]

            tv = movie.xpath('./span[@class="mjtv"]/text()')

            if len(tv):
                item['tv'] = tv.extract()[0]

            else:
                item['tv'] = ''

            yield item


