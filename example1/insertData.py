import pymysql.cursors
from xlrd import open_workbook
import sys

# 连接数据库
db = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='datamining',
    charset='utf8'
)

cursor = db.cursor()
# 使用execute方法执行SQL语句
# 建立数据库中的Stu表
# cursor.execute("create table Stu(ID int,Name char(20),City char(20), Gender char(20), Height float, C1 float, C2 float, C3 float, C4 float, C5 float, C6 float, C7 float, C8 float, C9 float, C10 float, Constitution char(20))character set utf8;")
cursor.execute("create table Stu(ID char(20),Name char(20),City char(20), Gender char(20), Height char(20), C1 char(20), C2 char(20), C3 char(20), C4 char(20), C5 char(20), C6 char(20), C7 char(20), C8 char(20), C9 char(20), C10 char(20), Constitution char(20))character set utf8;")

# 把Excel中的数据插入数据库中
sql = 'INSERT INTO STU(ID, Name, City, Gender, Height, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10,Constitution) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

# 打开Excel文件
book = open_workbook('data1.xlsx')
# 获取第一个表
sheet = book.sheets()[0]
# 获取行数
Rows = sheet.nrows
for r in range(1, Rows):
    ID = sheet.cell(r, 0).value
    Name = sheet.cell(r, 1).value
    City = sheet.cell(r, 2).value
    Gender = sheet.cell(r, 3).value
    Height = sheet.cell(r, 4).value
    C1 = sheet.cell(r, 5).value
    C2 = sheet.cell(r, 6).value
    C3 = sheet.cell(r, 7).value
    C4 = sheet.cell(r, 8).value
    C5 = sheet.cell(r, 9).value
    C6 = sheet.cell(r, 10).value
    C7 = sheet.cell(r, 11).value
    C8 = sheet.cell(r, 12).value
    C9 = sheet.cell(r, 13).value
    C10 = sheet.cell(r, 14).value
    Constitution = sheet.cell(r, 15).value

    VALUES = (ID, Name, City, Gender, Height, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10,Constitution)
    cursor.execute(sql, VALUES)
    db.commit()

# 关闭数据库连接
db.close()