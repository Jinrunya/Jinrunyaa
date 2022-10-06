# 蒙特卡罗法（统计试验法）
import random # 导入随机模块
S = 100000000 # 变量S为试验总次数（值设置得越大，PI的计算越准确，即频率越逼近于概率）
N = 0 # 变量N用于统计落在圆内的试验点的个数
for i in range(int(S)):
    print(1)
    x = random.random() # 获取0-1之间的随机数
    y = random.random() # 获取0-1之间的随机数
    d = (x-0.5)**2+(y-0.5)**2 # 计算试验点到圆心的欧式距离的平方
    if d<=0.5**2: # 通过比较试验点到圆心的欧式距离与圆半径的大小，判断该点是否在圆内
        N+=1
    else:
        pass
PI = 4*N/S
print(PI)
