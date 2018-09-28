from urllib import error, request
import random

# 创建proxy群

proxy_list = [
    {"https": "218.60.8.99:3129"},
    {"http": "223.202.204.195:80"},
    {"https": "101.37.79.125:3128"},
    {"https": "218.207.212.86:80"},
    {"https": "218.60.8.98:3129"},
    {"http": "121.8.98.196:80"},
    {"http": "125.62.26.197:3128"},
    {"https": "223.202.204.194:80"},
    {"http": "140.143.105.243:80}"},
    {"http": "121.8.98.197:80"},
    {"http": "140.143.105.246:80"},
    {"http": "140.143.105.245:80"},
    {"https": "114.215.95.188:3128"},
    {"http": "94.242.58.108:10010"},
    {"https": "113.200.56.13:8010"},
    {"http": "60.8.42.134:8908"},
    {"http": "94.242.58.142:10010"},
    {"http": "60.195.198.245:3128"},
    {"http": "13.56.105.158:80"},
    {"http": "139.217.24.50:3128"}

]

# 创建proxy_handler
proxy_handler_list = []
for proxy_handler in proxy_list:
    proxyhandler = request.ProxyHandler(proxy_handler)
    proxy_handler_list.append(proxyhandler)

#　创建opener
opener_list = []
for opener in proxy_handler_list:
    openerlist = request.build_opener(opener)
    opener_list.append(openerlist)

# 主函数,需要运行的函数
if __name__ == '__main__':

    url = "http://www.gaiji.com"

    try:
        opener = random.choice(opener_list)
        request.install_opener(opener)

        rsp = request.urlopen(url)
        html = rsp.read().decode()
        print(html)

    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)
