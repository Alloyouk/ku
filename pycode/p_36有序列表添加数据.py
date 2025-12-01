list=[1,14,5,7]
b=list.copy() #浅拷贝
b=sorted(list)
c=input('请输入一个数字：')
b.append(int(c))
b=sorted(b)
print(b)

list2=[1,14,5,7]
d=int(input('请输入一个数字：'))
list.append(d)
list.sort()
print(list)