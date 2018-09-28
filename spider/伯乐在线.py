'''
爬取伯乐在线的美女的联系方式
需要:
1.登录
2. 在登录和相应声望的前提下,提取对方的邮箱
'''

from urllib import request, error, parse
from http import cookiejar
import json


def login():
    '''
    输入用户名和密码
    获取相应的登录cookie
    cookie 写文件
    :return:
    '''

    #　需要找到登录入口
    url = "http://date.jobbole.com/wp-login.php"
    #　准备登录数据
    data = {
        "log": "augsnano",
        "pwd": "123456789",
        "wp-submit": "登录",
        #　登录定向的地址
        "redirect_to": "http://date.jobbole.com/wp-admin/",
        "testcookie": 1
    }

    data = parse.urlencode(data).encode()

    #　3.准备存放cookie文件
    # r　表示不转义
    f = r"jobbole_cookie.txt"

    #　准备请求头信息
    headers = {
        "User_Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36",
        "Connection": "keep-aliive"
    }

    # 5.准备cookie_handler
    cookie_handler = cookiejar.MozillaCookieJar(f)

    # 6.准备http请求handler
    http_handler = request.HTTPCookieProcessor(cookie_handler)

    # 7.构建opener
    opener = request.build_opener(http_handler)

    # 8.构建请求对象
    rep = request.Request(url, data=data, headers=headers)

    # 9.发送请求
    try:
        rsp = opener.open(rep)
        cookie_handler.save(f, ignore_discard=True, ignore_expires=True)

        html = rsp.read().decode()
        print(html)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    login()