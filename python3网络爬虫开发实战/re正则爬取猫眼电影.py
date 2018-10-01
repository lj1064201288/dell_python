'''
1.爬取猫眼电影TOP100的相关内容
2.检查是否安装好requests
3.使用re提取电影名称,时间,评分,评论,图片等信息,提取的结果会以文件的形式保存下来
'''

import requests
import re
import json
import time
from requests.exceptions import RequestException

# 抓取首页
def get_one_page(url):
    try:
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.text

    except RequestException:
        return None

def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',re.S)
    items = re.findall(pattern, html)
    # print(items)
    for item in items:
        yield{
            'index':item[0],
            'image':item[1],
            'title':item[2].strip(),
            'actor':item[3].strip()[3:] if len(item[3]) > 3 else '',
            'time':item[4].strip()[5:] if len(item[4]) > 5 else '',
            'score':item[5].strip() + item[6].strip()
        }

def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        #print(type(json.dumps(content)))
        f.write(json.dumps(content, ensure_ascii=False)+'\n')


def main(offset):
    url = 'http://www.maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    # print(html)
    # with open('猫眼电影.html', 'w') as f:
    #     f.write(html)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)

if __name__ == '__main__':

    for i in range(10):
        main(offset=i*10)
        time.sleep(1)
