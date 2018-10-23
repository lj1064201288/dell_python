'''
1. 爬取豆瓣电影排行榜首页
2. 检查安装requests
3. 使用正则表达式提取电影名称,评分,评价,演员,时间再保存至文件当中
'''

import re
import requests
import json
from requests.exceptions import RequestException


def get_one_page(url):

    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text

    except RequestException:
        return None

    # 保存豆瓣电影排行榜首页的源码


def parse_one_page(html):

    items = re.findall('<table.*?<a\sclass="nbg"\shref="(.*?)".*?title="(.*?)".*?img\ssrc="(.*?)".*?</a>.*?<p.*?class="pl">(\d+.\d+.\d+).*?/\s(\D.*?)</p>.*?class="rating_nums">(.*?)</span>.*?class="pl">(.*?)</span>', html, re.S)
    print(items)
    for item in items:
        yield {
            'href':item[0].strip(),
            'title':item[1].strip(),
            'img':item[2].strip(),
            'time':item[3].strip(),
            'actor':item[4].strip(),
            'grade':item[5].strip(),
            'evaluate':item[6].strip()
        }

def write_one_page(content):

    with open('豆瓣.txt', 'a', encoding='UTF-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


if __name__ == '__main__':

    url = "https://movie.douban.com/chart"
    html = get_one_page(url)

    for item in parse_one_page(html):
        print(item)
        write_one_page(item)