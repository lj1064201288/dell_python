import pymysql

# 通过connect()方法声明一个MySQL连接对象db,此时需要传入MySQL运行的host(即IP)
# 由于MySQL在本地运行,所以传入的是localhost,如果MySQL在远程运行,则传入其公网IP地址
db = pymysql.connect(host='localhost', user='root', password='123456', port=3306)
# 连接成功后,需要在调用cursor()方法获得MySQL的操作游标,利用游标来执行SQL语句
cursor = db.cursor()
# 这里执行了两句SQL,直接用execute()方法执行,获取MySQL的当前版本
cursor.execute('SELECT VERSION()')
# 调用fetchine()方法获得第一条数据
data = cursor.fetchone()
print('Database version:', data)
# 创建数据库的操作,数据库名叫spiders,编码默认为UTF-8
cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")
db.close()