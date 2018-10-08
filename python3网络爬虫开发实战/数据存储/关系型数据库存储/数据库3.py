import pymysql

id = '20120001'
user = 'Bob'
age = 20

db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
cursor = db.cursor()

# sql = 'INSERT INTO students(id, name, age) values('+ id +', '+ name +', '+ age +')'
# 上面的例子过于繁琐,不直观,所以可以选择直接使用格式符%s来实现,有几个values就写几个%s
sql = 'INSERT INTO students(id, name, age) values(%s, %s, %s)'

try:
    # 只需要使用execte()的第一个参数传入该SQL语句Values值用统一的元组传过来
    cursor.execute(sql, user, age)
    # commit()方法可实现数据插入,这个方法才是真正将语句提交到数据库执行的方法,对于数据插入,更新,删除操作,都需要调动该方法才能生效
    db.commit()
except:
    # 调用rollbadck()方法将数据回滚,相当于什么都没有发生过
    db.rollback()
db.close()
