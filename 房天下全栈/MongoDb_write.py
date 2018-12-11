import pymongo

class Mongo_DB():
    def __init__(self, mongo_db, city, item):
        self.host = 'localhost'
        self.mongo_db = mongo_db
        self.city = city
        self.item = item

    def open_spider(self):
        try:
            self.client = pymongo.MongoClient(self.host)
            self.db = self.client[self.mongo_db]
        except SystemError as s:
            print(s.args)
        except Exception as e:
            print(e.args)

    def process_item(self):
       try:
            self.db[self.city].insert(self.item)
            print(self.item['楼盘名称'],"存储到数据库成功")

       except SystemError as e:
           print(e.args)
           print( "存储到数据库失败", self.item)

       except Exception as e:
           print( self.item,"存储到数据库失败", e.args)

    def run_sql(self):
        self.open_spider()
        self.process_item()
        self.close_spider()

    def close_spider(self):
        self.client.close()
