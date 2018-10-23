import pymysql

db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='django')
cursor = db.cursor()

sql = "CREATE TABLE IF NOT EXISTS friends (id INT UNSIGNED AUTO_INCREMENT, name VARCHAR(255) NOT NULL, age INT NOT NULL, date VARCHAR(255), PRIMARY KEY (id))"

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()