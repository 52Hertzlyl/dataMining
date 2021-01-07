## 项目名称：数据挖掘课作业

#### 项目组成

## 1. exp1
实验一    《多源数据集成、清洗和统计》

题目
广州大学某班有同学100人，现要从两个数据源汇总学生数据。第一个数据源在数据库中，第二个数据源在txt文件中，两个数据源课程存在缺失、冗余和不一致性，请用C/C++/Java程序实现对两个数据源的一致性合并以及每个学生样本的数值量化。
● 数据库表：ID (int),  姓名(string), 家乡(string:限定为Beijing / Guangzhou / Shenzhen / Shanghai), 性别（string:boy/girl）、身高（float:单位是cm)）、课程1成绩（float）、课程2成绩（float）、...、课程10成绩(float)、体能测试成绩（string：bad/general/good/excellent）；其中课程1-课程5为百分制，课程6-课程10为十分制。
● txt文件：ID(string：6位学号)，性别（string:male/female）、身高（string:单位是m)）、课程1成绩（string）、课程2成绩（string）、...、课程10成绩(string)、体能测试成绩（string：差/一般/良好/优秀）；其中课程1-课程5为百分制，课程6-课程10为十分制。
参考
数据库中Stu表数据
ID	Name	City	Gender	Height	C1	...	C10	Constitution
1	Sun	Beijing	boy	160	87		9	good
2	Zhu	Shenzhen	girl	177	66		8	excellent
...	...	...	...	...	...	...	...	...
student.txt中
ID		Name	City		Gender	Height    C1	。。。	C10	        Constitution
202001	Sun		Beijing	male		180	      87	。。。	9		good
202003 	Tang		Hanghai	male		156	      91	。。。	10	        general
...		...		...		..		...	..		...		...		...
两个数据源合并后读入内存，并统计：
1. 学生中家乡在Beijing的所有课程的平均成绩。
2. 学生中家乡在广州，课程1在80分以上，且课程9在9分以上的男同学的数量。(备注：该处做了修正，课程10数据为空，更改为课程9)
3. 比较广州和上海两地女生的平均体能测试成绩，哪个地区的更强些？
4. 学习成绩和体能测试成绩，两者的相关性是多少？（九门课的成绩分别与体能成绩计算相关性）
提示
参考数据结构：
Student{
int id;
string id;
vector<float> data;
}
可能用到的公式：
均值公式	
协方差公式	
z-score规范化	
数组A和数组B的相关性	
这里A=[a1, a2,...ak,..., an],
B=[b1, b2,...bk,..., bn],
mean(A)代表A中元素的平均值
std是标准差，即对协方差的开平方。
点乘的定义：


实验一__目录结构


--data1.xlsx  `插入数据库的原始数据`

--data2.txt  `从文件读入的原始数据`

--data3.csv  `清洗完毕的数据`

--data4.csv  `清洗完毕的经过特意处理数据`

--insertData.py  `插入数据库的完整代码`

--process.py  `处理和计算的完整代码`

--实验结果.png  `实验打印的结果`


实验一__结果

-- `详见实验结果.png`




## 2. exp2


实验二__目录结构

--data3.csv  `实验一预处理后的代码，供实验二使用`

--exp2.py  `实验二的完整代码`

--C1成绩和体能成绩散点图.png  `实验二_第一题`

--C1成绩直方图.png  `实验二_第二题`

--归一化矩阵.csv  `实验二_第三题`

--correlation_matrix.csv  `实验二_第四题_相关矩阵`

--confusion_matrix.png  `实验二_第四题_混淆矩阵`

--每个点距离从近到远的ID.csv  `对每位同学的相关度由近到远的一个排序`

--每个点距离最近3个点的ID.csv  `实验二_第五题_对每位同学和他\她自身相关度最高的三个同学的ID`



实验二__结果

-- `详见exp2文件夹`




## 3. exp3

实验三__目录结构


--exp3.py  `实验三的k-means的完整代码`

--pca.py  `对归一化矩阵的降维代码`

--归一化二维矩阵.csv  `降维后保存的归一化二维矩阵`

--归一化矩阵.csv  `实验二的归一化矩阵`

--测试数据.csv  `老师给的二维实验数据`

--测试数据：k等于2的聚类.png  `老师给的数据的K等于2的聚类结果`

--测试数据：k等于3的聚类.png  `老师给的数据的K等于3的聚类结果`

--测试数据：k等于4的聚类.png  `老师给的数据的K等于4的聚类结果`

--测试数据：k等于5的聚类.png  `老师给的数据的K等于5的聚类结果`

--归一化数据：k等于2的聚类.png  `归一化数据的K等于2的聚类结果`

--归一化数据：k等于3的聚类.png  `归一化数据的K等于3的聚类结果`

--归一化数据：k等于4的聚类.png  `归一化数据的K等于4的聚类结果`

--归一化数据：k等于5的聚类.png  `归一化数据的K等于5的聚类结果`



实验三__结果

-- `详见exp3文件夹`

