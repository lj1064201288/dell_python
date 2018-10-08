import re
import json
import scrapy
from bs4 import BeautifulSoup
from item_baidu.items import ItemBaidu

class BaiduSpider(scrapy.Spider):
    # 项目名称
    name = 'baiduhr'

    # 只允许在此域名中爬取
    allowed_domains = ["talent.baidu.com"]

    # 起始页面
    start_urls = ['https://talent.baidu.com/baidu/web/httpservice/getPostList?recruitType=2&pageSize=10&curPage=1']



    def parse(self, response):

        # 使用BeautifulSoup获取源码
        soup = BeautifulSoup(response.text)
        # 使用re对需要的数据进行清洗
        contents = re.sub(r'<p>|</p>|<br/>', '', str(soup.p))
        # 获得需要的内容
        contents = json.loads(contents)["postList"]
        for content in contents:

            # 导入Item
            item = ItemBaidu()

            # 每个岗位都有自己的ID,name所以不需要判断
            item["postId"] = content["postId"]
            item["name"] = content["name"]
            # 判断该岗位是否有这些要求
            if "publishDate" in content.keys():
                item["publishDate"] = content["publishDate"]
            else:
                pass

            if "postType" in content.keys():
                item["postType"] = content["postType"]
            else:
                pass

            if 'workPlace' in content.keys():
                item["workPlace"] = content["workPlace"]
            else:
                pass

            if "workYears" in content.keys():
                item["workYears"] = content["workYears"]
            else:
                pass

            if "recruitNum" in content.keys():
                item["recruitNum"] = content["recruitNum"]
            else:
                pass

            if "education" in content.keys():
                item["education"] = content["education"]
            else:
                pass

            # 由于工作职责与内容里面有一些不需要的字符，这里使用re进行清除
            item["serviceCondition"] = re.sub(r"\r", " ", content["serviceCondition"])
            item["workContent"] = re.sub(r"\r", " ", content["workContent"])

            # 使用re找到页面的页数,然后进行更改
            curpage = re.search('curPage=(\d+)', response.url).group(1)
            page = int(curpage) + 1
            print(page)

            # 由于是Ajax数据,如果一直添加,会无限循环,所以设置最大页面为150页
            if page < 150:
                url = re.sub("curPage=(\d+)", "curPage=" + str(page), response.url)
                # 返回新的页面给self.parse重新执行上面的操作
                yield scrapy.Request(url, callback=self.parse)
            else:
                pass

            yield item





