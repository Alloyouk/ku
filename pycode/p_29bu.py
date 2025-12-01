a=20
sum=0
def jie_cheng(num):
    if num==1:
        return(1)
    else:
        return num*jie_cheng(num-1)
for i in range(1,a+1):
    sum+=jie_cheng(i)
print(sum)