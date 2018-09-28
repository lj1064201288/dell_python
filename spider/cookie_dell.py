from urllib import request, parse
from http import cookiejar
import ssl

# 创建cookie
filename = "cookie.txt"
cookie = cookiejar.MozillaCookieJar(filename)

cookieHandler = request.HTTPCookieProcessor(cookie)
httphandler = request.HTTPHandler()
httpshandler = request.HTTPSHandler()

opener = request.build_opener(cookieHandler, httphandler, httpshandler)

ssl._create_default_https_context = ssl._create_unverified_context

def login():
    login_url = "https://security.kaixin001.com/login/login_post.php"

    data = {
        "email":"13550211725",
        "password":"liujun19960106"
    }

    headers = {
        "Content-Lenght":len(data),
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36"
    }

    data = parse.urlencode(data)

    base_url = request.Request(login_url, data=data.encode(), headers=headers)

    rsp = opener.open(base_url)

    cookie.save(ignore_discard=True, ignore_expires=True)

def getHomePage():

    url = "http://www.kaixin001.com/home/?_profileuid=181784205&t=93"

    rsp = opener.open(url)

    html = rsp.read().decode()

    with open("开心网cookie.html", 'w') as f:
        f.write(html)

if __name__ == '__main__':
    login()
    getHomePage()

