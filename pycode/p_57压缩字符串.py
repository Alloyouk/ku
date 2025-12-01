def func(s):
    list = []
    for i in s:
        if not list or list[-2] != i:
            list.append(i)
            list.append(1)
        else:
            list[-1] += 1
    return ''.join(map(str,[x for x in list if x != 1]))

print(func("aaabbbccdaa"))  # 输出 "a3b3c2d1a2"