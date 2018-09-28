from urllib import request, parse
from bs4 import BeautifulSoup

if __name__ == '__main__':

    url = "https://www.sogou.com/web?"

    qe = {
        "query":"大熊猫"
    }

    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }

    data = parse.urlencode(qe)
    print(type(data))
    print(data)

    baseurl = url + data
    print(baseurl)


    baseurl = request.Request(baseurl, headers=headers)
    rsp = request.urlopen(baseurl)
    rep = rsp.read()

    soup = BeautifulSoup(rep, 'lxml')
    #content = soup.prettify()
    #print(content)

    print(soup.name)
    print(soup.meta)
    print(soup.title)
    print(soup.link)
    print(soup.title.string)
    print(type(soup.link))

