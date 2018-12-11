import time
import requests
import random
from lxml import etree
agents = [
            "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
            "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
            "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0",
            "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)"
        ]
class citys():

    def __init__(self):
        self.url = "http://www.fang.com/SoufunFamily.htm"

    def get_response(self):

        agent = random.choice(agents)

        headers = {
                "User-Agent": agent,
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8Accept-Encoding:gzip,deflateAccept-Language:zh-CN,zh;q=0.9",
                "Cache-Control":"max-age=0",
                "Connection":"keep-alive",
                "Host":"www.fang.com",
                "Referer":"http://wuhan.newhouse.fang.com/house/s/?ctm=1.sh.xf_search.head.11",
                "Upgrade-Insecure-Requests":"1",
        }

        try:
            response = requests.get(self.url, headers=headers)

            if response.status_code == 200:
                return response.text
            else:
                print(response.status_code)
                self.get_response()
        except Exception as e:
            time.sleep(2)
            print(e.args)
            self.get_response()


    def parse_citys(self):

        html = self.get_response()
        content = etree.HTML(html)
        citys = content.xpath('//div[@class="onCont"]/table/tr/td/a')

        item = {}
        for city in citys:
            href = city.xpath('./@href')[0]
            name = city.xpath('./text()')[0]

            item[name] = href
        if item:
            return item
        else:
            print("获取城市失败...")


