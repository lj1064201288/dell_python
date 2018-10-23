from selenium import webdriver

url = "https://www.youku.com"

browser = webdriver.Chrome()
browser.get(url)

browser.execute_script("window.scrollTo(1000, document.body.scrollHeight)")
