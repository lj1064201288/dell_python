import re
import scrapy
from hrqq_item.items import HrqqItem

class HrqqSpider(scrapy.Spider):

    name = 'qq'

    allowed_domains = ['hr.tencent.com']

    start_urls = ['https://hr.tencent.com/position.php?&start=0#a']

    def parse(self, response):

        info1 = response.xpath('//table[@class="tablelist"]/tr[@class="even"]')
        info2 = response.xpath('//table[@class="tablelist"]/tr[@class="odd"]')
        infos = info2 + info1

        for info in infos:

            item = HrqqItem()

            title = info.xpath('./td[1]/a/text()')
            href = info.xpath('./td[1]/a/@href')
            position = info.xpath('./td[2]/text()')
            num = info.xpath('./td[3]/text()')
            worklocation = info.xpath('./td[4]/text()')
            time = info.xpath('./td[5]/text()')

            if len(title):
                item['title'] = title.extract()[0]
            else:
                item['title'] = None

            if len(href):
                item['href'] = href.extract()[0]
            else:
                item['href'] = None

            if len(position):
                item['position'] = position.extract()[0]
            else:
                item['position'] = None

            if len(num):
                item['worklocation'] = worklocation.extract()[0]
            else:
                item['worklocation'] = None

            if len(time):
                item['time'] = time.extract()[0]
            else:
                item['time'] = None

            curpage = re.search('(\d+)', response.url).group(1)

            page = int(curpage) + 10

            url = re.sub('(\d+)', str(page), response.url)

            yield scrapy.Request(url, callback=self.parse)

            yield item