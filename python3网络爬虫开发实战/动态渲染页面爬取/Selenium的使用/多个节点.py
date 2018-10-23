from selenium import webdriver

url = "https://www.taobao.com"

browser = webdriver.Chrome()
browser.get(url)

lis = browser.find_elements_by_css_selector('.service-bd li')
print(lis)
browser.close()
