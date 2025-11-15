a=1.75
b=80.5
c=b/(a**2)
if c<=18.5:
    print("过轻")
elif c<=25:
    print("正常")
elif c<=32:
    print("过重")
else:
    print("严重肥胖")
