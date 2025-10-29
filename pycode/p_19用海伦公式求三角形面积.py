import math
a = int(input("请输入三角形的第一条边长："))
b = int(input("请输入三角形的第二条边长："))
c = int(input("请输入三角形的第三条边长："))
p = (a+b+c)/2
s = math.sqrt((p-a)*(p-b)*(p-c)*p)
print('三角形的面积为：%.2f'%s)#保留两位小数