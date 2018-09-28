from urllib import request
from bs4 import BeautifulSoup

if __name__ == '__main__':

    url = "https://www.ganji.com"
    rsp = request.urlopen(url)
    content = rsp.read()

    soup = BeautifulSoup(content, 'lxml')
    # content = soup.prettify()
    # print(content)

    print(soup.title)
    print(soup.link)
    print(soup.name)
    print(soup.attrs)
    print(soup.title.string)
    print(soup.head)
    print(soup.meta)
    print(type(soup.meta))