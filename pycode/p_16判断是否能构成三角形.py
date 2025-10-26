a=float(input('请输入第一条边：'))
b=float(input('请输入第二条边：'))
c=float(input('请输入第三条边：'))
if a<=0 or b<=0 or c<=0:
    print('输入错误，边长必须为正数')
if a+b>c and a+c>b and b+c>a:
    print('可以构成三角形')
else:
    print('不能构成三角形')