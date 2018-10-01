# 导入需要使用的模块
import re
import scrapy
# 调取事先写好的Item
from hrqq_item.items import HrqqItem

class HrqqSpider(scrapy.Spider):

    # 设置项目名称
    name = 'qq'

    # 设置只能在这个域名下访问
    allowed_domains = ['hr.tencent.com']

    # 设置开始的页面
    start_urls = ['https://hr.tencent.com/position.php?&start=0#a']

    def parse(self, response):

        info1 = response.xpath('//table[@class="tablelist"]/tr[@class="even"]')
        info2 = response.xpath('//table[@class="tablelist"]/tr[@class="odd"]')
        # 提取需要的数据
        infos = info2 + info1

        for info in infos:

            # 创建Item
            item = HrqqItem()

            title = info.xpath('./td[1]/a/text()')
            href = info.xpath('./td[1]/a/@href')
            position = info.xpath('./td[2]/text()')
            num = info.xpath('./td[3]/text()')
            worklocation = info.xpath('./td[4]/text()')
            time = info.xpath('./td[5]/text()')

            # 判断是否为空
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

            # 提取出页面控制页数的数字
            curpage = re.search('(\d+)', response.url).group(1)

            # 对提取出来的数字进行增加
            page = int(curpage) + 10

            # 将增加过的数字重新拼接到新的url当中
            url = re.sub('(\d+)', str(page), response.url)

            # 对新的URL进行返回再执行parse
            yield scrapy.Request(url, callback=self.parse)

            yield item