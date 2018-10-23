import time
from pyquery import PyQuery as pq
from urllib.parse import quote
from selenium import webdriver


def get_port(start_page):
    page = (start_page - 1) * 60
    url = "https://list.tmall.com/search_product.htm?s={page}&q={commodity}".format(page=str(page), commodity=commodity)
    browser.get(url)

    html = browser.page_source
    #get_parse(html)
    time.sleep(5)
    start_page += 1

    input = browser.find_element_by_css_selector(".ui-page-skipTo")
    input.clear()
    input.send_keys(str(start_page))

    if start_page <= 80:
        browser.find_element_by_css_selector('.ui-btn-s').click()

#def get_parse(html):



if __name__ == '__main__':


    start_page = int(input("请输入从第几页开始爬取:"))
    commodity = quote(input("请输入你要查询的商品:"))
    browser = webdriver.Chrome()
    get_port(start_page)

