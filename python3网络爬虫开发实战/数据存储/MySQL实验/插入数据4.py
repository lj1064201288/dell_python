import pymysql

db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='django')
cursor = db.cursor()

data = {
    'name':"袁素珍",
    'age':68,
    'date':'1950-07-02'
}

table = 'friends'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))

sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table,keys=keys, values=values)

try:
    cursor.execute(sql, tuple(data.values()))
    print("Successful........")
    db.commit()
except:
    print("Failed....")
    db.rollback()
finally:
    db.close()