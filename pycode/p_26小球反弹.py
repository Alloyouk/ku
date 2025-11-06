n=100
count=0
list=[]
while count<10:
    if count==0:
        list.append(n)
        count+=1
        n/=2
    else:
        list.append(2*n)
        count+=1
        n/=2
    print(list)
    print(sum(list))