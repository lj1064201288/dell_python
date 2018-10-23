from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException

browser = webdriver.Chrome()
try:
    browser.get("https://www.baidu.com")
except TimeoutException:
    print("Time out")
try:
    browser.find_element_by_id("hello")
except NoSuchElementException:
    print("No Element")
finally:
    browser.close()
