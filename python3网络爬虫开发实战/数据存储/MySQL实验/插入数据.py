import pymysql

db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='django')
cursor = db.cursor()

data = {
    'id': 1,
    'name':'阳志波',
    'age':24,
    'date':"1995-5-26"
}

table = 'friends'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))

sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)

try:
    cursor.execute(sql, tuple(data.values()))
    db.commit()
    print('Succeeful')
except Exception as e:
    print(e)
    db.rollback()
    print('Failed')
finally:
    db.close()
