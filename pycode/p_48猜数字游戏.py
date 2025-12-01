import random

target = random.randint(1,99)



times = 7
while times!=0:
    a=int(input('请输入你猜的数字'))
    if a<target:
        print('你猜小了')
        #times-=1
        #continue
    elif a>target:
        print('你猜大了')
    else:
        print('congratulations')
        break
    times-=1
    print('你还有',times,'次机会')
if times==0:
    print('很遗憾，游戏结束，正确数字是',target)