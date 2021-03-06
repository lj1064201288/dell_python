'''
实战演练
    1. 模拟这些Ajax请求,将前10页的微博全部爬取下来
'''

from pyquery import PyQuery as pq
from urllib.parse import urlencode
import requests


# 定义一个url的前半部分
base_url = "https://m.weibo.cn/api/container/getIndex?"

# 构造headers
headers = {
    "Accept":"application/json, text/plain, */*MWeibo-Pwa:1",
    "Referer": "https://m.weibo.cn/u/2830678474",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "Host":"m.weibo.cn"
}

def get_page(page):
    # 构造参数字典
    params = {
        "type": "uid",
        "value": "2830678474",
        "containerid": "1076032830678474",
        "page": page
    }

    # 调用uelencode()方法将参数转化为URL和GET请求参数
    url = base_url + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        # 判断是否请求成功
        if response.status_code == 200:
            return response.json()
    # 捕获异常
    except requests.ConnectionError as e:
        print("Error", e.args)

def parse_page(json):
    if json:

        items = json.get('data').get('cards')

        for item in items:

            item = item.get('mblog')
            weibo = {}
            print(item)
            weibo["id"] = item.get('id')
            weibo['text'] = pq(item.get('text')).text()
            weibo['attitudes'] = item.get('attitudes_count')
            weibo['comments'] = item.get('comments_count')
            weibo['reposts'] = item.get('reposts_count')

            yield weibo

if __name__ == '__main__':
    for page in range(1, 11):
        json = get_page(page)
        results = parse_page(json)
        for result in results:
            print(result)
