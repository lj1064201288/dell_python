# import re
# import json
# import requests
# from bs4 import BeautifulSoup
#
# url = "https://talent.baidu.com/baidu/web/httpservice/getPostList?recruitType=2&pageSize=10&curPage=1"
#
# headers = {
#     "Accept":"application/json, text/javascript, */*; q=0.01",
#     "Accept-Encoding":"gzip,deflate,br",
#     "Accept-Language":"zh-CN,zh;q=0.9",
#     "Connection":"keep-alive",
#     "Content-Type":"application/x-www-form-urlencoded",
#     "Cookie":"BAIDUID=584A0EABFB5FA77738E86731C51999B1:FG=1;BIDUPSID=584A0EABFB5FA77738E86731C51999B1;PSTM=1535809183;BDORZ=B490B5EBF6F3CD402E515D22BCDA1598;JSESSIONID=E9E7951236F30EAAB1860B4B29264057.dayee-client2;CCK=rO0ABXNyABRqYXZhLnNlY3VyaXR5LktleVJlcL35T7OImqVDAgAETAAJYWxnb3JpdGhtdAASTGphdmEvbGFuZy9TdHJpbmc7WwAHZW5jb2RlZHQAAltCTAAGZm9ybWF0cQB%2BAAFMAAR0eXBldAAbTGphdmEvc2VjdXJpdHkvS2V5UmVwJFR5cGU7eHB0AANERVN1cgACW0Ks8xf4BghU4AIAAHhwAAAACOV6bgFFwT2idAADUkFXfnIAGWphdmEuc2VjdXJpdHkuS2V5UmVwJFR5cGUAAAAAAAAAABIAAHhyAA5qYXZhLmxhbmcuRW51bQAAAAAAAAAAEgAAeHB0AAZTRUNSRVQ%3D;Hm_lvt_50e85ccdd6c1e538eb1290bc92327926=1538935839,1538971376,1538978843,1539066049;Hm_lpvt_50e85ccdd6c1e538eb1290bc92327926=1539066049",
#     "Host":"talent.baidu.com",
#     "Referer": "https://talent.baidu.com/external/baidu/index.html",
#     "User-Agent":"Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,like Gecko) Chrome/69.0.3497.81 Safari/537.36",
#     "X-Requested-With":"XMLHttpRequest"
# }
#
# params = {
#
# }
#
# response = requests.get(url)
# print(requests.json())

# if response.status_code == 200:
#     html = response.text
#
# soup = BeautifulSoup(html, 'lxml')
#
# # print(soup.prettify())
#
# print("###" * 50)
# #print(soup.p)
# # p = soup.find_all('postList')
# p = str(soup.p)
# # print(type(p))
# # print(p)
#
#
# # data = json.loads(p)
# # print(type(data))
# data = re.sub('<p>|</p>', ' ', p)
# # print(data)
# data = data.strip()
# # print(data)
# # print(type(data))
# data = json.loads(data)
# data = data["postList"]
# # print(data)
#
# datas = re.sub(r'<br/>', '', str(data))
# # datas = re.sub(r'\r', ' ', datas)
# datas = re.sub("'", '"', datas)
# # soup = BeautifulSoup(datas, 'lxml')
# # print(soup.prettify())
# # print(datas)
# # print(type(datas))
# datas = json.loads(datas)


# for i in range(len(datas)):
#     serviceConditions = []
#     serviceConditions.append(datas[i]['serviceCondition'])
#     serviceConditions = re.sub(r'\r', ',', serviceConditions[0])
#     print(serviceConditions)

# url = "https://talent.baidu.com/baidu/web/httpservice/getPostList?recruitType=2&pageSize=10&curPage=1"
# item = re.search('curPage=(\d+)', url).group(1)
# page = int(item) + 1
# url = re.sub("curPage=(\d+)", "curPage=" + str(page), url)
# print(url)
from urllib import request

url = "https://www.taobao.com"

response = request.urlopen(url)
content = response.read()
html = content.decode('utf-8')
print(html)


