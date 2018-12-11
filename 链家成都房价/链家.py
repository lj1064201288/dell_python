import re
import time
import os
import csv
import requests
from lxml import etree


def get_locat(city, pg):
    for page in range(1, pg+1):
        url = 'https://cd.fang.lianjia.com/loupan/{0}/pg{1}'.format(city, str(page))
        try:
            response = requests.get(url)
            if response.status_code == 200:
                yield response.text
        except:
            print('Error')


def parse(text):
    for i in text:
        html = etree.HTML(i)
        items = html.xpath('//div/ul[@class="resblock-list-wrapper"]/li')

        for item in items:
            houses = {}
            houses['title'] = item.xpath('./div[@class="resblock-desc-wrapper"]/div/a/text()')[0].strip()
            houses['type'] = item.xpath('./div[@class="resblock-desc-wrapper"]/div/span/text()')[0].strip()
            houses['status'] = item.xpath('./div[@class="resblock-desc-wrapper"]/div/span/text()')[1].strip()
            locat = item.xpath('.//div[@class="resblock-location"]/a/text()')
            houses['locat'] = '/'.join(item.xpath('.//div[@class="resblock-location"]/span/text()') + locat)
            area = item.xpath('.//div[@class="resblock-area"]/span/text()')
            if area:
                houses['area'] = area[0].strip()
            else:
                houses['area'] = '没有说明'
            houses['tag'] = '/'.join(item.xpath('.//div[@class="resblock-tag"]/span/text()'))
            houses['price'] = ''.join(item.xpath('.//div[@class="main-price"]/span/text()'))
            yield  houses

# def get_write(item, city):
#
#     file = open()



if __name__ == '__main__':

    text = get_locat('jinjiang', 6)
    item = parse(text)
    #get_write(item)