# import time
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# url = "https://s.taobao.com/search?q=iPad&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306"
# cookies = {
#         "t":"004b2784566ddb5070766028b97eb0ca",
#         "thw":"cn, cna:dR5zFK94vFoCAXwOiz6GSdIN",
#         "v":"0",
#         "cookie2":"1154d6be0319c798f6d1aa87b138cd35",
#         "_tb_token_":"eeee4e7e56a4b",
#         "unb":"2121265944",
#         "sg":"%E4%B8%B64b",
#         "_l_g_":"Ug%3D%3D",
#         "skt":"226eaf0c77a03d21",
#         "cookie1":"AQGkUGFgeGYVFo17DQ7%2FZ%2Fah8TXUDFNyYnoZl9vOMx0%3D",
#         "csg":"0bb4a629",
#         "uc3":"vt3:F8dByR6tHqjmREK57Tc%3D&id2:UUkM9qmL8wumqw%3D%3D&nk2:hVTL33Mee3g6C1L7WYI%3D&lg2:V32FPkk%2Fw0dUvg%3D%3D",
#         "existShop":"MTU0MjUzMDk5MA%3D%3D",
#         "tracknick":"%5Cu7E9F%5Cu5BAB%5Cu5546%5Cu89D2%5Cu5FB5%5Cu7FBD%5Cu4E36",
#         "lgc":"%5Cu7E9F%5Cu5BAB%5Cu5546%5Cu89D2%5Cu5FB5%5Cu7FBD%5Cu4E36",
#         "_cc_":"V32FPkk%2Fhw%3D%3D",
#         "dnk":"%5Cu7E9F%5Cu5BAB%5Cu5546%5Cu89D2%5Cu5FB5%5Cu7FBD%5Cu4E36",
#         "_nk_":"%5Cu7E9F%5Cu5BAB%5Cu5546%5Cu89D2%5Cu5FB5%5Cu7FBD%5Cu4E36",
#         "cookie17":"UUkM9qmL8wumqw%3D%3D",
#         "tg:0, mt":"ci:7_1",
#         "enc":"PPVobhhwi4CuKJ0Wm1va1RJnwjsxS9MDqtxwdBFM%2F857%2FO1NxwiEtYJfjfjTF6r3nyBYyBPb2gSVbTk0SN1%2FHg%3D%3D",
#         "JSESSIONID":"79EA261C1CAA2EEDCB95D79A6E2715F5",
#         "alitrackid":"www.taobao.com",
#         "lastalitrackid":"www.taobao.com",
#         "cookie15":"W5iHLLyFOGW7aA%3D%3D",
#         "hng":"CN%7Czh-CN%7CCNY%7C156",
#         "x":"e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0 ",
#         "swfstore":"168758",
#         "isg":"BAMDd-TVXJvm9RBWIejE1_Hcksdt0Jfc4AAwfTXgPWLI9CIWvUvbCq9uasQf1O-y",
# }
#
# driver = webdriver.Chrome()
# driver.get(url)
# driver.add_cookie(cookies)
# time.sleep(2)
#
# driver.save_screenshot('淘宝.png')
# with open("淘宝.html", 'w') as f:
#     f.write(driver.page_source)
#
# name = driver.find_element_by_id("TPL_username_1").send_keys("2574019428@qq.com")
# password = driver.find_element_by_id("TPL_password_1")
# password.send_keys("lj1064201288")
# password.send_keys(Keys.ENTER)
#
# driver.save_screenshot('淘宝1.png')
# time.sleep(2)
import pymongo
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq
from config import *
from urllib.parse import quote

# browser = webdriver.Chrome()
# browser = webdriver.PhantomJS(service_args=SERVICE_ARGS)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)

wait = WebDriverWait(browser, 10)
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]


def index_page(page):
    """
    抓取索引页
    :param page: 页码
    """
    print('正在爬取第', page, '页')
    try:
        url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
        browser.get(url)
        print(browser.page_source)
        if page > 1:
            input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input')))
            submit = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit')))
            input.clear()
            input.send_keys(page)
            submit.click()
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page)))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
        get_products()
    except TimeoutException:
        index_page(page)


def get_products():
    """
    提取商品数据
    """
    html = browser.page_source
    print(html)
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'image': item.find('.pic .img').attr('data-src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text(),
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
        print(product)
        save_to_mongo(product)


def save_to_mongo(result):
    """
    保存至MongoDB
    :param result: 结果
    """
    try:
        if db[MONGO_COLLECTION].insert(result):
            print('存储到MongoDB成功')
    except Exception:
        print('存储到MongoDB失败')


def main():
    """
    遍历每一页
    """
    for i in range(1, MAX_PAGE + 1):
        index_page(i)
    browser.close()


if __name__ == '__main__':
    main()