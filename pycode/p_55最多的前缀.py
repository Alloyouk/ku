def func(strs):
    n= len(strs)
    if n==0:
        return ''
    for i in range(len(strs[0])):
        temp = strs[0][i]
        for j in range(1,n):
            if i == len(strs[j]) or temp != strs[j][i]:
                return strs[0][0:i]
    return strs[0]

list = ['abcd','abdd','abcdef']
print(func(list))
