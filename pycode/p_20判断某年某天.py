import datetime
year,month,day = map(int,input().split(' '))#匹配函数
yuandan = datetime.date(year,1,1)
now = datetime.date(year,month,day)
s = (now-yuandan).days +1
print(s)