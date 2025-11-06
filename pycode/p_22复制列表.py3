#浅复制直接赋值
#引用
import copy
list = [1,2,3,4]
list1=copy.copy(list)
list[0]=30
print(list1)