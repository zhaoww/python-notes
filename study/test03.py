# -*-coding:utf-8-*-

# dict key-value相当于java map
dict0 = {'a':11,'b':22,'c':33}
print(dict0)
dict0['a'] = 111
print(dict0['a'])

dict1 = dict0
del dict1['a']
# del dict1
print(dict1)
dict1.clear()
print(dict1)

dict2 = {(1,2):111}
# error 键不可变 可用元组 但不能用list
# dict3 = {[1,2]:111}

# set 无序
set1=set([123,456,789,123,123])
# dict使用的是大括号,dict也是无序的,只不过dict保存的是key-value键值对值,而set可以理解为只保存key值
print(set1) # result:{456, 123, 789}

set1.add(111)
print(set1)
set1.remove(111)
print(set1)