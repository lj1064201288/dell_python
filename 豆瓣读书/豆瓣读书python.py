'''
爬取豆瓣读书关于python的书籍并保存
要求:
    1.先是获取豆瓣阅读的源代码,使用selenium获取源码后进行保存
    2.使用etree对源码进行解析,需要的数据有书名,作者,发布时间,出版社,价格,评价人数,评分
    3.把解析之后的数据存入文档当中
分析:
    1.豆瓣读书首页url("https://book.douban.com/subject_search?search_text=python&cat=1001&start=0")
    2.可以得到每个页面书籍的数量是以start控制的
    3.使用list创建一个url列表
    3.之后对url_list进行依次访问获取数据
    4.考虑到读取的url较多,所以每页只是截图保存,源码就每一页写下来之后都保存至同一个文档进行覆盖
'''

from selenium import webdriver
from lxml import etree
import time
import json

def get_douban(url, num):

    # 创建driver
    driver = webdriver.Chrome()

    driver.get(url)
    # 为了防止页面还未加载完毕,所以让程序等待2秒钟
    time.sleep(2)

    # 对所要爬取的网页进行截图d
    driver.save_screenshot("豆瓣读书" + str(num) + ".png")

    # 截图的文件名称,随着页面的改变而改变,之后保存
    fn = "豆瓣读书源码.html"
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(driver.page_source)

    # 防止源码还未读取完毕,程序等待2秒
    time.sleep(2)
    content_douban(fn)

    # 读取完毕之后,退出浏览器
    driver.quit()

def content_douban(fn):

    html = ""

    with open(fn, 'r', encoding='utf-8') as r:
        html = r.read()

    # 创建etree
    html = etree.HTML(html)
    contents = html.xpath('//div[@class="item-root"]')

    for content in contents:

        # 创建存储数据的dict
        python_book_dict = {}

        # 获取书名
        book = content.xpath('.//div/a[@class="title-text"]')
        if len(book):
            python_book_dict["书名"] = book[0].text

        # 获取作者/翻译/出版社/发布时间/价格
        author = content.xpath('.//div[@class="meta abstract"]')
        # 判断数据是否存在,如果没有者不保存
        if len(author):
            python_book_dict["作者/翻译/出版社/发布时间/价格"] = author[0].text

        # 获取评价人数
        evaluation = content.xpath('.//span[@class="pl"]')
        if len(evaluation):
            python_book_dict["评价人数"] = evaluation[0].text
        # 获取评分
        pf = content.xpath('.//span[@class="rating_nums"]')
        if len(pf):
            python_book_dict["评分"] = pf[0].text

        # 将获取的数据进行保存至列表当中
        datas.append(python_book_dict)

if __name__ == '__main__':

    # 创建列表存储数据
    datas = []
    # url = "https://book.douban.com/subject_search?search_text=python&cat=1001&start=15"
    # get_douban(url, 15)

    # 获取每一页的url
    for i in range(0,1711,15):
        url = "https://book.douban.com/subject_search?search_text=python&cat=1001&start={0}".format(i)
        get_douban(url, int(i/15))

    filename = "豆瓣图书python.json"

    # 对数据以json进行保存进行保存
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(datas, f, indent=5)
    #
    # filename = "豆瓣图书python.json"
    # with open(filename, 'r', encoding='utf-8') as r:
    #     data = json.load(r)
    #
    # for d in data:
    #     print(d)

    # str_data = str(datas)
    # with open("douban.json", 'a') as f:
    #     f.write(str_data)












