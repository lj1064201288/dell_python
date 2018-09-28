'''
抓取扇贝单词中关于python的单词
分析：
    1.访问url("https://www.shanbay.com/wordlist/187711/540712/?page=1")
    2.可以看出每一页的是由page控制的,可以做一个列表进行依次访问
    3.提取出的数据使用json进行保存
'''
from urllib import request
from lxml import etree
import json



def page(n):

    # 页面的url
    url = "https://www.shanbay.com/wordlist/187711/540712/?page=" + str(n)

    rsp = request.urlopen(url)

    # 创建etree
    html = rsp.read()
    html = etree.HTML(html)

    # 对数据进行解析
    tr_list = html.xpath('//tr[@class="row"]')
    for tr in tr_list:
        # 创建一个dict用于保存每一次抓取下来的数据
        word = {}

        # 获取单词
        strong = tr.xpath('.//strong')
        # 判断提取时是否有数据
        if len(strong):
            # 对数据进行简单的清洗
            name = strong[0].text.strip()
            word['name'] = name
        # 获取单词的解释
        word_content = tr.xpath('.//td[@class="span10"]')
        if len(word_content):
            content = word_content[0].text.strip()
            word['content'] = content
        # 判断是否提取数据成功,如果有,者添加至列表当中
        if word != {}:
            words.append(word)



if __name__ == '__main__':

    # 创建一个存储数据的列表
    words = []

    # 一共爬取10页数据
    for i in range(1,11):
        page(i)

    # 查看单词的个数
    print(len(words))
    # for w in words:
    #     j = str(w)
    #     with open("扇贝单词1.json", 'a') as f:
    #         f.write(j)

    # s = str(words)

    #json_sql = json.loads("s")

    # with open("扇贝单词.json", 'w') as f:
    #     f.write(s)

    filename = "扇贝单词.json"

    #　对趴下来的数据以json的方式进行保存
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(words, f, indent=5)

