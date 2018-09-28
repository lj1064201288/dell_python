'''
爬取斗鱼第一页的主播信息,需要主播名称,观看人数,房间名称,直播类型
'''

from selenium import webdriver
from bs4 import BeautifulSoup
import json
import time


class Douyu():

    def douyu(self):
        self.driver = webdriver.Chrome()
        self.url = "https://www.douyu.com/directory/all"

    def file_save(self):
        self.driver.get(self.url)

        time.sleep(3)
        self.driver.save_screenshot("斗鱼.png")
        self.file = "斗鱼.html"

        with open(self.file, 'w', encoding='utf-8') as f:
            f.write(self.driver.page_source)

    def employ(self):

        with open(self.file, 'r', encoding='utf-8') as r:
            html = r.read()

        soup = BeautifulSoup(html, 'xml')

        self.rooms = soup.find_all('h3', {'class':'ellipsis'})
        self.attrs = soup.find_all('span', {'class':'tag ellipsis'})
        self.names = soup.find_all('span', {'class':'dy-name ellipsis fl'})
        self.nums = soup.find_all('span', {'class': 'dy-num fr'})

    def Data(self):

        datas = []

        for i in range(len(self.nums)):
            data_dict = {}
            if len(self.rooms[i]):
                data_dict['房间名称:'] = self.rooms[i].get_text().strip()
            if len(self.attrs[i]):
                data_dict['直播类型:'] = self.attrs[i].get_text().strip()
            if len(self.names[i]):
                data_dict['主播名称:'] = self.names[i].get_text().strip()
            if len(self.nums[i]):
                data_dict['观看人数:'] = self.nums[i].get_text().strip()

            datas.append(data_dict)

        print(len(datas))

        filename = "斗鱼.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(datas, f, indent=5)


    def Quit(self):
        self.driver.quit()

if __name__ == '__main__':

    douyu = Douyu()

    douyu.douyu()
    douyu.file_save()
    douyu.employ()
    douyu.Data()
    douyu.Quit()


