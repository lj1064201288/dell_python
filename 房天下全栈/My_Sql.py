import pymysql

class MySQL():

    def __init__(self,database, table, items):
        self.host = 'localhost'
        self.port = 3306
        self.user = 'root'
        self.password = '123456'
        self.database = database
        self.table = table
        self.items = items

    def create_db(self):
        self.db = pymysql.connect(host=self.host, user=self.user, password=self.password, port=self.port)
        self.cursor = self.db.cursor()
        self.cursor.execute("CREATE DATABASE {0} DEFAULT CHARACTER SET utf8".format(self.database))


    def create_table(self):
        self.cursor.execute('CREATE TABLE {0} (id VARCHAR(255) PRIMARY KEY, )')


