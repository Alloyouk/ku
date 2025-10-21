list=[]
for i in range(1,100):
    if i%2!=0:#不等于
        list .append(i)
        print(list)

#第二种方法
llst=[]
for i in range(1,100,2):#间隔
    list.append(i)#追加和列表
    print(list)
