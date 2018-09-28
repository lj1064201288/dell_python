'''
爬取扇贝单词上面关于python的常用单词
分析:
1. 获取扇贝的python单词书的url
2. 进入页面把数据进行提取
3. 把提取的数据使用json格式进行保存
'''

from urllib import request
from lxml import etree


def shanbay(num):

    url = "https://www.shanbay.com/wordlist/187711/540712/?page="+str(num)

    rsp = request.urlopen(url)
    rep = rsp.read()

    html = etree.HTML(rep)
    tr_list = html.xpath('//tr[contains(@class,"row")]')

    words = []

    for tr in tr_list:

        word = {}

        td_name = tr.xpath('.//strong')
        # print(name[0].text.strip())
        if len(td_name):
            name = td_name[0].text.strip()
            word['name'] = name

        td_content = tr.xpath('./td[@class="span10"]')
        if len(td_content):
            content = td_content[0].text.strip()
            #print(content[0].text.strip())
            word['content'] = content
        if word != {}:
            words.append(word)

    for w in words:
        print(w)


if __name__ == '__main__':
    shanbay(1)