import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import csv

# 设置matplotlib正常显示中文和负号
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号


# 计算某一行的平均值
def calc_mean(x):
    """

    :param x:传入列表的某一行
    :return: 返回该行的平均值
    """
    lens = len(x)
    total = 0
    for i in range(lens):
        total = total + x[i]
    ave = total / lens
    return ave


# 计算E(ab)
def calc_Eab(a, b):
    """

    :param a:
    :param b:
    :return:
    """
    lens = len(a)
    total = 0
    for i in range(lens):
        total = total + a[i] * b[i]
    Eab = total / lens
    return Eab


def square(x):
    """

    :param x:传入一个数组
    :return: 返回数组的平方
    """
    res = x ** 2
    return res


# 计算a和b的协方差
def calc_corr(a, b):
    """

    :param a:a学生成绩
    :param b:b学生成绩
    :return: a和b的协方差
    """
    # 计算E(a) E(b) E(ab)
    E_a = calc_mean(a)
    E_b = calc_mean(b)
    E_ab = calc_Eab(a, b)
    # 计算分子，协方差—cov(a,b)=E(ab)-E(a)*E(b)
    cov_ab = E_ab - E_a * E_b
    # 计算分母，D(X)=E(X²)-E²(X)
    square_a = square(a)
    square_b = square(b)
    D_a = calc_mean(square_a) - E_a ** 2
    D_b = calc_mean(square_b) - E_b ** 2
    # 方差开平方就标准差
    std_a = pow(D_a, 0.5)
    std_b = pow(D_b, 0.5)
    # 相关系数保留小数点后6位
    corr_factor = '%.6f' % (cov_ab / (std_a * std_b))
    return corr_factor


# 冒泡排序 从大到小
def bubble_sort(data, id):
    """

    :param data:归一化矩阵
    :param id: id矩阵
    :return: 排序后的归一化矩阵，id矩阵也跟着一起排序
    """
    for i in range(0, len(data) - 1):
        for j in range(0, len(data) - i - 1):
            if data[j] < data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                id[j], id[j + 1] = id[j + 1], id[j]
    return data


if __name__ == '__main__':

    # 读取实验一的数据
    data = pd.read_csv('data3.csv')

    # 第1题
    # 将体能成绩的非数值评价转换为数值评价,分别是“100,75,50,25”
    data = data.replace({"Constitution": {"excellent": 100, "good": 75, "general": 50, "bad": 25}})
    # x轴是C1课程成绩 y轴是体能成绩
    x = data.iloc[:, 5]
    y = data.iloc[:, 15]
    # 将数值评价转换为非数值评价，这样可以保值它的y轴递增顺序是正确的的
    plt.yticks([100, 75, 50, 25], ['$excellent$', '$good$', '$general$', '$bad$'])
    # 绘制散点图
    plt.scatter(x, y, c='coral')
    plt.title("C1成绩和体能成绩散点图")
    plt.xlabel('C1成绩')
    plt.ylabel('体能成绩')
    plt.savefig("C1成绩和体能成绩散点图.png")
    plt.show()

    # 第2题
    print("第2题的打印：")
    print('C1成绩的最低分：' + str(x.min()))
    print('C1成绩的最高分：' + str(x.max()))

    # 绘制直方图
    # 因为最低分是67，最高分是90 因此直方图X轴的区间设定在[65,90]
    plt.hist(x, histtype='bar', bins=[65, 70, 75, 80, 85, 90, 95], color="coral")
    plt.xlabel("C1成绩")
    plt.ylabel("人数")
    plt.title("C1成绩直方图")
    plt.savefig("C1成绩直方图.png")
    plt.show()

    # 第3题

    # 记录每位同学成绩的数组
    mark_array = []
    with open('data3.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            # 跳过列名不加入array
            if row[0] == 'ID':
                continue
            if row[15] == 'bad':
                row[15] = '65'
            if row[15] == 'general':
                row[15] = '75'
            if row[15] == 'good':
                row[15] = '85'
            if row[15] == 'excellent':
                row[15] = '95'
            mark_array.append(row[5:])

    # 字符串转整型
    for i in range(len(mark_array)):
        for j in range(len(mark_array[0])):
            mark_array[i][j] = int(mark_array[i][j])

    # 记录每位同学成绩的矩阵
    mark_matrix = np.array(mark_array)

    # 去除全0的第九列
    mark_matrix = np.delete(mark_matrix, 9, axis=1)
    print("第3题的打印：")
    print("去除全0的第九列的成绩矩阵：")
    print(mark_matrix)

    # 矩阵的行数 和 列数
    row = len(mark_matrix)
    col = len(mark_matrix[0])
    print("矩阵的行数：" + str(len(mark_matrix)))
    print("矩阵的列数：" + str(col))

    # 记录10个成绩的平均值数组
    score_avg = []
    # 记录每列全部数值的和
    total = 0
    for i in range(col):
        for j in range(row):  # j是106
            total = total + mark_matrix[j][i]
        score_avg.append(total / row)
        total = 0
    print("每列的平均值：")
    print(score_avg)

    # 记录10个成绩的标准差数组
    score_std = []
    # 记录10个成绩的标准差数组
    score_var = []
    # 记录每列全部 (x-均值)**2 的和
    total = 0
    for i in range(col):
        for j in range(row):
            total = total + (mark_matrix[j][i] - score_avg[i]) ** 2
        total = total / row
        score_var.append(total)
        std = pow(total, 0.5)
        score_std.append(std)
        total = 0
    print("每列的标准差：")
    print(score_std)

    # 创建一个空矩阵来记录每个标准化后的数组
    Normalized_matrix = np.zeros((106, 10))
    # z-score标准化 x-均值/标准差
    for i in range(col):
        for j in range(row):
            Normalized_matrix[j][i] = (mark_matrix[j][i] - score_avg[i])
            Normalized_matrix[j][i] = Normalized_matrix[j][i] / score_std[i]
    print("z-score标准化：")
    print(Normalized_matrix)

    # 保存归一化矩阵
    np.savetxt('归一化.csv', Normalized_matrix, delimiter=',')

    # 第4.5题
    score_array = []  # 106个同学所有成绩的矩阵 106*106
    id_col = []  # 获取每个同学的id 1*106
    with open('data3.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            # 跳过列名不加入array
            if row[0] == 'ID':
                continue
            if row[15] == 'bad':
                row[15] = '65'
            if row[15] == 'general':
                row[15] = '75'
            if row[15] == 'good':
                row[15] = '85'
            if row[15] == 'excellent':
                row[15] = '95'
            score_array.append(row[5:])
            id_col.append(row[0:1])

# 字符串转整型
for i in range(len(score_array)):
    for j in range(len(score_array[0])):
        score_array[i][j] = int(score_array[i][j])

score_matrix = np.array(score_array)
id_col = np.array(id_col)
# 将提取的id列变成id行，然后依次加入id——matrix
id_row = id_col[:, 0]
# id 矩阵 106*106
id_matrix = []

for i in range(106):
    id_matrix.append(id_row)

id_matrix = np.array(id_matrix)
# id矩阵写入csv文件
# np.savetxt('id_matrix.txt', id_matrix, delimiter=',', fmt='%s')

# 第4题
# 矩阵相关度计算
# 创建一个空矩阵来记录每个相关度
corr_matrix = np.zeros((106, 106))

# 将矩阵的每一行进行相关度的计算
row = len(score_matrix)
col = len(score_matrix[0])
# 得到协相关矩阵
for i in range(row):
    for j in range(row):
        r_ab = calc_corr(score_matrix[i], score_matrix[j])
        corr_matrix[i][j] = r_ab
print("第4题的打印：")
print('相关矩阵的维度：' + str(corr_matrix.shape))
print('相关矩阵：')
print(corr_matrix)
# 协相关矩阵写入csv文件
np.savetxt('correlation_matrix .csv', corr_matrix, delimiter=',')

# 协相关矩阵可视化为混淆矩阵
confusion_matrix = pd.DataFrame(corr_matrix)
sns.heatmap(confusion_matrix, annot=False)
plt.savefig("confusion_matrix.png")
plt.title("相关矩阵可视化为混淆矩阵")
plt.show()

# 第5题
# 根据相关矩阵，找到距离每个样本最近的三个样本
# 对相关矩阵进行从大到小排序，那么id矩阵也跟着排序，最后输出的txt是在id矩阵实现的

sort_corr = np.zeros((106, 106))
for i in range(row):
    sort_corr[i] = bubble_sort(corr_matrix[i], id_matrix[i])

# 排序后的协相关矩阵
np.savetxt("每个点距离从近到远的ID.csv", id_matrix, delimiter=',', fmt='%s')

# 找到每个点最近的3个点,并且把3个点都输入到txt文件
file = open('每个点距离最近3个点的ID.txt', 'w')
for i in range(row):
    for j in range(4):
        if j == 0:
            continue
        file.write(str(id_matrix[i][j]))
        blank = '\t'
        file.write(blank)
    line = '\n'
    file.write(line)
file.close()
