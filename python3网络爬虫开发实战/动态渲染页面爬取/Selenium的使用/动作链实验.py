from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()
url = "https://www.taobao.com"
browser.get(url)
source = browser.find_element_by_css_selector('#a21bo.2017.201859.1')
target = browser.find_element_by_css_selector('#q')
actions = ActionChains(browser)
actions.drag_and_drop(source, target)
actions.perform()