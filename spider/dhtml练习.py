from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

if __name__ == '__main__':

    url = "http://www.tmall.com"

    driver = webdriver.Chrome()
    driver.get(url)

    text = driver.find_element_by_id("site-nav").text
    print(text)
    print(driver.title)

    # 得到页面的快照
    driver.save_screenshot("tmall.png")
    driver.quit()
