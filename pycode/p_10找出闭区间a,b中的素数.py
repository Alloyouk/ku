def prime(n):
    flag=True
    for i in range(2,n):
        if n%i==0:
            flag=False
            break
    return flag
a=int(input("请输入左端点的值："))
b=int(input("请输入右端点的值："))
list=[]
for i in range(a,b+1):
    if prime(i):
        list.append(i)
print(list)