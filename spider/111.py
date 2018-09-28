import requests
from lxml import etree

if __name__ == '__main__':

    url = "https://hr.163.com/position/list.do?positionName=&currentPage=1"

    html = requests.get(url)

    html = etree.HTML(html.text)

    title = html.xpath('//table[@class="position-tb"]/tbody/tr')
    print(len(title))

    for t in title:

        name = t.xpath('.//div[1]/p/text()')
        if len(name):
            print(str(name))
            print('***' * 50)
        else:
            pass

