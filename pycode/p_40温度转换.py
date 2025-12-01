a=int(input('摄氏度请按1，华氏度请按2：'))

if a==1:
    b=float(input('请输入摄氏度：'))
    c=(b*9/5)+32
    print('华氏度为：',c)
else:
    d=float(input('请输入华氏度：'))
    e=(d-32)*5/9
    print('摄氏度为：',e)