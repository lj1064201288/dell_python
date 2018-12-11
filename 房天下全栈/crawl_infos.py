import re
import csv
import math
import time
import random
import chardet
import requests
# 导入MongoDB的模块
from MongoDb_write import Mongo_DB
from lxml import etree
# 导入爬取西刺代理第一页的代理列表
#from get_proxys import test_ip


#proxys = test_ip()
proxys = [
    "58.53.128.83:3128",
    "110.84.208.56:8118",
    "124.243.226.18:8888",
    "14.221.165.167:8118",
    "219.234.5.128:3128",
    "110.184.189.146:8118",
    "110.73.42.32:8123",
    "175.18.93.98:80",
    "180.164.24.165:53281",
    "219.238.186.188:8118",
    "106.15.42.179:33543",
    "118.122.92.252:37901",
    "114.223.165.185:8118",
    "123.7.61.8:53281",
    "101.236.55.145:8866",
    "61.135.217.7:80",
    "118.190.94.224:9001",
    "58.242.136.18:808",
    "101.132.142.124:8080",
    "121.33.220.158:808",
    "171.37.163.68:8123",
    "222.171.251.43:40149",
    "116.7.176.75:8118",
    "114.224.135.99:8118",
    "218.17.139.5:808",
    "180.103.223.210:8118",
    "183.63.123.3:56489",
    "202.104.113.35:53281",
    "222.182.121.228:8118",
    "58.218.201.188:58093",
    "125.40.29.100:8118",
    "116.227.128.77:39791",
    "183.3.150.210:41258",
    "113.108.242.36:47713",
    "139.129.207.72:808",
    "182.101.11.101:808",
    "61.178.238.122:63000",
    "221.210.120.153:54402",
    "221.224.136.211:35101",
    "218.76.253.201:61408",
    "182.111.64.7:41766",
    "180.104.107.46:45700",
    "171.37.163.126:8123",
    "58.210.133.98:32741",
    "61.184.109.33:61320",
    "59.52.184.164:42694",
    "125.67.25.83:41681"
]

class crwal_ftx(object):
    def __init__(self, city, url, write):
        self.city = city
        self.url = url
        self.num = 1
        self.page = 100
        self.type = ''
        self.write = write


    def parse_info(self, last_html):
        pass

    def get_html(self, url):
        # 随机获取浏览器
        agent = random.choice(agents)
        # 随机获取代理
        proxy = random.choice(proxys)

        # 构建headers头
        headers = {
            'User-Agent':agent,
        }

        # 构建代理
        proxies = {
            'http': 'http://' + proxy
        }
        # 设置异常
        try:
            response = requests.get(url, headers=headers, timeout=5)
            if response.status_code == 200:
                # 获取页面的编码格式
                charset = chardet.detect(response.content)['encoding']
                # 设置页面的编码格式
                html = response.content.decode(charset, 'ignore')
                # 返回得到的页面信息
                return html

            else:
                print('获取页面失败')
        except Exception as e:
            print(e.args)
            time.sleep(2)
            # 如果超过三次获取失败后取消
            while self.num:
                self.get_html(url)


    def get_house(self):
        for i in range(0,self.page):
            # 使用re正则提取出页面的页数然后加一
            num = re.search('(\d+)', self.url).group()
            page = int(num) + i
            new_url = re.sub('(\d+)', str(page), self.url)
            # 获取每一页的html
            html = self.get_html(new_url)
            print('开始获取第{0}页的信息'.format(i+1))
            # 将页面传入子页面获取函数
            self.get_subpage(html)
            time.sleep(5)

    def get_subpage(self, html):
        pass

    def Write_MySql(self):
        pass

    def Write_Csvs(self, items):
        for item in items:
            print(item)
            lptags = list(item.keys())
            lpstates = list(item.values())
            with open(self.city + self.type + '.csv', 'a', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(lptags)
                writer.writerow(lpstates)
                print('存储第{0}条信息成功!'.format(self.num) )
                self.num += 1

    def run(self):
        pass

    def MongoDB_Writer(self, items):
        # 获取到城市的前拼
        collection = self.url.split('.')[0].split('//')[1]
        # 将获取到的数据存入数据库
        for item in items:
            mongo_db = Mongo_DB(self.type, collection, item)
            mongo_db.run_sql()


agents = [
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0",
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
]


class new_house(crwal_ftx):
    # 继承主类的构造函数
    def __init__(self, city, url, write):
        super().__init__(city, url, write)
        self.page = 0
        self.type = 'newhouse'

    # 解析需要的数据页面
    def parse_info(self, last_html):
        # 构建字典
        item = {}
        # 分析页面内容
        content = etree.HTML(last_html)
        # 楼盘名称
        title = content.xpath('//a[@class="ts_linear"]/text()')
        if title:
            item["楼盘名称"] = title[0].strip()
        # 楼盘价格
        price = content.xpath('//div[@class="main-info-price"]/em/text()')
        if price:
            item['价格'] = price[0].strip()

        # 楼盘评论
        remark = content.xpath('//a[@class="comment"]/span/text()')
        if remark:
            rem = ''
            for rem in remark:
                    rem += ''.join(rem).replace(' ', '')
            item['用户点评'] = rem.strip()
        else:
            item['用户点评'] = None
        # 获取到房子的详细信息
        li1 = content.xpath('//ul[@class="list clearfix"]/li')
        li2 = content.xpath('//ul[@class="clearfix list"]/li')
        lis = li1 + li2
        lptypes = []
        lpstates= []
        for li in lis:
            lptype = ''
            lpstate = ''
            infos = li.xpath('div[@class="list-left"]/text()')
            for info in infos:
                lptype += ''.join(info.strip())
            lptype = re.sub('：', '', lptype)
            lptypes.append(lptype.replace(' ', ''))
            info1 = li.xpath('div[@class="list-right"]/text()')
            info2 = li.xpath('div[@class="list-right-floor"]/text()')
            info1 = info1 + info2
            for info in info1:
                lpstate += ''.join(info.strip())
            lpstates.append(lpstate.replace(' ', ''))
        # 将楼盘信息打包成字典
        infos = dict(zip(lptypes, lpstates))
        # 将楼盘信息的字典添加到提取的数据里面
        for k, v in infos.items():
            item[k] = v
        # 返回数据生成器
        yield item

    # 获取楼盘的页数
    def get_page(self):
        # 请求第一个页面
        html = self.get_html(self.url)
        content = etree.HTML(html)
        # 获取楼盘的数量
        nums = content.xpath('//div[@class="page"]/ul/li/b/text()')[0]
        # 每页20个求出多少页
        self.page += math.ceil(int(nums) / 20)

    # 进入子页面进行处理
    def get_subpage(self, html):
        # 解析第一页的内容
        content = etree.HTML(html)
        # 获取到每个楼盘的url
        hrefs = content.xpath('//div[@class="nlcd_name"]/a/@href')
        for href in hrefs:
            frist_url = 'http:' + href
            print(frist_url)
            # 进入主页
            time.sleep(1)
            frist_html = self.get_html(frist_url)
            frist_content = etree.HTML(frist_html)
            # 获取到详细页面的url
            last_url = "http:" + frist_content.xpath('//div[@class="navleft tf"]/a/@href')[1]
            print(last_url)
            # 进入详细页面
            last_html = self.get_html(last_url)
            # 将详细页面的url发送到解析页面进行解析并返回给一个对象
            items = self.parse_info(last_html)
            # 对页面进行存储
            if self.write == 'csv':
                self.Write_Csvs(items)
            if self.write == 'MongoDB':
                self.MongoDB_Writer(items)
    def run(self):
        self.get_page()
        self.get_house()

    def MongoDB_Writer(self, items):
        # print(items)
        # 获取到城市的前拼
        collection = self.url.split('.')[0].split('//')[1]
        mongo_db = Mongo_DB(self.type, collection, items)
        mongo_db.run_sql()




#二手房的类继承新房类
class esf_house(crwal_ftx):
    def __init__(self, city, url, write):
        super().__init__(city, url, write)
        self.type = 'esf'
        self.host = self.url.split('/')[2]

    # 进入子页面
    def get_subpage(self, html):
        # 解析页面的信息
        content = etree.HTML(html)
        # 得到每个二手房的url
        hrefs = content.xpath('//h4[@class="clearfix"]/a/@href')
        for href in hrefs:
            last_url = 'http://' + self.host + href
            # 获取页面的html
            last_html = self.get_html(last_url)
            # 把需要获取的信息页面传入解析方法解析
            items = self.parse_info(last_html)
            # 对信息进行存储
            if self.write == 'csv':
                self.Write_Csvs(items)
            if self.write == 'MongoDB':
                self.MongoDB_Writer(items)

    def parse_info(self, last_html):
        item = {}
        content = etree.HTML(last_html)
        title = content.xpath('//h1[@class="title floatl"]/text()')
        if title:
            item['标题'] = title[0].strip()

        total_price = content.xpath('//div[@class="trl-item price_esf  sty1"]/i/text()')
        if total_price:
            item['总价'] = total_price[0] + '万元'

        info_types = content.xpath('//div[@class="font14"]/text()')
        info_contents = content.xpath('//div[@class="tt"]/text()')
        infos = dict(zip(info_types, info_contents))
        for k,v in infos.items():
            item[k] = v

        yield item

    def run(self):
        self.get_house()

class zf_house(crwal_ftx):
    def __init__(self, city, url, write):
        super().__init__(city, url, write)
        self.type = 'zf'
        self.host = self.url.split('/')[2]

    def get_subpage(self, html):
        # 解析页面的信息
        content = etree.HTML(html)
        # 得到每个租房的url
        hrefs = content.xpath('//p[@class="title"]/a/@href')
        for href in hrefs:
            last_url = 'http://' + self.host + href
            # 获取页面的html
            last_html = self.get_html(last_url)
            # 把需要获取的信息页面传入解析方法解析
            items = self.parse_info(last_html)
            # 对信息进行存储
            if self.write == 'csv':
                self.Write_Csvs(items)
            if self.write == 'MongoDB':
                self.MongoDB_Writer(items)

    def parse_info(self, last_html):
        item = {}
        # 解析最后的页面
        content = etree.HTML(last_html)
        title = content.xpath('//div/h1/text()')
        if title:
            item['标题'] = title[0].strip()

        price = content.xpath('//div[@class="tr-line clearfix zf_new_title"]/descendant:: */text()')
        if price:
            item['租金'] = price[0].strip() + price[1].strip()

        info_types = content.xpath('//div[@class="font14"]/text()')
        info_contents = content.xpath('//div[@class="tt"]/text()')
        infos = dict(zip(info_types, info_contents))
        for k, v in infos.items():
            item[k] = v

        yield item

    def run(self):
        self.get_house()

#house = zf_house('成都', 'http://anshan.zu.fang.com/house/i31/', 'csv')
#
#house.run()
#house.Write_Csvs()