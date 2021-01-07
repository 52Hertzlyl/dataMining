import operator
import math
import numpy as np
import pymysql.cursors
import sys
import csv


# 获取数据库中的数据
def getDbData():
    """

    :return: 返回从数据库中获取的结果
    """
    db = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='123456',
        db='datamining',
        charset='utf8'
    )

    # 获取游标
    cursor = db.cursor()

    # 执行SQL
    sql = 'select *from stu'
    cursor.execute(sql)

    # 从游标中取出所有记录放到一个序列中并关闭游标
    res = cursor.fetchall()

    # 结果为二维元组，需要转换为二维列表
    dbData = list(list(items) for items in list(res))

    cursor.close()
    db.close()
    return dbData


# 获取txt文件里面的数据
def getTxtData():
    """

    :return: 返回从txt文件里面获取的结果
    """
    file1 = open("data2.txt", "r")
    next(file1)
    list_row = file1.readlines()
    txtData = []
    for i in range(len(list_row)):
        column_list = list_row[i].strip().split(",")  # 每一行split后是一个列表
        txtData.append(column_list)  # 在末尾追加到txtData
    file1.close()
    return txtData

# 把female和male改为boy和girl
def changeSex(data):
    """

    :param data: 整个数据
    :return: 把female和male改为boy和girl后的数据
    """
    for i in range(len(data)):
        if data[i][3] == 'male':
            data[i][3] = 'boy'
        if data[i][3] == 'female':
            data[i][3] = 'girl'
    return data

# 把身高改为cm做单位
def changeHeight(data):
    """

    :param data: 整个数据
    :return: 把身高改为cm做单位后的数据
    """
    for i in range(len(data)):
        data[i][4] = str(round(float(data[i][4]) * 100))
    return data

# 数据处理
def Process(data):
    """

    :param data: 整个数据
    :return: 处理完毕的数据
    """
    # 先算出平均身高以及课程的平均成绩，用来填补空缺

    avg = []

    # 算出男女的平均身高
    bogAvg = 0
    bogCount = 0
    girlAvg = 0
    girlCount = 0
    for i in range(len(data)):
        if data[i][4] == '':
            continue
        if data[i][3] == 'boy':
            bogAvg += float(data[i][4])
            bogCount += 1
        if data[i][3] == 'girl':
            girlAvg += float(data[i][4])
            girlCount += 1
    bogAvg = round(bogAvg / bogCount)
    girlAvg = round(girlAvg / girlCount)
    avg.append(bogAvg)
    avg.append(girlAvg)

    # 算出平均成绩
    for i in range(10):
        tmp = 0
        for j in range(len(data)):
            if data[j][i+5] == '':
                continue
            tmp += float(data[j][i+5])
        tmp = round(tmp / len(data))
        avg.append(tmp)
    avg = [str(i) for i in avg]
    # print(avg)

    # 填补身高和成绩的空缺
    for i in range(11):
        for j in range(len(data)):
            if data[j][i + 4] == '':
                if i == 0:
                    if data[j][i+3] == 'boy':
                        data[j][i + 4] = avg[i]
                    if data[j][i + 3] == 'girl':
                        data[j][i + 4] = avg[i+1]
                else:
                    data[j][i + 4] = avg[i+1]

    # 算出Constitution平均值（采用众数）
    boyCons = []
    girlCons = []
    for i in range(len(data)):
        if data[i][15] == '':
            continue
        if data[i][3] == 'boy':
            boyCons.append(data[i][15])
        if data[i][3] == 'girl':
            girlCons.append(data[i][15])
    index, max_type = max(enumerate(boyCons), key=operator.itemgetter(1))
    boyCon = max_type
    index, max_type = max(enumerate(girlCons), key=operator.itemgetter(1))
    girlCon = max_type
    # print(boyCon,girlCon)

    # 填补Constitution空缺
    for i in range(len(data)):
        if data[i][15] == '':
            if data[i][3] == 'boy':
                data[i][15] = boyCon
            if data[i][3] == 'girl':
                data[i][15] = girlCon
    return data

# 数据对比以及合并
def merge(db,txt):

    """

    :param db: 从数据库中获取的数据
    :param txt: 从txt中获取的数据
    :return: 合并后的数据
    """

    # 先让data为txt，然后再从db中拿出缺失的数据

    data = []
    for i in range(len(txt)):
        flag1 = 0
        for j in range(len(data)):
            if txt[i][0] == data[j][0]:
                flag1 = 1
                break
        if flag1 == 0:
            data.append(txt[i])

    for i in range(len(db)):
        flag = 0
        if int(db[i][0]) < 10:
            db[i][0] = "20200" + db[i][0]
        elif int(db[i][0]) < 100:
            db[i][0] = "2020" + db[i][0]
        else:
            db[i][0] = "202" + db[i][0]
        for j in range(len(data)):
            if db[i][0] == data[j][0]:
                flag = 1
                break
        if flag == 0:
            data.append(db[i])


    # for i in range(len(db)):
    #     flag = 0
    #     for j in range(len(data)):
    #         if db[i][1] == data[j][1]:
    #             flag = 1
    #             break
    #     if flag == 0:
    #         if int(db[i][0]) < 10:
    #             db[i][0] = "20200" + db[i][0]
    #         elif int(db[i][0]) < 100:
    #             db[i][0] = "2020" + db[i][0]
    #         else:
    #             db[i][0] = "202" + db[i][0]
    #         data.append(db[i])

    return data

# 学生中家乡在Beijing的所有课程的平均成绩
def bjAvgGrade(data):

    """

    :param data: 清洗好的数据
    :return: 学生中家乡在Beijing的所有课程的平均成绩
    """

    total = 0
    for i in range(len(data)):
        for j in range(9):
            total += int(data[i][j+5])
    avg = total / (9 * len(data))
    return avg

# 学生中家乡在广州，课程1在80分以上，且课程9在9分以上的男同学的数量
def gz(data):
    """

    :param data: 清洗好的数据
    :return: 学生中家乡在广州，课程1在80分以上，且课程9在9分以上的男同学的数量
    """
    count = 0
    for i in range(len(data)):
        if data[i][2] == 'Guangzhou' and int(data[i][5]) > 80 and int(data[i][13]) >= 9 and data[i][3] == 'boy':
            count += 1
    return count

# 比较广州和上海两地女生的平均体能测试成绩，哪个地区的更强些
def conGZandSH(data):
    """

    :param data: 清洗好的数据
    :return: 比较广州和上海两地女生的平均体能测试成绩，哪个地区的更强些
    """
    gz = 0
    sh = 0
    for i in range(len(data)):
        if data[i][2] == 'Guangzhou' and data[i][3] == 'girl':
            if data[i][15] == 'bad':
                gz += 25
            elif data[i][15] == 'general':
                gz += 50
            elif data[i][15] == 'good':
                gz += 75
            elif data[i][15] == 'excellent':
                gz += 100
        if data[i][2] == 'Shanghai' and data[i][3] == 'girl':
            if data[i][15] == 'bad':
                sh += 25
            elif data[i][15] == 'general':
                sh += 50
            elif data[i][15] == 'good':
                sh += 75
            elif data[i][15] == 'excellent':
                sh += 100

    if gz > sh :
        return 'Guangzhou'
    else :
        return 'Shanghai'


# 学习成绩和体能测试成绩，两者的相关性是多少？
def relevance(data):
    """

    :param data: 清洗好的数据
    :return: 学习成绩和体能测试成绩，两者的相关性
    """
    result = []
    for i in range(5,14):
        # 先算出成绩平均值
        avgGrade = 0
        for j in range(len(data)):
            avgGrade += int(data[j][i])
        avgGrade = avgGrade / len(data)

        # 再算出成绩标准差
        s = 0
        for j in range(len(data)):
            s += pow(int(data[j][i]) - avgGrade,2)
        s = s / (len(data) - 1)
        std = math.sqrt(s)

        # 算出体测平均值
        avgTest = 0
        for j in range(len(data)):
            if data[j][15] == 'bad':
                avgTest += 25
            elif data[j][15] == 'general':
                avgTest += 50
            elif data[j][15] == 'good':
                avgTest += 75
            elif data[j][15] == 'excellent':
                avgTest += 100
        avgTest = avgTest / len(data)

        # 算出体测标准差
        stdTest = 0
        for j in range(len(data)):
            if data[j][15] == 'bad':
                stdTest += pow((25 - avgGrade),2)
            elif data[j][15] == 'general':
                stdTest += pow((50 - avgGrade),2)
            elif data[j][15] == 'good':
                stdTest += pow((75 - avgGrade),2)
            elif data[j][15] == 'excellent':
                stdTest += pow((100 - avgGrade),2)
        stdTest = stdTest / (len(data) - 1)
        stdTest = math.sqrt(stdTest)

        # 算出A
        A = []
        a = 0
        for j in range(len(data)):
            a = (int(data[j][i]) - avgGrade) / std
            A.append(a)

        # 算出B
        B = []
        b = 0
        for j in range(len(data)):
            if data[j][15] == 'bad':
                b = (25 - avgTest) / stdTest
            elif data[j][15] == 'general':
                b = (50 - avgTest) / stdTest
            elif data[j][15] == 'good':
                b = (75 - avgTest) / stdTest
            elif data[j][15] == 'excellent':
                b = (100 - avgTest) / stdTest
            B.append(b)

        # 最后算出A·B
        # print(A)
        # print(B)
        aa = np.array(A)
        bb = np.array(B)
        res = np.dot(aa,bb)
        # print("res---------",res)
        result.append(res)
    return result

def writeCsv(data):
    """

    :param data: 把清洗好的数据写入csv文件
    :return: Null
    """
    f = open('data3.csv', 'w', newline='')
    writer = csv.writer(f)
    for i in data:
        writer.writerow(i)
    f.close()


text = getTxtData()
text = changeSex(text)
text = changeHeight(text)
text = Process(text)
# print(text)



dbtext = getDbData()
dbtext = Process(dbtext)
data = merge(dbtext, text)

for j in range(len(data)):
    if data[j][15] == 'bad':
        data[j][15] = '25'
    elif data[j][15] == 'general':
        data[j][15] = '50'
    elif data[j][15] == 'good':
         data[j][15] = '75'
    elif data[j][15] == 'excellent':
        data[j][15] = '100'

f = open('data4.csv', 'w', newline='')
writer = csv.writer(f)
writer.writerow(['ID', 'Name', 'City', 'Gender', 'Height', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'Constitution'])
for i in data:
    writer.writerow(i)
f.close()

print("学生中家乡在Beijing的所有课程的平均成绩:", bjAvgGrade(data))
print("学生中家乡在广州，课程1在80分以上，且课程9在9分以上的男同学的数量:", gz(data))
print("比较广州和上海两地女生的平均体能测试成绩，哪个地区的更强些:", conGZandSH(data))
print("学习成绩和体能测试成绩，两者的相关性是多少？\n", relevance(data))

