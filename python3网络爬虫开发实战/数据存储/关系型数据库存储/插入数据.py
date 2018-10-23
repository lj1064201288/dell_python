import pymysql

id = "20181015"
user = '刘俊'
age = '18'

db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
cursor = db.cursor()

sql = 'INSERT INTO students(id, name,age) VALUES (%s, %s, %s)'
try:
    cursor.execute(sql, (id, user, age))
    db.commit()
except:
    db.rollback()
db.close()