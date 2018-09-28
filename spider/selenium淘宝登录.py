from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

if __name__ == '__main__':

    url = "https://login.tmall.com/?spm=875.7931836/B.a2226mz.1.66144265sShRhv&redirectURL=https%3A%2F%2Fwww.tmall.com%2F"
    driver = webdriver.Chrome()
    driver.get(url)

    driver.save_screenshot('天猫.png')

    time.sleep(5)

    with open("tmall.html", 'w', encoding='utf-8') as f:
        f.write(driver.page_source)


    driver.save_screenshot('天猫2.png')
    driver.find_element_by_id('TPL_username_1').send_keys('2574019428@qq.com')
    driver.find_element_by_id('password-label').send_keys('lj1064201288')
    #driver.find_element_by_class_name('forget-pwd J_Quick2Static').click()
    time.sleep(3)
    driver.save_screenshot('天猫3.png')

    driver.quit()