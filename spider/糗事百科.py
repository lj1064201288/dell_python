'''
项目实战2:
1. 爬取糗事百科的段子跟用户名称与点赞次数,进行保存
2. 使用xpath进行提取数据
3. 最后使用json格式进行保存
'''

from lxml import etree
import requests
import json

if __name__ == '__main__':

    url = "https://www.qiushibaike.com/"

    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36",
        "Accept":'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        "Accept-Encoding":"gzip, deflate, br",
        "Accept-Language":"h-CN,zh;q=0.9"
    }

    rsp = requests.get(url, headers=headers)
    rep = rsp.text
    #print(rep)

    html = etree.HTML(rep)
    print(html)
    rst = html.xpath('//div[contains(@id, "qiushi_tag")]')
    #print(rst)

    for r in rst:
        item = {}
        print(type(r))
        #print(r)

        content = r.xpath('//div[@class="content"]/span')
        for c in content:
            print(c.text.strip())
        # print(type(content))
        # print(content)

