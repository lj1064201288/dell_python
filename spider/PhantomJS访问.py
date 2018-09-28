from selenium import webdriver
import time

if __name__ == '__main__':

    driver = webdriver.PhantomJS()
    url = "http://www.baidu.com"

    driver.get(url)

    print(driver.title)