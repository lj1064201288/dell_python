'''
爬取百度贴吧-王力宏吧
1.　王力宏吧的主页是　http://tieba.baidu.com/f?ie=utf-8&kw=%E7%8E%8B%E5%8A%9B%E5%AE%8F
2. 进去之后,贴吧有很多页
    第一页的网址:http://tieba.baidu.com/f?kw=%E7%8E%8B%E5%8A%9B%E5%AE%8F&ie=utf-8&pn=0
    第二页的网址:http://tieba.baidu.com/f?kw=%E7%8E%8B%E5%8A%9B%E5%AE%8F&ie=utf-8&pn=50
    第三页的网址:http://tieba.baidu.com/f?kw=%E7%8E%8B%E5%8A%9B%E5%AE%8F&ie=utf-8&pn=100
    第四页的网址:http://tieba.baidu.com/f?kw=%E7%8E%8B%E5%8A%9B%E5%AE%8F&ie=utf-8&pn=150
    第五页的网址:http://tieba.baidu.com/f?kw=%E7%8E%8B%E5%8A%9B%E5%AE%8F&ie=utf-8&pn=200
3. 由上面的网址可以找到规律,每一页只有后面数字不同,且数字应该是(页数-1)*50

解决问题:
1.准备构建参数字典
    字典包含案部分, kw,ie, pn
2. 使用parse构建完整的url
3.　使用for循环下载
'''

from urllib import request, parse

if __name__ == '__main__':

    # 1.准备构建函数
    qs = {
        'kw': '王力宏',
        'ie': 'utf-8',
        'pn': 0
    }

    # 2.使用parse构建完整的url
    # 假定只需要前10页
    urls = []
    baseurl = "https://tieba.baidu.com/f?"
    for i in range(10):
        pn = i * 50
        qs['pn'] = str(pn)
        #　把qs编码后和基础url进行拼接
        # 拼接完毕后装入url列表中
        urls.append(baseurl + parse.urlencode(qs))
    print(urls)
    # 3. 使用for循环下载
    baurl = []
    for url in urls:
        rsp = request.urlopen(url)
        html = rsp.read().decode('utf-8')
        print(url)
        print(html)



