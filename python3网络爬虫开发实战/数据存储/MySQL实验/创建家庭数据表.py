import pymysql

db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='Family')
cursor = db.cursor()

sql = "create table if not exists family (id int unsigned auto_increment, name varchar(255) not null, age INT not null, brithday VARCHAR(255) not null,submission_date DATE, primary key(id) )"

try:
    cursor.execute(sql)
    db.commit()
except Exception as e:
    db.rollback()
    print(e)
finally:
    db.close()