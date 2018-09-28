'''
爬取腾讯招聘网站
'''
from urllib import request
from bs4 import BeautifulSoup

def Tencent():

    url = "https://hr.tencent.com/position.php?keywords=&tid=0&lid=2268"

    rsp = request.urlopen(url)
    html = rsp.read()

    soup = BeautifulSoup(html, 'lxml')

    tr1 = soup.select('tr[class="even"]')
    tr2 = soup.select('tr[class="odd"]')
    trs = tr1 + tr2
    for tr in trs:
        name = tr.select('td a')[0].get_text()
        print(name)
        href = tr.select('td a')[0].attrs['href']
        print(href)
        attr = tr.select('td')[1].get_text()
        print(attr)
        city = tr.select('td')[3].get_text()
        print(city)
        data = tr.select('td')[4].get_text()
        print(data)

        print("*" * 50)
    #for tr in name:


if __name__ == '__main__':

    Tencent()