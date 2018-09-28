'''项目要求: 1. 爬取赶集网成都的python招聘职位,然后将所有的招聘信息的标题全部提取到一个文件当中
            2. 一共爬取15页招聘信息,如果没有,则爬取到最大
'''

from urllib import request,error,parse
from bs4 import BeautifulSoup
import time
import re
from lxml import etree

if __name__ == '__main__':

    url = "http://cd.ganji.com/site/s/_python/"

    rsp = request.urlopen(url)
    content = rsp.read()

    soup = BeautifulSoup(content,"lxml")

    #text = soup.prettify()
    text = soup.title
    print(text)
    text = soup.div.div.div
    print(text)


