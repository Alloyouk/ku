#转为字符串型 再根据索引取值
for i in range(100,1000):
    a=i%10
    b=(i%100)//10
    c=i//100
    list=[]
    if a**3+b**3+c**3==i:
        list.append(i)
        print(list)