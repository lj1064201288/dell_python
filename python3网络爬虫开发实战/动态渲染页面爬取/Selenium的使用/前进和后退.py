import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://www.baidu.com")
browser.get("https://www.taobao.com")
browser.get("https://www.zhihu.com/explore")

browser.back()
time.sleep(2)
browser.forward()
time.sleep(3)
browser.close()