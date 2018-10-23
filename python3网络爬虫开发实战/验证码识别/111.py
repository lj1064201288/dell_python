# import math
# import requests
# from lxml import etree
#
# url = "https://cd.fang.lianjia.com/loupan/jinjiang/pg1"
# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36"
# }
# response = requests.get(url, headers=headers)
# text = response.text
# html = etree.HTML(text)
# items = html.xpath('//div[@class="page-box"]/@data-total-count')[0].strip()
# end_page = math.ceil(int(items) / 10)
# print(end_page)
# import re
# a = "jinjiang-qingyang-wuhou-gaoxin7-chenghua-jinniu-tianfuxinqu-gaoxinxi1-shuangliu-wenjiang-pidou-longquanyi-xindou-qingbaijiang-jintang-dayi-pujiang-xinjin-pengzhou-qionglai-chongzhou1-doujiangyan-jianyang-tianfuxinqunanqu-deyang-leshan-meishan-ziyang"
# b = re.sub('-', "','", a)
# print(b)

import pypinyin

a = '我来了'
b = pypinyin.pinyin(a, style=pypinyin.NORMAL)
c = ''
for d in b:
    c += ''.join(d)
print(c)