def func(nums):
    l=[i for i in range(1,len(nums)+1)]
    l2=[]
    nums = set(nums)

    for o in l:
        if o in nums:
            continue
        else:
            l2.append(o)
    return l2