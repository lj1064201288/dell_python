import re
import scrapy
from item_wangyi.items import WangyiItem

class WangyiSpider(scrapy.Spider):

    name = 'wangyi'

    allowed_domains = ["hr.163.com"]

    start_urls = ["https://hr.163.com/position/list.do?positionName=&currentPage=1"]

    def parse(self, response):

        infos = response.xpath('//table[@class="position-tb"]/tbody/tr')

        for info in infos:

            item = WangyiItem()

            title = info.xpath('./td[1]/a/text()')

            href = info.xpath('./td[1]/a/@href')

            position = info.xpath('./td[2]/text()')

            work_type = info.xpath('./td[3]/text()')

            work_location = info.xpath('./td[4]/text()')

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

            if len(title):
                item['work_type'] = work_type.extract()[0].strip()
            else:
                pass

            if len(work_location):
                item['work_location'] = work_location.extract()[0].strip()
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

