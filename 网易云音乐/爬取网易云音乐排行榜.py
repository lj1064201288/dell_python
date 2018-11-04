'''
爬取网易云音乐新歌榜
'''

import os
import csv
import time
import requests
from lxml import etree
from selenium import webdriver



class WangyiMusc(object):

    # id表示你要获取排行榜
    def __init__(self, id, mating):
        self.browser = webdriver.Chrome()
        self.id = id
        self.url = "https://music.163.com/#/discover/toplist?id={0}".format(self.id)
        self.music_url = "http://music.163.com/song/media/outer/url?id={0}.mp3"
        self.mat = mating

    def get_html(self):
        self.browser.get(self.url)
        self.browser.switch_to_frame('contentFrame')
        iframe = self.browser.page_source
        time.sleep(5)
        return iframe

    def parse_html(self):
        iframe = self.get_html()
        html = etree.HTML(iframe)
        contents = html.xpath('//tbody/tr')

        try:
            for content in contents:

                title = content.xpath('./td/div/div/div/span/a/b/@title')[0].strip()
                music_id = content.xpath('./td/div/div/span/@data-res-id')[0].strip()
                self.write_music(title, music_id)
                num = content.xpath('./td/div/span[@class="num"]/text()')[0].strip()
                time = content.xpath('./td[@class=" s-fc3"]/span/text()')[0].strip()
                singer = content.xpath('./td/div[@class="text"]/@title')[0].strip()
                items = num, title, time, singer

                yield  list(items)

        except Exception as e:
            print('解析失败！',e.args)

    def get_time(self):
        t = time.localtime()
        tt = time.strftime('%Y年%m月%d日', t)
        return tt

    def write_music(self, title, music_id):
        url = self.music_url.format(music_id)
        try:
            headers = {
                'User-Agent':'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/70.0.3538.77Safari/537.36',
            }
            music = requests.get(url, headers=headers)

            if music.status_code == 200:
                path = self.get_time() + os.sep + self.mat + os.sep
                if not os.path.exists(path):
                    os.makedirs(path)
                with open(path+title+'.mp3', 'ab') as f:
                    f.write(music.content)
                    print('下载' + title + "成功...")

        except Exception as e:
            print("下载{0}失败!!!".format(title), e.args)

    def write_items(self):
        path = self.get_time() + os.sep + self.mat + "榜单信息"
        try:
            if not os.path.exists(path):
                os.makedirs(path)
            with open(path+'.csv', 'w', encoding='utf-8') as file:
                csvfile = csv.writer(file)
                csvfile.writerow(['排名', '歌名', '时长', '歌手'])
                for parse in self.parse_html():
                    csvfile.writerow(parse)
                print("存储信息成功.")
        except Exception as e:
            print("存储信息失败!", e.args)

def operation(id, mating):

    try:
        music = WangyiMusc(id, mating)
        music.get_html()
        music.parse_html()
        music.get_time()
        music.write_items()
        print("下载完成...")
        music.browser.close()
    except Exception as e:
        print("下载失败!", e.args)

def user_select():
    ids = ['19723756', '3779629', '2884035', '3778678', '991319590',
           '2408901803', '1978921795', '71385702', '2462790889',
           '10520166', '3812895', '60131', '71384707', '180106', '60198',
           '27135204', '11641012', '120001', '2323534945', '745956260',
           '2023401535', '2006508653', '21845217', '112463',
           '112504', '64016', '10169002', '1899724']

    names = ['云音乐飙升榜', '云音乐新歌榜', '网易原创歌曲榜',
             '云音乐热歌榜', '江小白YOLO云音乐说唱榜', '公告牌音乐榜', '云音乐电音榜',
             '云音乐电音榜', '云音乐ACG音乐榜', 'YY音乐榜', '云音乐国电榜', '云音乐国电榜',
             '云音乐国电榜', '云音乐古典音乐榜', 'UK排行榜周榜', '美国Billboard周榜',
             '法国 NRJVos Hits 周榜', 'iTunes榜', 'Hit FMTop榜', '说唱TOP榜', '云音乐韩语榜',
             '英国Q杂志中文版周榜', '电竞音乐榜', 'KTV唛榜', '台湾Hito排行榜', '中国TOP排行榜（港台榜）',
             '中国TOP排行榜（内地榜）', '香港r台中文歌曲龙虎榜', '中国嘻哈榜']
    musics = {}
    nums = {}

    for mat in range(len(ids)):
        musics[names[mat]] = ids[mat]

    for num in range(1, len(names) + 1):
        nums[num] = names[num - 1]

    for k, v in nums.items():
        print(k, ":", v)

    n = input('请输入你要下载的榜单(请输入数字):')
    if str(n) not in nums.keys():
        print("输入有误，请重新输入")
    mating = nums[int(n)]
    id = musics[mating]
    operation(id, mating)


if __name__ == '__main__':
   user_select()



