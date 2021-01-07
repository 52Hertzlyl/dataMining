import matplotlib.pyplot as plt
import csv
import random
import numpy as np


# 计算该簇的平均值得到新的簇点
def avg(x):
    sum1 = 0
    sum2 = 0
    for i in range(len(x)):
        sum1 = sum1 + x[i][0]
        sum2 = sum2 + x[i][1]
    sum1 = sum1 / (len(x))
    sum2 = sum2 / (len(x))
    return sum1, sum2


# 计算欧氏距离
def dis(x, y):
    """

    :param x:
    :param y:
    :return: 2个坐标之间的距离
    """
    dis1 = (x[0] - y[0]) ** 2
    dis2 = (x[1] - y[1]) ** 2
    dis = pow((dis1 + dis2), 0.5)
    return dis


# 随机生成k个簇心
def rand_heart(data, k):
    cluster_heart = []
    # 随机在data选一个元素作为簇心
    for i in range(k):
        a = random.choice(data)
        cluster_heart.append(a)
    return cluster_heart


# k-means
def k_means(data, k):
    # 数据行的数目
    m = len(data)

    # 生成 每个点的归属簇和离簇距离
    point_to_cluster = [[0 for i in range(2)] for i in range(m)]

    # 定义循环标志
    cluster_flag = True
    # 碎金生成k个簇心
    cluser_heart = rand_heart(data, k)

    # 如果当前所以点的簇心都没更新过，那么这个循环停止，代表聚类成功
    while cluster_flag:
        cluster_flag = False
        # 遍历所有的点（行数）
        for i in range(m):
            # 初始最小距离
            min_dist = 10000000.0
            # 初始簇心序号
            min_cluster_num = -1

            # 对于每个点,找到它当前最近的簇心
            for j in range(k):
                # 计算该点到质心的欧式距离
                distance = dis(cluser_heart[j], data[i])

                if distance < min_dist:
                    min_dist = distance
                    min_cluster_num = j
                point_to_cluster[i] = min_cluster_num, min_dist
            # 如果当前的点的簇心还有比之前距离更小的簇心的话
            if point_to_cluster[i][0] != min_cluster_num:
                cluster_flag = True
        # 更新簇心
        for j in range(k):
            sum = []
            for i in range(m):
                if point_to_cluster[i][0] == j:
                    sum.append(data[i])
            # 赋予新的簇心
            s1, s2 = avg(sum)
            cluser_heart[j][0] = s1
            cluser_heart[j][1] = s2

    return cluser_heart, point_to_cluster


# 画图
def show(data, k, cluster_heart, point_to_cluster):
    # 计算行数
    m = len(data)
    mark = ['or', 'ob', 'og', 'ok', 'oy', 'om']

    # 绘制所有的点
    for i in range(m):
        markIndex = int(point_to_cluster[i][0])
        plt.plot(data[i][0], data[i][1], mark[markIndex])

    theta = np.arange(0, 2 * np.pi, 0.01)

    mark = ['Dr', 'Db', 'Dg', 'Dk', 'Dy', 'Dm']
    color = ['r', 'b', 'g', 'k', 'y']
    # 绘制簇心
    print(len(point_to_cluster))
    for i in range(k):
        r = 0
        plt.plot(cluster_heart[i][0], cluster_heart[i][1], mark[i])
        for x in range(len(point_to_cluster)):
            if i == point_to_cluster[x][0]:
                if r < point_to_cluster[x][1]:
                    r = point_to_cluster[x][1]
        r = pow(r, 0.5)
        plt.plot(cluster_heart[i][0] + r * np.cos(theta), cluster_heart[i][1] + r * np.sin(theta), color[i])
    png_name = "测试数据：k等于%i的聚类.png" % k
    plt.savefig(png_name, format='png')
    plt.show()


if __name__ == '__main__':
    # 声明一个列表存入归一化二维矩阵
    normal_list = []
    # 这里面再读取一次文件再存入新的文件的目的是，由于一开始存入文件的数据类型为string,这里转换为float了再存入新的文件后读取
with open('测试数据.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        # string 转换 float
        temp1 = float(row[0])
        temp2 = float(row[1])
        temp = [temp1, temp2]
        normal_list.append(temp)

# 设置K值
k = 5
# 聚类算法
cluser_heart, point_to_cluster = k_means(normal_list, k)
# 画图函数
show(normal_list, k, cluser_heart, point_to_cluster)

