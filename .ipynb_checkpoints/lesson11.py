import pymysql
import numpy as np
import pandas as pd
import csv

# 链接数据库
db = pymysql.connect(host="cdb-r2g8flnu.bj.tencentcdb.com", port=10209, user
="dase2020", password="dase2020", database="dase_intro_2020")
cursor = db.cursor()  # 使用 cursor() 方法创建一个游标对象 cursor,执行SQL语句都是通过游标对象实现
sql = "SELECT VERSION();"  # 该SQL语句返回MySQL的安装版本，用以确定是否成功连接服务器
cursor.execute(sql)  # 执行SQL语句
result = cursor.fetchone()  # 获取单条数据
# print(result)

with open('bike.csv', 'w',newline='', encoding="UTF-8") as f:
    writer = csv.writer(f)
    sql = "SELECT * FROM  bicycle_train;"
    cursor.execute(sql)
    result = cursor.fetchall()
    for r in result:
        writer.writerow(r)
    bike_data=pd.read_csv('bike.csv',dtype=float, quoting=csv.QUOTE_NONE,encoding="UTF-8")
