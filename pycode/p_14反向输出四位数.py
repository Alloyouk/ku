a=int(input("请输入一个四位数："))
a=str(a)#转为字符串型
a=a[::-1]#字符串切片逆序
a=int(a)
print(f"该四位数的反向输出结果为：{a}")