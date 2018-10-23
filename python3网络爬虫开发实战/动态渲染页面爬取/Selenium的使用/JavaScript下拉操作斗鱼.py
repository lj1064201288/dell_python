from selenium import webdriver

browser = webdriver.Chrome()

url = "https://www.douyu.com"

browser.get(url)
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')