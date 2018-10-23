import pymysql

db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='django')
cursor = db.cursor()

data = {
    'id':2,
    'name':"黄志强",
    'age':23,
    'date':"1995-04-02"
}

table = 'friends'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))

sql = "INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE ".format(table=table, keys=keys, values=values)
update = ', '.join(["{key} = %s".format(key=key) for key in data])
sql = sql+update
print(sql)
try:
    if cursor.execute(sql, tuple(data.values())*2):
        print('Successful')
        db.commit()
except Exception as e:
    print(e)
    print("Failed")
    db.rollback()
db.close()