import pymysql

db = pymysql.connect(host="localhost", user='root', password='123456', port=3306, db='django')
cursor = db.cursor()

table = "friends"
age = "age > 30"

sql = 'DELETE FROM {table} WHERE {age}'.format(table=table, age=age)
try:
    cursor.execute(sql)
    print("Successful...")
    db.commit()
except:
    print("Failed...")
    db.rollback()
finally:
    db.close()