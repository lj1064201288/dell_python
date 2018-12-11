import re
from urllib import request, parse
#
# a = "http://anshan.fang.com/house/s/b92/"
#
# result  = a.split('.')
# result.insert(1, "esf")
# result = '.'.join(result)
# num = re.search('(\d+)', result).group()
# page = int(num) + 1
# url = re.sub('(\d+)', str(page), result)
# print(url)
#import headers.txt
#
# def read_header():
#     with open('headers', 'r') as r:
#         data = r.read()
#         return data
#
# a = read_header()
# print(dict(a))
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
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
        "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)"
]
import random
import requests
from bs4 import BeautifulSoup
from lxml import etree
from urllib import request, parse
from http.cookiejar import CookieJar

# cookie = CookieJar()
#
# cookie_handler = request.HTTPCookieProcessor(cookie)
# http_handler = request.HTTPHandler()
# https_handler = request.HTTPSHandler()
#
# opener = request.build_opener(cookie_handler, http_handler, https_handler)

# agent = random.choice(agents)
# headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
#         "Cookie":'global_cookie=gysxj5x0ynb100ds09iyd67go1cjool2tvs; integratecover=1; new_search_uid=952c1e291f0214d601a5158c46d93fad; searchLabelN=1_1542653015_170%5B%3A%7C%40%7C%3A%5D6267f1ef69402caf708e4f1281a25f70; searchConN=1_1542653015_919%5B%3A%7C%40%7C%3A%5D07c856047f1e5692353c45897f51f24b; passport=username=&password=&isvalid=1&validation=; Integrateactivity=notincludemc; SoufunSessionID_Office=1_1542733014_482; newhouse_user_guid=D10FE4F6-C033-311A-A38D-1CF62DD62257; vh_newhouse=1_1542733036_625%5B%3A%7C%40%7C%3A%5Dbc21a9e1138de7a3ed1d0b9fb3510f96; city=cd; showAdcd=1; __utmz=147393320.1542913318.9.6.utmcsr=cd.newhouse.fang.com|utmccn=(referral)|utmcmd=referral|utmcct=/house/s/b91/; __utma=147393320.822014318.1542648488.1542913318.1542990885.10; __utmc=147393320; __utmt_t0=1; __utmt_t1=1; __utmt_t2=1; __utmt_t3=1; __utmt_t4=1; __utmb=147393320.25.10.1542990885; unique_cookie=U_nkidqhipp6sdln46f6cucuea02rjou8xktc*5',
#         "Accept-Encoding": "gzip, deflate"
# }
#
#
# url = "https://cd.newhouse.fang.com/house/s/b91"
# response = requests.get(url, headers=headers)
# print(response.text)
#
# with open('fangtianxia.html', 'w' ,encoding='utf-8') as f:
#         f.write(response.text)
# rep = request.Request(url, headers=headers)
# response = opener.open(rep)
#
#
# print(cookie)
#
# for i in response:
#         with open('cookie.txt', 'w', encoding='utf-8') as f:
#                 f.write(i.d)
# html = response.text
# soup = BeautifulSoup(html, 'lxml')
# title = soup.select('title')
# print(title)
# response = request.Request(url,headers=headers)
# response = request.urlopen(response)
# print(response.read().decode())

import chardet
# import zlib
#
# if __name__ == "__main__":
#         url='http://cd.newhouse.fang.com/house/s/'
#         req = request.Request(url)
#         response = request.urlopen(req, timeout=120)
#         html = response.read()
#
#         encoding = response.info().get('Content-Encoding')
#
#         if encoding == 'gzip':
#                 html = zlib.decompress(html, 16+zlib.MAX_WBITS)
#         elif encoding == 'deflate':
#                 try:
#                         html = zlib.decompress(html, -zlib.MAX_WBITS)
#                 except zlib.error:
#                         html = zlib.decompress(html)
#
#         charset = chardet.detect(html)["encoding"]
#         print(charset)
#         #print(html)
#         print(html.decode(charset,'ignore'))
#from get_proxys import write_proxy

#proxys = write_proxy()
#proxy = random.choice(proxys)
# proxies = {
#         'https': "https://" + proxy
# }
import zlib
agent = random.choice(agents)
headers = {
        "Upgrade-Insecure-Requests": "1",
        'User-Agent': agent
}
url = "http://cd.zu.fang.com/chuzu/3_202829499_1.htm?"
response = requests.get(url, headers=headers)
#html = response.text
charset = chardet.detect(response.content)['encoding']
html = response.content.decode(charset, 'ignore')
#print(charset)
#encoding = response.content.decode('GBK', 'ignore')#['Content-Encoding']
#print(encoding)
#html = response.text.encode(encoding, 'ignore')

#print(html)
#html = response.content.decode('GB2312', 'ignore')
# with open('fangtianxia.html', 'w', encoding='utf-8') as f:
#         f.write(html)
# with open('fangtianxia.html', 'r', encoding='utf-8') as r:
#         html = r.read()
#
#print(html)

from pyquery import PyQuery as pq
#soup = BeautifulSoup(html, 'xml')
#item = soup.find(class_='list clearfix')
#print(soup.prettify())
# item = {}
# doc = pq(html)
# left = doc.find('.list-left')
# right = doc('.list-right')
# print(len(left))
# lefts = []
# rights = []
# #print(lis[3].text)
# for l in left:
#         left.append(l.text)
#
# for r in right:
#         right.append(r.text)
#
# print(lefts)
# print(rights)

#print(lis.text())
#print(lis[11].text.strip())
#print(html)
ls = etree.HTML(html)
# li = ls.xpath('//div[@class="tt"]/text()')
# #film = ''
# for fit in li:
#         print(fit)
# print(film.strip())
li1 = ls.xpath('//div[@class="tt"]/text()')
li2 = ls.xpath('//div[@class="font14"]/text()')
lis = li1 + li2
#item_type = []
# item = []
# for li in li1:
#         # ifs = ''
#         # ifx = ''
#         item_type.append(li.strip())
# for li in li2:
#         item.append(li.strip())
#
# infos = dict(zip(item, item_type))
# print(infos)
print(lis)

        # infos = li.xpath('div[@class="list-left"]/text()')
        # for info in infos:
        #         ifx += ''.join(info.strip())
        # ifx = re.sub('：', '', ifx)
        # item.append(ifx)
        # info1 = li.xpath('div[@class="list-right"]/text()')
        # info2 = li.xpath('div[@class="list-right-floor"]/text()')
        # info1 = info1 + info2
        # for info in info1:
        #         ifs += ''.join(info.strip())
        # item_type.append(ifs)
# print(item_type)
# print(len(item_type))
# print(item)
# print(len(item))
#print(dict(zip(item, item_type)))
# for r in right:
#         rights.append(r.strip())
# lefts = left.split('：')
# print(len(lefts))
# print(type(lefts))
# # for l in lefts:
# #         print(l)
# print(lefts)
# print(rights)
# item = {}
# a = zip(lefts, rights)
#print(list(a))
# print(lis[0], lis[1])
# for li in lis:
#         price = li.xpath('./dd/h4/a/@href')
#        # unit_price = li.xpath('./dd[@class="price_right"]/span/text()')
#         #for unit in price:
#                 #price += '.'.join(unit)
#         if price:
#                 print(price[0])

#fitment = li.select('div')[1]
#print(li)
# li = lis[1]
# aa = li.xpath('./ul[@class="list clearfix"]/li')
# print(len(aa))
# for a in aa:
#         b = a.xpath('./div[@class="list-right"]/text()')
#         print(b)
#title = html.xpath('.//')
# url = "http://cd.newhouse.fang.com/house/s/b91/"
#
# hrefs = []
#
# for b in range(0, 39):
#         num = re.search('(\d+)',url).group()
#         page = int(num) + b
#         new_url = re.sub('(\d+)', str(page), url)
#         hrefs.append(new_url)
# for href in hrefs:
#         print(href)
