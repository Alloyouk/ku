#递归
def fib(n):
	if n == 1 or n == 2:
		return (1)
	else:
		return fib(n-1) + fib(n-2)
print(fib(6))

#非递归
n=6
fibs=[1,1]
for i in range(2,n+1):
	fibs.append(fibs[i-1]+fibs[i-2])
print (fibs[n-1])#输出第n个斐波那契数