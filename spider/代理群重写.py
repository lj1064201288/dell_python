from urllib import request, error

proxy_list = [
    {'http':'114.215.95.188:3128'},
    {'http':'140.143.105.246:80'},
    {'http':'204.48.26.161:8080'},
    {'http':'213.131.47.194:8080'},
    {'http':'94.242.58.142:10010'}
    ]

#　创建proxyhandler群
proxyhandler_list = []
for proxy in proxy_list:
    proxyhandler = request.ProxyHandler(proxy)
    proxyhandler_list.append(proxyhandler)

# 创建opener
opener_list = []
for opener_handler in proxyhandler_list:
    opener = request.build_opener(opener_handler)
    opener_list.append(opener)

if __name__ == '__main__':

    import random

    url = "http://www.ganji.com"

    #　安装opener
    try:
        opener = random.choice(opener_list)
        request.install_opener(opener)

        rsp = request.urlopen(url)
        html = rsp.read().decode()
        print(html)

        with open("赶集.html", 'w') as f:
            f.write(html)

    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)


