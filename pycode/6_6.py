list=[]
a=100
for i in range(0,21):
    for o in range(0,21):
        for p in range (0,21):
            if i*5+o*3+p==a:
                list.append((i,o,p))
                print(list)
                