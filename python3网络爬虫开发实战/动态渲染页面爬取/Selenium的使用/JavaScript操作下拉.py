from selenium import webdriver


url = "https://www.taobao.com"

browser = webdriver.Chrome()
browser.get(url)

browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

