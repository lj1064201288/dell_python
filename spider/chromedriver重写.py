from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

if __name__ == '__main__':

    url = "http://www.baidu.com"

    driver = webdriver.Chrome()

    driver.get(url)

    time.sleep(3)
    text = driver.find_element_by_id('wrapper').text
    print(text)
    text = driver.find_element_by_id('lg').text
    print(text)
