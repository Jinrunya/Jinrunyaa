import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

temperature = pd.read_csv("C:\\Users\\vip\\Desktop\\temp\\daily_KP_SUN_2020.csv", usecols=["數值/Value"])
temperature = np.array(temperature)


def average(list):
    length = len(list)
    result = 0
    for i in range(length):
        result = result + list[i]
    result = result / length
    return result


def amount(list):
    length = len(list)
    result = 0
    for i in range(length):
        result = result + list[i]
    return result


list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []
list7 = []
list8 = []
list9 = []
result = 0
for i in range(31):
    list1.append(float(temperature[i]))

for i in range(29):
    list2.append(float(temperature[i + 31]))

for i in range(31):
    list3.append(float(temperature[i + 31 + 29]))

for i in range(30):
    list4.append(float(temperature[i + 31 + 29 + 31]))

for i in range(31):
    list5.append(float(temperature[i + 31 + 29 + 31 + 30]))

for i in range(30):
    list6.append(float(temperature[i + 31 + 29 + 31 + 30 + 31]))

for i in range(31):
    list7.append(float(temperature[i + 31 + 29 + 31 + 30 + 31 + 30]))

for i in range(31):
    list8.append(float(temperature[i + 31 + 29 + 31 + 30 + 31 + 30 + 31]))

for i in range(30):
    list9.append(float(temperature[i + 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31]))

a1 = average(list1)
a2 = average(list2)
a3 = average(list3)
a4 = average(list4)
a5 = average(list5)
a6 = average(list6)
a7 = average(list7)
a8 = average(list8)
a9 = average(list9)

t1 = amount(list1)
t2 = amount(list2)
t3 = amount(list3)
t4 = amount(list4)
t5 = amount(list5)
t6 = amount(list6)
t7 = amount(list7)
t8 = amount(list8)
t9 = amount(list9)

# 创建一个点数为 8 x 6 的窗口, 并设置分辨率为 80像素/每英寸
plt.figure(figsize=(10, 20), dpi=80)
# 再创建一个规格为 1 x 1 的子图
plt.subplot(2, 1, 1)
# 柱子总数
N = 9
# 包含每个柱子对应值的序列
values = (a1, a2, a3, a4, a5, a6, a7, a8, a9)
# 包含每个柱子下标的序列
index = np.arange(N)
# 柱子的宽度
width = 0.35
# 绘制柱状图, 每根柱子的颜色为紫罗兰色
p2 = plt.bar(index, values, width, label=" Monthly average sunlight", color="#3CC9DE")
# 设置横轴标签
plt.xlabel('Months')
# 设置纵轴标签
plt.ylabel('average sunlight')
# 添加标题
plt.title('Monthly average sunlight')
# 添加纵横轴的刻度
plt.xticks(index, ('1', '2', '3', '4', '5', '6', '7', '8', '9'))
plt.yticks(np.arange(0, 20, 1))
# 添加图例
plt.legend(loc="upper right")

plt.subplot(2, 1, 2)
# 柱子总数
N = 9
# 包含每个柱子对应值的序列
values2 = (t1, t2, t3, t4, t5, t6, t7, t8, t9)
# 包含每个柱子下标的序列
index = np.arange(N)
# 柱子的宽度
width = 0.35
# 绘制柱状图, 每根柱子的颜色为紫罗兰色
p2 = plt.bar(index, values2, width, label="Monthly sunlight amount", color="#3CC9DE")
# 设置横轴标签
plt.xlabel('Months')
# 设置纵轴标签
plt.ylabel('sunlight amount')
# 添加标题
plt.title('Monthly sunlight amount')
# 添加纵横轴的刻度
plt.xticks(index, ('1', '2', '3', '4', '5', '6', '7', '8', '9'))
plt.yticks(np.arange(0, 250, 10))
# 添加图例
plt.legend(loc="upper right")
plt.show()
