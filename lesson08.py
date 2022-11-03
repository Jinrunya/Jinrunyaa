import pymysql
import numpy as np

# 链接数据库
db = pymysql.connect(host="cdb-r2g8flnu.bj.tencentcdb.com", port=10209, user
="dase2020", password="dase2020", database="dase_intro_2020")
cursor = db.cursor()  # 使用 cursor() 方法创建一个游标对象 cursor,执行SQL语句都是通过游标对象实现
sql = "SELECT VERSION();"  # 该SQL语句返回MySQL的安装版本，用以确定是否成功连接服务器
cursor.execute(sql)  # 执行SQL语句
result = cursor.fetchone()  # 获取单条数据
# print(result)
# 实验开始.ver
# task 01
sql = "SELECT * FROM  bicycle_train LIMIT 17,5 ;"
cursor.execute(sql)
result = cursor.fetchall()
print(result)


# task 02
sql = "SELECT MIN(wind) FROM bicycle_train;"
cursor.execute(sql)
result = cursor.fetchall()
print("Min:", end=" ")
print("%d" % (result[0][0]))
sql = "SELECT MAX(wind) FROM bicycle_train;"
cursor.execute(sql)
result2 = cursor.fetchall()
print("Max:", end=" ")
print("%d" % (result2[0][0]))

# task 03
sql = "SELECT AVG(temp_air) FROM bicycle_train WHERE city=0 AND hour=10 AND weather=1 AND wind BETWEEN 0 AND 1 AND y>=100"
cursor.execute(sql)
result3 = cursor.fetchall()
print("%f" % (result3[0][0]))


# task 04
sql = "SELECT temp_air FROM bicycle_train WHERE city=0 AND hour=10 AND weather=1 AND wind BETWEEN 0 AND 1 AND y>=100"
cursor.execute(sql)
result4 = cursor.fetchall()
a = np.var(result4)
print("%f" % a)

# task 05
sql = "SELECT SUM(y) from bicycle_train WHERE is_workday=1 AND city=1 AND weather=3"
cursor.execute(sql)
result5 = cursor.fetchall()
print("上海的雨雪天使用总量：%d" % result5[0][0])
sql = "SELECT SUM(y) from bicycle_train WHERE is_workday=1 AND city=0 AND weather=3"
cursor.execute(sql)
result6 = cursor.fetchall()
print("北京的雨雪天使用总量：%d" % result6[0][0])

# task 06
sql = "SELECT  hour,AVG(y) from bicycle_train WHERE city=1 AND temp_body<=10 AND is_workday=1 AND hour BETWEEN 17 AND 19 GROUP BY hour ORDER BY AVG(y)"
cursor.execute(sql)
result7 = cursor.fetchall()
for record in result7:
    print("时间：%d 均值：%d" % (record[0], round(record[1])))
