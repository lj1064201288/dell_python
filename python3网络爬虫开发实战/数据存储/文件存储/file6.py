import csv

with open('data.csv', 'w') as csvfile:
    # 调用csv库的writer()方法初始化写入对象
    writer = csv.writer(csvfile)
    # 调用writerow()方法传入每行的数据即可完成写入
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['10001', 'Mike', 20])
    writer.writerow(['10002', 'Bob', 22])
    writer.writerow(['10003', 'Jordan', 21])