from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

if __name__ == '__main__':

    driver = webdriver.PhantomJS()

    driver.get("http://www.baidu.com")

    print("Title: {0}".format(driver.title))