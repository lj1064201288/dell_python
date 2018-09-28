'''
爬取登录开心网，利用cookie
免除ssl
'''
'''
步骤:
1.寻找登录入口:"通过搜查相应的文字可以快速定位"
    login_url = "https://security.kaixin001.com/login/login_post.php"
    相应的用户名和密码对应名称为emall,passwoed
2. 构造opener
3. 构造login函数
'''

from urllib import request, parse
from http import cookiejar
import ssl

# 忽略安全问题
ssl._create_default_https_context = ssl._create_unverified_context

cookie = cookiejar.CookieJar()
cookie_handler = request.HTTPCookieProcessor(cookie)
http_handler = request.HTTPHandler()
https_handler = request.HTTPSHandler()

opener = request.build_opener(cookie_handler, http_handler, https_handler)

def login():
    login_url = "https://security.kaixin001.com/login/login_post.php"

    data = {
        "email":'13550211725',
        "password":"liujun19960106"
    }
    # 对post的内容进行编码
    data = parse.urlencode(data)

    # http的请求头
    headers = {
        "Content-Lenght":len(data),
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36"
    }

    # 构造请求对象Request对象
    # data要求是一个bytes对象,需要进行编码
    rep = request.Request(login_url, data=data.encode(), headers=headers)

    rsp = opener.open(rep)

    html = rsp.read()
    html = html.decode()
    #print(html)

    with open("开心网.html", 'w') as f:
        f.write(html)

def getHomePage():
    base_url = "http://www.kaixin001.com/home/?_profileuid=181784205&t=98"
    rsp = opener.open(base_url)
    html = rsp.read().decode()
    print(html)


if __name__ == '__main__':

    login()
    getHomePage(