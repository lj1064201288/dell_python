import pymysql

db = pymysql.connect(host='localhost', user='root', password='123456', port=3306)
cursor = db.cursor()

cursor.execute('select version()')
data = cursor.fetchone()
cursor.execute('create database Family default character set utf8')
db.close()