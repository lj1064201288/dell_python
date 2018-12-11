import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
url = "https://auth.geetest.com/login/"

browser.get(url)

wait = WebDriverWait(browser, 20)
email = "1064201288@qq.com"
password = "liujun19960106"

# 输入账户名和密码
user = browser.find_element_by_xpath('//input[@type="email"]')
user.send_keys(email)
Password = browser.find_element_by_xpath('//input[@type="password"]')
Password.send_keys(password)

# 点击验证码
button = browser.find_element_by_class_name('geetest_radar_tip')
button.click()

# 获取图片的位置
time.sleep(3)
img = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_canvas_img')))
location = img.location
print(location)
size = img.size
print(size)
top, bottom, lift, right = location['y'], location['y']+size['height'],
