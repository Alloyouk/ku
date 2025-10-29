
for i in range(1,1000):
    sum=0
    for j in range(1,i):
            if i%j==0:
                  sum+=j
    if sum==i:
          print(f'{i}是完数')