'''
导入scrapy
所有类一般是xxxspider
所有爬虫类都是scrapy.Spider的子类
'''

import scrapy

class BaiduScrapy(scrapy.Spider):

    # name 是爬虫的名称
    name = "baidu"

    # 起始url列表
    start_urls = ['http://www.baidu.com']

    # 负责分析downloader下载得到的结果
    def parse(self, response):
        '''
        只是保存网页即可
        :param response:
        :return:
        '''
        with open('baidu.html', 'w', encoding='utf-8') as f:
            f.write(response.body.decode('utf-8'))

