def func(s):
    res = ""
    for i in s:
        if i !=" ":
            res += i
        else:
            res += "%"
    return res
print(func('Hello world'))