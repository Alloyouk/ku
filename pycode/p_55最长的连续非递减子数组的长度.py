def func(list):
    max_len = 0
    current_len = 1
    for i in range(1, len(list)):
        if list[i] >= list[i - 1]:
            current_len += 1
        else:
            if current_len > max_len:
                max_len = current_len
            current_len = 1
    if current_len > max_len:
        max_len = current_len
    return max_len
print(func([2,3,5,6,1,4,7,8,9]))