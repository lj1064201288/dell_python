'''
构建代理集群/队列
每次访问服务器,随机抽取一个代理
抽取可以使用　random.choice

分析步骤:
1.构建代理群
2.每次访问,随机选取代理并执行
'''

from urllib import request, error


#　设置代理地址
proxy_list = [
    # 列表中存放的是dict类型的元素
    {"http":"115.217.253.107:32682"},
    {"http":"58.212.42.95:23115"},
    {"http":"222.85.50.196:808"},
    {"http":"123.53.118.126:32040"},
    {"http":"49.85.6.176:47480"},
    {"http":"118.190.95.43:9001"},
]

# 2. 创建ProxyHandler
proxy_handler_list = []
for proxy in proxy_list:
    proxy_handler = request.ProxyHandler(proxy)
    proxy_handler_list.append(proxy_handler)

# 创建opener
opener_list = []
for proxy_handler in proxy_handler_list:
    opener = request.build_opener(proxy_handler)
    opener_list.append(opener)


import random

url = "https://www.ganji.com"

try:
    # 4.安装opener
    opener = random.choice(opener_list)
    request.install_opener(opener)

    rsp = request.urlopen(url)
    html = rsp.read().decode()
    print(html)
except error.URLError as e:
    print(e)
except Exception as e:
    print(e)

