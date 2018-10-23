import pymysql

db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='django')
cursor = db.cursor()

names = ['贺海川', '唐凯', '刘琼英', '刘连芳', '刘俊']
ages = ['23', '23', '45', '43', '18']
dates = ['1995-09-28', '1995-06-26', '1973-09-28', '1976-05-24', '1996-02-24']

for i in range(len(names)):
    data = {}

    data['name'] = names[i]
    data['age'] = ages[i]
    data['date'] = dates[i]

    table = 'friends'
    keys = ', '.join(data.keys())
    values = ', '.join(['%s'] * len(data))
    sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
    try:
        cursor.execute(sql, tuple(data.values()))
        print('Successful')
        db.commit()
    except Exception as e:
        print(e)
        print("Failed")
        db.rollback()

db.close()
