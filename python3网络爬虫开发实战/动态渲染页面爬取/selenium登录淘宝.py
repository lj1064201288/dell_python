import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = "https://login.taobao.com/member/login.jhtml?from=taobaoindex&f=top&style=&sub=true&redirect_url=https%3A%2F%2Fi.taobao.com%2Fmy_taobao.htm%3Fspm%3Da21bo.2017.754894437.3.5af911d9n0Zqob%26ad_id%3D%26am_id%3D%26cm_id%3D%26pm_id%3D1501036000a02c5c3739"

driver = webdriver.Chrome()
driver.get(url)
time.sleep(2)

driver.save_screenshot('淘宝.png')
with open("淘宝.html", 'w') as f:
    f.write(driver.page_source)

name = driver.find_element_by_id("TPL_username_1").send_keys("2574019428@qq.com")
password = driver.find_element_by_id("TPL_password_1")
password.send_keys("lj1064201288")
password.send_keys(Keys.ENTER)

driver.save_screenshot('淘宝1.png')
time.sleep(2)