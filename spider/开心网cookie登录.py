from urllib import request
from http import cookiejar
import ssl

cookie = cookiejar.MozillaCookieJar()
cookie.load("cookie.txt", ignore_discard=True, ignore_expires=True)

cookie_handler = request.HTTPCookieProcessor(cookie)
http_handler = request.HTTPHandler()
https_handler = request.HTTPSHandler()

opener = request.build_opener(cookie_handler, http_handler, https_handler)

ssl._create_default_https_context = ssl._create_unverified_context

def getHomePage():
    base_url = "http://www.kaixin001.com/home/?_profileuid=181784205&t=93"

    rsp = opener.open(base_url)
    http = rsp.read().decode()

    with open("开心网cookie登录.html", 'w') as f:
        f.write(http)

if __name__ == '__main__':

    getHomePage()