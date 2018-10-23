import pymysql

db = pymysql.connect(host="localhost", user='root', password='123456', port=3306, db='django')
cursor = db.cursor()

data = {
    'id':1,
    'name':'阳志波',
    'age':24,
    'date':"1995-05-26"
}

table = 'friends'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))

sql = "INSERT INTO {table}({keys}) VALUES({values}) ON DUPLICATE KEY UPDATE ".format(table=table, keys=keys, values=values)
updata = ', '.join(["{key}=%s".format(key=key) for key in data])
sql = sql + updata
print(sql)
try:
    cursor.execute(sql, tuple(data.values()) * 2)
    print('Successful...')
    db.commit()
except:
    print("Failed...")
    db.rollback()
finally:
    db.close()
