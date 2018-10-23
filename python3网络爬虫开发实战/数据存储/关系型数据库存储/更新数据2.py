import pymysql

db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
cursor = db.cursor()

data = {
    'id':'20181014',
    'name':'LIUJUN',
    'age':22
}

table = 'students'
keys = ','.join(data.keys())
values = ','.join(['%s'] * len(data))

sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys, values=values)
updata = ','.join([" {key} = %s".format(key=key) for key in data])
sql += updata

try:
    if cursor.execute(sql, tuple(data.values()) * 2):
        print('Successful')
        db.commit()
except:
    print('Failed')
    db.rollback()
db.close()

