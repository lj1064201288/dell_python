import string, random, pymysql


forselect = string.ascii_letters + '1234567890'

def generate(count, lenght):
    '''
    :param count: 激活码的个数
    :param lenght: 激活码的长度
    :return: 激活码
    '''

    for i in range(count):
        RE = ''
        for x in range(lenght):
            RE += random.choice(forselect)
        yield RE

def MySQL(code):
    db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='codes')
    cursor = db.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS code (id VARCHAR(255) NOT NULL, content VARCHAR(255) not null, PRIMARY KEY (id))')
    try:
        sql = 'insert into code(content)VALUES ({})'.format(code)
        cursor.execute(sql)
        db.commit()
        print('插入成功')
    except:
        db.rollback()
        print('插入失败')
    else:
        cursor.close()
        db.close()

if __name__ == '__main__':
    code = generate(200,20)
    print(list(code))
    MySQL(code)
