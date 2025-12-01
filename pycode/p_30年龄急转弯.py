
def func(n):
    if n==1:
        return 10
    else:
        return func(n-1) + 2
print(func(5))