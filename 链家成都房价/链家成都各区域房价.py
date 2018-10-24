import os
import csv
import math
import pypinyin
import requests
from lxml import etree

class Chengdu(object):

    #初始化地址,页数,内容,url
    def __init__(self, locat):
        self.locat = locat
        self.page = 0
        self.content = ''
        self.url = 'https://cd.fang.lianjia.com/loupan/{0}/'.format(self.locat)

    # 获取该地区有多少房子的信息,并传入给self.page
    def get_end_page(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                text = response.text
                html = etree.HTML(text)
                num = html.xpath('//div[@class="page-box"]/@data-total-count')[0]
                end_page = math.ceil(int(num)/10)
                self.page = end_page
            else:
                print('访问失败')
        except Exception as e:
            print(e)

    # 把每一页的源码返回到下一步进行解析
    def get_items(self):

        for page in range(1, self.page+1):
            url = self.url + 'pg' + str(page)
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    self.content = response.text
                    yield self.content
            except:
                print("ContentError!!!")

    # 解析页面,获取需要的数据,每获取到一条者返回一条信息
    def get_parse(self):
        if self.get_items():
            for info in self.get_items():
                html = etree.HTML(info)
                items = html.xpath('//div/ul[@class="resblock-list-wrapper"]/li')

                for item in items:
                    houses = []
                    houses.append(item.xpath('./div[@class="resblock-desc-wrapper"]/div/a/text()')[0].strip())
                    houses.append(item.xpath('./div[@class="resblock-desc-wrapper"]/div/span/text()')[0].strip())
                    houses.append(item.xpath('./div[@class="resblock-desc-wrapper"]/div/span/text()')[1].strip())
                    locat = item.xpath('.//div[@class="resblock-location"]/a/text()')
                    houses.append('/'.join(item.xpath('.//div[@class="resblock-location"]/span/text()') + locat))
                    area = item.xpath('.//div[@class="resblock-area"]/span/text()')
                    if area:
                        houses.append(area[0].strip())
                    else:
                        houses.append('没有说明')
                    houses.append('/'.join(item.xpath('.//div[@class="resblock-tag"]/span/text()')))
                    houses.append(''.join(item.xpath('.//div[@class="main-price"]/span/text()')))

                    yield houses

    # 对获取到的信息进行保存,以excel表格的方式进行存储
    def write_csv(self):

        file_path =  '链家' + os.sep + self.locat + os.sep
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        file = open(file_path + self.locat + '.csv', 'a')
        writer = csv.writer(file)
        writer.writerow(['名称', '类型', '状态', '地址', '面积', '标签', '价格'])

        content_generator = self.get_parse()
        for content in content_generator:
            print(content)
            content = list(content)
            writer.writerow(content)

        file.close()

# 实例化对象执行爬虫
def main(city):
    lianjia = Chengdu(city)
    lianjia.get_end_page()
    lianjia.get_items()
    lianjia.get_parse()
    lianjia.write_csv()

# 获取输入的地址
def city_locat(area):
    pinyin_locat = pypinyin.pinyin(area, pypinyin.NORMAL)
    locat = ''
    for pinyin in pinyin_locat:
        locat += ''.join(pinyin)
    if area == '高新':
        locat = locat + '7'
    if area == '高新西':
        locat = locat + '1'
    citys = ['jinjiang','qingyang','wuhou','gaoxin7','chenghua','jinniu','tianfuxinqu','gaoxinxi1','shuangliu','wenjiang','pidou','longquanyi','xindou','qingbaijiang','jintang','dayi','pujiang','xinjin','pengzhou','qionglai','chongzhou1','doujiangyan','jianyang','tianfuxinqunanqu','deyang','leshan','meishan','ziyang']

    if locat in citys:
        index = citys.index(locat)
        main(citys[index])
    else:
        print('没有这个城市,请重新输入!')

if __name__ == '__main__':

    # 输入想要获取的地区,输入q退出获取
    while True:
        area = input('请输入需要获取的地区(输入q退出):')

        if area == 'q':
            break

        city_locat(area)


