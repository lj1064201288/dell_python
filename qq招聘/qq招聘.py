'''
爬取qq招聘成都的所有信息
分析:
    1.qq招聘上面关于成都的招聘一共有58条,每页10条,一共6页
    2.创建一个url列表,对列表里的url依次进行访问
    3.使用bs4进行数据提取
    4.然后把数据存储在文件当中
'''

from urllib import request
from bs4 import BeautifulSoup



def qq(url):
    rsp = request.urlopen(url)

    html = rsp.read()

    soup = BeautifulSoup(html, 'lxml')

    tr1 = soup.select('tr[class="even"]')
    tr2 = soup.select('tr[class="odd"]')
    trs = tr1 + tr2

    for tr in trs:
        recs = {}
        name = tr.select('td a')[0].get_text()
        recs["标题"] = name
        href = tr.select('td a')[0].attrs['href']
        recs["链接"] = href
        attr = tr.select('td')[1].get_text()
        recs["职业"] = attr
        city = tr.select('td')[3].get_text()
        recs["城市"] = city
        release_time = tr.select('td')[4].get_text()
        recs["发布时间"] = release_time

        infos.append(recs)


if __name__ == '__main__':

    url_list = []
    infos = []
    for i in range(0, 60, 10):
        url = "https://hr.tencent.com/position.php?keywords=&tid=0&lid=2268&start={0}#a".format(i)
        url_list.append(url)

    for url in url_list:
        qq(url)

    # for info in infos:
    #     print(info)
    #     s = str(info)
    #     with open("qq招聘.json", 'a') as f:
    #         f.writelines(s)
    js = str(infos)

    with open("qq招聘.json", 'w') as f:
        f.write(js + "\n")

