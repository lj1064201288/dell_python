from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://www.zhihu.com/explore")
print(browser.get_cookies())
print("***" * 50)
browser.add_cookie({'name':'name', 'domain':'www.zhihu.com', 'value':'germey'})
print(browser.get_cookies())
print("***" * 50)
browser.delete_all_cookies()
print(browser.get_cookies())
