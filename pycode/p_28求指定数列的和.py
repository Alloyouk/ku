sum=0
up=2
down=1
for i in range(20):
    sum+=up/down
    a=down
    down=up
    up=up+a
print(sum)