from selenium import webdriver
from bs4 import BeautifulSoup
import time
import json

class Douyu():

    def douyu(self):
        self.driver = webdriver.Chrome()
        self.url = "https://www.douyu.com/directory/all"
        self.num = 0

    def get_url(self):
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.save_screenshot("douyu.png")
        self.html = self.driver.page_source
        with open('斗鱼.html', 'w', encoding='utf-8') as f:
            f.write(self.html)

    def etree_douyu(self):
        soup = BeautifulSoup(self.html, 'xml')
        names = soup.find_all('span', {'class':'dy-name ellipsis fl'})
        titles = soup.find_all('h3', {'class':'ellipsis'})
        nums = soup.find_all('span', {'class':'dy-num fr'})
        attrs = soup.find_all('span', {'class':'tag-ellipsis'})

        for title, name, num in zip(titles, names, nums):
            t = title.get_text().strip()
            n = name.get_text().strip()
            m = num.get_text().strip()
            # a = attr.get_text().strip()
            print("房间:{0} 主播:{1} 观看人数:{2}".format(t,n,m))
            self.num += 1


    def close(self):
        self.driver.quit()


if __name__ == '__main__':

    douyu = Douyu()
    douyu.douyu()
    douyu.get_url()
    douyu.etree_douyu()
    douyu.close()
    print(douyu.num)

