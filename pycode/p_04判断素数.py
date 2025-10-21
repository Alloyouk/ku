a=37
flag=False#判断
for i in range(2,a):
    if a%i==0:
        flag=True
        break#打断
if flag:#意思是true
    print("是合数")
else:
    print("是素数")