c = int(input('请输入一个数字：'))

a=str(c)
a=a[::-1]
b=int(a)
if b==c:
    print('yes')
else:
    print('no')