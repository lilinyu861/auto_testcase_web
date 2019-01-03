import pymysql
db = pymysql.connect(user='root', password='root', db='testdjango')
cursor = db.cursor()
cursor.execute("select * from table")
result = cursor.fetchall()
cursor.close()
db.close()



