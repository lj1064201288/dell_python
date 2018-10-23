from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://taobao.com")
input_first = browser.find_element_by_id('q')
input_second = browser.find_element_by_css_selector("#q")
input_third = browser.find_element_by_xpath('//*[@id="q"]')
print(input_first,"\n", input_second,"\n", input_third)
browser.close()