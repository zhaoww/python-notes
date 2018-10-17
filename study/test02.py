# -*-coding:utf-8-*-

# list
list0 = ['hello', '你好', 123]
# 索引访问列表 冒号截取列表
print(list0[1])
list1 = list0[1:3]
print(list1)

list0[2] = 456
# append添加
list0.append('app')
print(list0)
# 插入指定位置
list0.insert(2, 'insert')
print(list0)

# 删除1
list0.pop(2)
print(list0)
# 删除2
del list0[2]
print(list0)

print(len([1, 2, 3]))
# 连接
print([1,2] + [3, 4, 5])
# 复制
print([1] * 4)

# 迭代
print(3 in [1, 2, 3])
for x in [3,4,5,6]:
	print(x)

#================================================
# tuple
tuple0 = ('hello', 'world', 123)
tuple4 = 'hello', 'world', 123
# 元组中只包含一个元素时，需要在元素后面添加逗号
tuple1 = ('hello',)
tuple2 = ('hello')
tuple3 = ()
print(tuple0)
print(tuple4)
print(tuple1)
print(tuple2)
print(tuple3)

# 大体操作和list无差 只是不能修改& 删除 另外可以del删除整个元组

# 将列表转换为元组
print(tuple([1,2,3]))
# 将元组转换为列表
print(list((1,2,3)))