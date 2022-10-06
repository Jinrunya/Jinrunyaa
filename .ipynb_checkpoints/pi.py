# Π=2*arctan(1/根号3)
import math
y=1/math.sqrt(3)
#print(y)
def PI(number):
    sn=0
    for i in range(2, number+1):
        n = pow(-1, i-1)
        tmp=pow(y,2*i-1)/(2*i-1)
        sn=n*tmp
    return sn


a = 0.000000001
i = 1
sum = y
x = 1
while abs(x) > a:
    i = i + 1
    x = PI(i)
    print(x)
    sum = sum + x
    print(sum)

print(sum * 6)

