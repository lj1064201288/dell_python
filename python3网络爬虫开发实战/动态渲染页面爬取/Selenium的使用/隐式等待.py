from selenium import webdriver

browser = webdriver.Chrome()
# 使用implicitly_wait()方法实现隐式等待
browser.implicitly_wait(10)
browser.get('https://www.zhihu.com/explore')
input = browser.find_element_by_class_name('zu-top-add-question')
print(input)