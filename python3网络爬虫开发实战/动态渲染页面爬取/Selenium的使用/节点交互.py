import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = "https://www.taobao.com"

browser = webdriver.Chrome()
# 使用驱动浏览器打开淘宝
browser.get(url)

# 获取淘宝搜索的输入框id
input = browser.find_element_by_id('q')
# 在输入框当中输入iPhone
input.send_keys('iPhone')
time.sleep(1)
# 清除输入框内的内容
input.clear()
# 在输入框当中输入iPad
input.send_keys('iPad')
button = browser.find_element_by_class_name('search-button')
# 点击搜索
button.click()
time.sleep(3)
#browser.close()