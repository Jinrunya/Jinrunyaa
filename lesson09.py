import csv
import pymysql
import pandas as pd  # pandas是一个强大的分析结构化数据的工具集

##task 01##

db = pymysql.connect(host="cdb-r2g8flnu.bj.tencentcdb.com", port=10209, user
="dase2020", password="dase2020", database="dase_intro_2020")
cursor = db.cursor()  # 使用 cursor() 方法创建一个游标对象 cursor,执行SQL语句都是通过游标对象实现
sql = "SELECT VERSION();"  # 该SQL语句返回MySQL的安装版本，用以确定是否成功连接服务器
cursor.execute(sql)  # 执行SQL语句
result = cursor.fetchone()  # 获取单条数据
# print(result)
with open('SH_Grade.csv', 'w',newline='', encoding="UTF-8") as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'Stuid', 'Sex', 'CHI611', 'MATH611', 'ENG611',
                     'CHI612', 'MATH612', 'ENG612',
                     'CHI621', 'MATH621', 'ENG621',
                     'CHI622', 'MATH622', 'ENG622',
                     'CHI711', 'MATH711', 'ENG711',
                     'CHI712', 'MATH712', 'ENG712',
                     'CHI721', 'MATH721', 'ENG721',
                     'CHI722', 'MATH722', 'ENG722',
                     'CHI811', 'MATH811', 'ENG811', 'PHY811',
                     'CHI812', 'MATH812', 'ENG812', 'PHY812',
                     'CHI821', 'MATH821', 'ENG821', 'PHY821',
                     'CHI822', 'MATH822', 'ENG822', 'PHY822',
                     'CHI911', 'MATH911', 'ENG911', 'PHY911', 'CHE911',
                     'CHI912', 'MATH912', 'ENG912', 'PHY912', 'CHE912',
                     'CHI921', 'MATH921', 'ENG921', 'PHY921', 'CHE921'])
    sql = "SELECT * FROM SH_Grade"
    cursor.execute(sql)
    result = cursor.fetchall()
    for r in result:
        writer.writerow(r)
    student_data = pd.read_csv('SH_Grade.csv',dtype=str, quoting=csv.QUOTE_NONE,encoding="UTF-8")
    n = student_data['Stuid'].apply( lambda x:x[0])
    student_data['Class'] = n
    pd.set_option('display.max_rows', None)  # 展示所有行
    print(student_data)
    print(student_data.columns)
    order = ['id','Class', 'Stuid', 'Sex', 'CHI611', 'MATH611', 'ENG611', 'CHI612',
       'MATH612', 'ENG612', 'CHI621', 'MATH621', 'ENG621', 'CHI622', 'MATH622',
       'ENG622', 'CHI711', 'MATH711', 'ENG711', 'CHI712', 'MATH712', 'ENG712',
       'CHI721', 'MATH721', 'ENG721', 'CHI722', 'MATH722', 'ENG722', 'CHI811',
       'MATH811', 'ENG811', 'PHY811', 'CHI812', 'MATH812', 'ENG812', 'PHY812',
       'CHI821', 'MATH821', 'ENG821', 'PHY821', 'CHI822', 'MATH822', 'ENG822',
       'PHY822', 'CHI911', 'MATH911', 'ENG911', 'PHY911', 'CHE911', 'CHI912',
       'MATH912', 'ENG912', 'PHY912', 'CHE912', 'CHI921', 'MATH921', 'ENG921',
       'PHY921', 'CHE921']
    student_data = student_data[order]
    print(student_data)
    ##task 02##

    student_data1 = student_data.drop_duplicates(subset=['id'])
    print(student_data1)
