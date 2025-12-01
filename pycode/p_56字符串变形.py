def func(s):
    l = s.split(' ')
    l=l[::-1]
    s=""
    for i in l:
        i = i.swapcase()
        s += i
        s += ' '
    return s[0:len(s)-1]
