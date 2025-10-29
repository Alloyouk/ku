a=int(input('请输入一个整数：'))
y=2
list=[]
while a!=y:
    if a%y==0:
        list.append(y)
        a/=y
    else:
        y+=1
list.append(int(a))

#print(list) 
for i in list:
    print(f"{i}",end=' ')