from urllib import request, parse


if __name__ == '__main__':

    baseurl = "http://tieba.baidu.com/f?"

    qs = {
        'kw': 'Avril',
        'ie': 'utf-8',
        'pn': 0
    }
    urls = []
    filename = []

    for i in range(5):
        pn = i * 50
        filename.append('Avril' + str(i))
        qs['pn'] = str(pn)
        urls.append(baseurl + parse.urlencode(qs))
    #print(filename)

    htmls = []
    for url in urls:
        rsp = request.urlopen(url)
        html = rsp.read().decode()
        htmls.append(html)


    #print(htmls[0])
    for j in range(5):
        with open(filename[j]+'.html', 'w') as f:
            f.write(htmls[j])
