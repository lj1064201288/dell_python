import pymysql

db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='django')
cursor = db.cursor()

table = "friends"
id = "id = 9"

sql = "DELETE FROM {table} WHERE {id}".format(table=table, id=id)

try:
    cursor.execute(sql)
    print("Successful...")
    db.commit()
except Exception as e:
    print(e)
    print("Failed...")
    db.rollback()
finally:
    db.close()