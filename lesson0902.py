import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

f1 = open('C:\\Users\\vip\\Desktop\\CODES\\datacode\\SH_Grade.csv', 'r', encoding='UTF-8')
student_data = pd.read_csv('SH_Grade.csv', dtype=str, quoting=csv.QUOTE_NONE, encoding="UTF-8")
n = student_data['Stuid'].apply(lambda x: x[0])
student_data['Class'] = n
pd.set_option('display.max_rows', None)  # 展示所有行
# print(student_data)
# print(student_data.columns)
order = ['id', 'Class', 'Stuid', 'Sex', 'CHI611', 'MATH611', 'ENG611', 'CHI612',
         'MATH612', 'ENG612', 'CHI621', 'MATH621', 'ENG621', 'CHI622', 'MATH622',
         'ENG622', 'CHI711', 'MATH711', 'ENG711', 'CHI712', 'MATH712', 'ENG712',
         'CHI721', 'MATH721', 'ENG721', 'CHI722', 'MATH722', 'ENG722', 'CHI811',
         'MATH811', 'ENG811', 'PHY811', 'CHI812', 'MATH812', 'ENG812', 'PHY812',
         'CHI821', 'MATH821', 'ENG821', 'PHY821', 'CHI822', 'MATH822', 'ENG822',
         'PHY822', 'CHI911', 'MATH911', 'ENG911', 'PHY911', 'CHE911', 'CHI912',
         'MATH912', 'ENG912', 'PHY912', 'CHE912', 'CHI921', 'MATH921', 'ENG921',
         'PHY921', 'CHE921']
student_data = student_data[order]
# print(student_data)
# task 02

student_data1 = student_data.drop_duplicates(subset=['Stuid'])
# print(student_data1)

# task 03

student_data2 = student_data1.dropna(thresh=47)
# print(student_data2)

# task 04

student_data3 = student_data2.copy()
student_data3['Sex'] = student_data3['Sex'].fillna(method='ffill')
# print(student_data3)
student_data4 = student_data3.copy()
student_data4.iloc[:, 4:] = student_data4.iloc[:, 4:].fillna(student_data4.iloc[:, 4:].median())
# print(student_data4)

# task 05
order=['CHI611', 'MATH611', 'ENG611', 'CHI612',
         'MATH612', 'ENG612', 'CHI621', 'MATH621', 'ENG621', 'CHI622', 'MATH622',
         'ENG622', 'CHI711', 'MATH711', 'ENG711', 'CHI712', 'MATH712', 'ENG712',
         'CHI721', 'MATH721', 'ENG721', 'CHI722', 'MATH722', 'ENG722', 'CHI811',
         'MATH811', 'ENG811', 'PHY811', 'CHI812', 'MATH812', 'ENG812', 'PHY812',
         'CHI821', 'MATH821', 'ENG821', 'PHY821', 'CHI822', 'MATH822', 'ENG822',
         'PHY822', 'CHI911', 'MATH911', 'ENG911', 'PHY911', 'CHE911', 'CHI912',
         'MATH912', 'ENG912', 'PHY912', 'CHE912', 'CHI921', 'MATH921', 'ENG921',
         'PHY921', 'CHE921']
student_data4[order] = student_data4[order].astype(float)
#student_data4.info()
student_data4.iloc[:, 40:43] = student_data4.iloc[:, 40:43] * 5 / 6
student_data4.iloc[:, 44:47] = student_data4.iloc[:, 44:47] * 2 / 3
student_data4.iloc[:, 49:52] = student_data4.iloc[:, 49:52] * 2 / 3
student_data4.iloc[:, 54:57] = student_data4.iloc[:, 54:57] * 2 / 3
student_data4['CHE911'] = student_data4['CHE911'] / 6 * 10
student_data4['CHE921'] = student_data4['CHE921'] / 6 * 10
#print(student_data4.iloc[:, 4:].max())


plt.figure(figsize=(20, 30), dpi=80)
# task 06
plt.subplot(121)
class_girlgirl = student_data4[student_data4['Sex'] == 'F'].groupby('Class')['Sex'].count()
# print(class_girlgirl)
class_boyboy = student_data4[student_data4['Sex'] == 'M'].groupby('Class')['Sex'].count()
# print(class_boyboy)
plt.bar(class_girlgirl.index, class_girlgirl.values,
        tick_label=['ClassA', 'ClassB', 'ClassC', 'ClassD', 'ClassE', 'ClassF', 'ClassG'], label='GirlGirl',
        color='red')
plt.bar(class_boyboy.index, class_boyboy.values,
        tick_label=['ClassA', 'ClassB', 'ClassC', 'ClassD', 'ClassE', 'ClassF', 'ClassG'], bottom=class_girlgirl.values,
        label='BoyBoy', color='black')
plt.legend(loc='best')
# plt.show()

# task 07
# print
plt.subplot(122)
chi = [c for c in student_data4.columns if 'CHI' in c]
A13 = student_data4[student_data4.Stuid == 'A13']
A15 = student_data4[student_data4.Stuid == 'A15']
# 设置绘图风格
A13chi = []
A15chi = []
for i in range(len(chi)):
    A13chi.append(float(A13[chi[i]]))
    A15chi.append(float(A15[chi[i]]))
    chi[i] = i + 1
plt.style.use('ggplot')
plt.plot(chi, A13chi, label='A13 Chinese Grade', color='red', linestyle=':', marker='.', markersize=5)
plt.plot(chi, A15chi, label='A15 Chinese Grade', color='black', linestyle='-.', marker='.', markersize=5)
# 对于X轴，只显示x中各个数对应的刻度值
_xtick_labels = ['Test{}'.format(chi[i]) for i in range(len(chi))]
plt.xticks(chi, _xtick_labels, rotation=45)
plt.xticks(fontsize=8, )  # 改变x轴文字值的文字大小
plt.title('A13 and A15 series of Chinese Score')
plt.legend()
# plt.show()


# task 08
student_badCHI_badENG = student_data4.query('CHI721<60 or ENG721<60')
# print(student_badCHI_badENG)
terrible_score = ['Stuid', 'Class', 'CHI721', 'ENG721']
outputpath='C:\\Users\\vip\\Desktop\\CODES\\datacode\\task8.csv'
student_badCHI_badENG=student_badCHI_badENG[terrible_score]
student_badCHI_badENG.to_csv(outputpath,sep=',',index=False,header=True)
# print(student_badCHI_badENG[terrible_score])

# task 09
#student_data4.info()
ClassA_student = student_data4[student_data4.Class == 'A']
ClassC_student = student_data4[student_data4.Class == 'C']
pd.set_option('display.expand_frame_repr', False)
print(ClassA_student.describe())
print(ClassC_student.describe())

"""
1.A班语文整体平均水平高于C班,且A班两极分化较小
2.A班数学整体平均水平高于C班，且A班两极分化小与语文的两极分化，但是C班两极分化比语文更严重
3.A班与C班的英语水平动态变化，并非长期压制，且C班更好的情况略多一点，A班的两极分化有时比C班更严重
4.C班的物理水平基本一直高于A班，物理学科在开设初期各个班的两极分化都较为严重
5.A班的化学一直好于C班但差距缩小
"""