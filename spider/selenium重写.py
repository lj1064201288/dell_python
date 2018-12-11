from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

if __name__ == '__main__':

    driver = webdriver.Chrome()

    driver.get("https://music.163.com/#/discover/toplist?id=3779629")

    print("Title: {0}".format(driver.title))