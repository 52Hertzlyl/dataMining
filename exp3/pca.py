# encoding: utf-8
from sklearn.decomposition import PCA
from pandas.core.frame import DataFrame
import numpy as np

if __name__ == '__main__':

    normal_list = []
    # 打开处理好的归一化矩阵数据
    with open('归一化矩阵.csv', 'r') as f:
        line = f.readline()
        while line:
            if line == "":
                continue
            word = line.split(",")
            normal_list.append(word)
            line = f.readline()

    normal_dataframe = DataFrame(normal_list)
    print(normal_dataframe)
    normal_array = np.array(normal_dataframe)

    # 将数据降到二维
    pca_sk = PCA(n_components=2)
    normal_2D_array = pca_sk.fit_transform(normal_array)

    # 存入新的csv
    data1 = DataFrame(normal_2D_array)
    data1.to_csv('PCA.csv', index=False, header=False)
    print("降维成功")
