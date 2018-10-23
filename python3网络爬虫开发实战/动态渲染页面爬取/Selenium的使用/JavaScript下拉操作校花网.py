import time
from selenium import webdriver

browser = webdriver.Chrome()

url = "http://www.xiaohuar.com/2014.html"

browser.get(url)

browser.execute_script("window.scrollTo(30, document.body.scrollHeight)")
time.sleep(3)
browser.execute_script('window.scrollTo(300, document.body.scrollLife)')
time.sleep(3)