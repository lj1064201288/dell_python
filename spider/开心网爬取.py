from urllib import request, parse
from http import cookiejar
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

#　创建opener
cookie = cookiejar.CookieJar()
cookie_handler = request.HTTPCookieProcessor(cookie)
http_handler = request.HTTPHandler()
https_handler = request.HTTPSHandler()

opener = request.build_opener(cookie_handler, http_handler, https_handler)

def login():

    login_url = "https://security.kaixin001.com/login/login_post.php"

    data = {
        "email":"13550211725",
        "password":"liujun19960106"
    }

    data = parse.urlencode(data)

    headers = {
        "Content-Lenght": len(data),
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36"
    }

    rsp = request.Request(login_url, data=data.encode(), headers=headers)

    html = opener.open(rsp)
    html = html.read().decode()
    print(html)

if __name__ == '__main__':

    login()

