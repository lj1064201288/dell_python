import re
import scrapy
from item_hrtencent.items import HrTencentItem

class Tencent_Spider(scrapy.Spider):

    name = 'tencent'

    allowed_domains = ['hr.tencent.com']

    start_urls = ['https://hr.tencent.com/position.php?&start=0#a']

    def parse(self, response):

        info1 = response.xpath('//table[@class="tablelist"]/tr[@class="even"]')
        info2 = response.xpath('//table[@class="tablelist"]/tr[@class="odd"]')
        infos = info1 + info2

        for info in infos:

            item = HrTencentItem()

            title = info.xpath('./td[@class="l square"]/a/text()')
            href = info.xpath('./td[@class="l square"]/a/@href')
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
                item['num'] = num.extract()[0]
            else:
                item['num'] = None

            if len(worklocation):
                item['worklocation'] = worklocation.extract()[0]
            else:
                item['worklocation'] = None

            if len(time):
                item['time'] = time.extract()[0]
            else:
                item['time'] = None


            change = re.search('(\d+)', response.url).group(1)

            page = int(change) + 10

            url = re.sub('(\d+)', str(page), response.url)

            yield scrapy.Request(url, callback=self.parse)

            yield item