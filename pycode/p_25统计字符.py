string = input ('请输入字符串：')
char=0
number=0
space=0
other=0
for i in string:#遍历字符串中的每一个字符
    if i.isalpha():
        char+=1
    elif i.isdigit():
        number+=1
    elif i.isspace():
        space+=1
    else:
        other+=1
print(f'字母有{char}个，数字有{number}个，空格有{space}个，其他字符有{other}个')