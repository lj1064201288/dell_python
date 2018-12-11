'''
项目目标:
    1.获取百度实习生招聘的所有招聘信息,首页url为:https://talent.baidu.com/baidu/web/httpservice/getPostList?
    2.使用re正则进行简单清洗
    3.最好以json格式保存只文档当中
分析:
    1.百度招聘的每一页面属性为Ajax,打开页面params属性发现规律,curPage为页面的页数,_为打开页面的时间戳,所以这里需要使用到params
    2.爬取下来的数据格式为json

'''

import re
import json
import requests
import time
from urllib.parse import urlencode

# 获取页面信息
def get_page(page):

    # params中有一个值为当前时间戳乘于1000
    date = time.time() * 1000

    # 构建params
    params = {
        "workPlace": "0/4/7/9",
        "recruitType": 12,
        "pageSize": 10,
        "curPage": page,
        "_": date
    }

    # 构建headers头
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip,deflate,br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Host":"talent.baidu.com",
        "Referer": "https://talent.baidu.com/external/baidu/index.html",
        "User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,like Gecko) Chrome/69.0.3497.81 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }

    url = "https://talent.baidu.com/baidu/web/httpservice/getPostList?" + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        # 判断是否获取成功
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except Exception as e:
        print(e.args)

def parse_page(data):

    items = data["postList"]

    for item in items:
        baidu = {}

        baidu = item
        # 由于发现有的信息当中是没有serviceCondition的内容,所以这里使用了判断语句
        if "serviceCondition" in baidu.keys():
            baidu['serviceCondition'] = re.sub(r'\r<br>', " ", baidu['serviceCondition']).strip()
        baidu['workContent'] = re.sub(r'\r<br>', " ", baidu['workContent']).strip()


        yield baidu

# 保存爬下来的数据
def write_page(info):

    content = json.dumps(info, ensure_ascii=False) + "\n"
    with open("百度.json", 'a') as f:
        f.write(content)


if __name__ == '__main__':

    for i in range(1,16):

        time.sleep(2)
        print(i)
        data = get_page(i)
        #print(data)
        infos = parse_page(data)

        for info in infos:
            write_page(info)


