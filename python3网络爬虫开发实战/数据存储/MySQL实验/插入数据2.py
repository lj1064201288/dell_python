import pymysql

db = pymysql.connect(host="localhost", user='root', password='123456', port=3306, db='django')
cursor = db.cursor()

data = {
    'name':'黄志强',
    'age': 23,
    'date': '19950402'
}

table = 'friends'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))

sql = 'INSERT INTO {table}({keys}) VALUES({values})'.format(table=table, keys=keys, values=values)

try:
    cursor.execute(sql, tuple(data.values()))
    print("Successful")
    db.commit()
except:
    print('Failed')
    db.rollback()
finally:
    db.close()