import pymysql

db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='django')
cursor = db.cursor()

sql = 'SELECT * FROM friends WHERE age >= 20'

try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)
    one = cursor.fetchone()
    print("One:", one)
    results = cursor.fetchall()
    print("Results:", results)
    print("Results Type:", type(results))
    for result in results:
        print(result)

except:
    print('Error')