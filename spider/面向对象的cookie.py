from urllib import request, error, parse
from http import cookiejar
import ssl


def login():

    url = "https://www.mxdxlove.cn/login/"

    data = {
        "username": "13550211725",
        "password":"liujun19960106"
    }

    data = parse.urlencode(data).encode()

    headers = {
    "Accept": "text/html, application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q = 0.8",
    "Accept-Encoding":"gzip,deflate,br:",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Host": "www.mxdxlove.cn",
    "Upgrade-Insecure-Requests": '1',
    "User-Agent":"Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/69.0.3497.81Safari/537.36"
    }

    rsp = request.Request(url, data=data, headers=headers)
    http = request.urlopen(rsp)
    print(http.read().decode())

if __name__ == '__main__':
    login()