import re
import scrapy
from item_wangyihr.items import WangyiHrItem

class WangyiSpider(scrapy.Spider):

    name = 'wangyihr'

    allowed_domains = ['hr.163.com']
    start_urls = ['https://hr.163.com/position/list.do?currentPage=1']

    def parse(self, response):

        infos = response.xpath('//table[@class="position-tb"]/tbody/tr')

        for info in infos:

            item = WangyiHrItem()

            title = info.xpath('./td/a/text()')
            href = info.xpath('./td/a/@href')
            position = info.xpath('./td[2]/text()')
            work_type = info.xpath('./td[3]/text()')
            worklocation = info.xpath('./td[4]/text()')
            num = info.xpath('./td[5]/text()')
            time = info.xpath('./td[6]/text()')

            if len(title):
                item['title'] = title.extract()[0].strip()
            else:
                pass

            if len(href):
                item['href'] = href.extract()[0].strip()
            else:
                pass

            if len(position):
                item['position'] = position.extract()[0].strip()
            else:
                pass

            if len(work_type):
                item['work_type'] = work_type.extract()[0].strip()
            else:
                pass

            if len(worklocation):
                item['worklocation'] = worklocation.extract()[0].strip()
            else:
                pass

            if len(num):
                item['num'] = num.extract()[0].strip()
            else:
                pass

            if len(time):
                item['time'] = time.extract()[0].strip()
            else:
                pass

            curpage = re.findall('(\d+)', response.url)

            page = int(curpage[1]) + 1

            url = re.sub('[=](\d+)', '='+str(page), response.url)

            yield scrapy.Request(url, callback=self.parse)

            if len(item):
                yield item
