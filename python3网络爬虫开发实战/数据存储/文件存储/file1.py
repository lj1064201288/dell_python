'''
1.目标:
    保存知乎上发现页面的热门话题部分,将其问题和答案统一保存文本形式
2. 基本实例:
    首先,可以用requests将网页源代码获取下来,然后使用pyquery解析库解析,接下来提取标题,回答者,回答保存到文本
'''

import requests
from pyquery import PyQuery as pq

url = "https://www.zhihu.com/explore"

headers = {
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36"
}
try:
    html = requests.get(url, headers=headers)
    if html.status_code == 200:
        html = html.text
        with open('知乎.html', 'w') as f:
            f.write(html)
    doc = pq(html)
    divs = doc('#js-explore-tab .feed-item').items()
    print(divs)
    print(type(divs))
    for div in divs:
        print(type(div))
        question = div.find('h2').text()
        author = div.find('.author-link-line').text()
        answer = pq(div.find('.content').html()).text()
        with open('explore.txt', 'a', encoding='utf-8') as f:
            f.write('\n'.join([question, author, answer]))
            f.write('\n' + "=" * 50 + '\n')
except Exception as e:
    print(e)

