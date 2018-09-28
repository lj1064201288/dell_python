from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def login(url):

    driver = webdriver.Chrome()

    driver.get(url)

    time.sleep(3)
    driver.save_screenshot("豆瓣登录页面.png")

   

    driver.find_element_by_id('email').send_keys('13550211725')
    driver.find_element_by_id('password').send_keys('liujun19960106')
    s = driver.find_element_by_name("captcha-solution")
    if s:
        captcha = input("please input code:")
        driver.find_element_by_name('captcha-solution').send_keys(captcha)

    driver.find_element_by_name('login').click()

    driver.save_screenshot("豆瓣login.png")

    filename = "豆瓣.html"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(driver.page_source)

    driver.quit()
    
if __name__ == '__main__':

    url = "https://www.douban.com/accounts/login?source=movie"

    login(url)