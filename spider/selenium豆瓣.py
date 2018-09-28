from selenium import webdriver
from lxml import etree
import time
import json

def get_wed():

    url = "https://book.douban.com/subject_search?search_text=python&cat=1001"

    driver = webdriver.Chrome()
    driver.get(url)

    time.sleep(3)
    driver.save_screenshot("豆瓣.png")

    fn = "豆瓣读书.html"

    with open(fn, 'w', encoding='utf-8') as f:
        f.write(driver.page_source)

    content_page(fn)

    driver.quit()

def content_page(fn):

    html = ""

    with open(fn, 'r', encoding='utf-8') as r:
        html = r.read()

    tree = etree.HTML(html)
    contents = tree.xpath('//div[@class="item-root"]')

    for content in contents:

        book_dict = {}

        book = content.xpath('.//div/a[@class="title-text"]')
        #print(book[0].text.strip())
        if len(book):
            book_dict["书名"] = book[0].text.strip()

        author = content.xpath('.//div[@class="meta abstract"]')
        if len(author):
            book_dict["作者/出版社/发布时间/价格"] = author[0].text.strip()

        evaluate = content.xpath('.//span[@class="pl"]')
        if len(evaluate):
            book_dict["评价人数"] = evaluate[0].text.strip()


        pf = content.xpath('.//span[@class="rating_nums"]')
        if len(pf):
            book_dict["评分"] = pf[0].text.strip()

        python_books.append(book_dict)

    # books = tree.xpath('//div/a[@class="title-text"]')
    # authors = tree.xpath('//div[@class="meta abstract"]')
    # evaluates = tree.xpath('//span[@class="pl"]')
    # pfs = tree.xpath('//span[@class="rating_nums"]')

    # for i in range(15):
    #     for book in books:
    #         book_dict["书名"] = book.text.strip()
    #
    #
    #     for author in authors:
    #         book_dict["作者/出版社/发布时间/价格"] = author.text.strip()
    #
    #
    #     for evaluate in evaluates:
    #         book_dict["评价人数"] = evaluate.text.strip()
    #
    #
    #     for pf in pfs:
    #         book_dict["评分"] = pf.text.strip()
    #
    #     python_books.append(book_dict)





if __name__ == '__main__':

    python_books = []

    get_wed()

    js = json.dumps(python_books, indent=5)
    print(js)

    # with open('豆瓣读书.json', encoding='utf-8') as f:
    #     f.writable(js)
    #
    book = str(python_books)

    with open("豆瓣读书.json", 'w') as f:
        f.write(book)


