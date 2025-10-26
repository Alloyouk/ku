#方法一：非递归
a=5
sum=1#初始化乘积变量
for i in range (1,a+1):
    sum*=i
    print(sum)
#方法二：递归
def jie_cheng(num):
    if num==1:
        return 1
    else:
        return num*jie_cheng(num-1)
    print(jie_cheng(a))
