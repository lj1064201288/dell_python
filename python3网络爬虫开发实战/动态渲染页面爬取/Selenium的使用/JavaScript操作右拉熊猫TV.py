from selenium import webdriver

browser = webdriver.Chrome()

url = "https://pandatv.com"
browser.get(url)

browser.execute_script('window.scrollTo(0, document.body.scrollLife)')
