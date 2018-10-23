'''
项目目标:
    1. 使用Selenium来模拟浏览器操作,抓取淘宝商品信息,并将结果保存到MongoDB
    2. 利用Selenium抓取淘宝商品并使用pyquery解析得到商品的图片,名称,价格,购买人数,店铺名称和店铺所在地的信息,并将其保存到MongoDB
准备工作:
    1. 确保已将Chrome浏览器配置好了ChromeDriver
    2. 还需要正确安装Python的Selenium库,最后,还对接了PhantomJS和Firefox
'''

import time
from urllib import parse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

content = 'iPad'

user = '2574019428@qq.com'
password = 'liujun19960106'

url = "https://login.tmall.com"
browser.get(url)
browser.switch_to_frame('J_loginIframe')
#browser.find_element_by_id('mq').send_keys(content)
time.sleep(1)
browser.find_element_by_css_selector('.forget-pwd.J_Quick2Static').click()
time.sleep(1)
for u in user:
    browser.find_element_by_id('TPL_username_1').send_keys(u)
    time.sleep(0.1)

for p in password:
    browser.find_element_by_id('TPL_password_1').send_keys(p)
    time.sleep(0.05)
# borwser.find_element_by_css_selector('search-combobox-input-wrap').send_keys('iPad')
#browser.find_element_by_xpath('//fieldset/div/button').click()

#borwser.find_element_by_css_selector('.forget-pwd.J_Quick2Static').click()
# borwser.find_element_by_id("TPL_username_1").send_keys("2574019428@qq.com")
# borwser.find_element_by_id("TPL_password_1").send_keys('lj1064201288')
