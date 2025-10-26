import math
a=int(input("请输入直角三角形的第一条直角边长："))

b=int(input("请输入直角三角形的第二条直角边长："))
m=a*a+b*b
c=math.sqrt(m)
print(f"斜边长为：{c}")