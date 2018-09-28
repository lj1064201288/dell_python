'''
爬取百度贴吧当中关于Taylor的帖子源码
总共爬取10页的源码进行保存
'''

from urllib import request, parse


if __name__ == '__main__':

    # 获取百度贴吧url
    baseurl = "http://tieba.baidu.com/f?"

    # 创建要发送的信息
    qs = {
        'kw':'泰勒斯威夫特',
        'ie':'utf-8',
        'pn':0
    }

    urls = []
    filenames = []
    # 贴吧每一页的属性为50条信息,创建url列表
    for i in range(10):
        pn = i * 50
        qs['pn'] = str(pn)
        filenames.append('Taylor' + str(i))
        urls.append(baseurl+parse.urlencode(qs))

    # 创建存储源码的列表
    htmls = []
    for url in urls:
        rsp = request.urlopen(url)
        html = rsp.read().decode()
        htmls.append(html)

    # 对源码进行保存
    for j in range(10):

        with open(filenames[j]+'.xml', 'w') as f:
            f.write(htmls[j])
