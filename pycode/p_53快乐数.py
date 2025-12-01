def change(x):
    sum=0
    while x > 0:
        j = x%10
        sum+=j*j
        x//=10
    return sum

def happynumber(n):
    while n>9:
        n=change(n)
    if n==1:
        return True
    else:
        return False
print(happynumber(19))
