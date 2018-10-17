# -*-coding:utf-8-*-

# 函数定义
def sum(num1, num2):
	return num1 + num2

print(sum(1,2))

# 参数传递

# 字符串，整形，浮点型，tuple 是不可更改的对象，而 list ，dict 等是可以更改的对象
# 不可更改的类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是 a 的值，没有影响 a 对象本身。比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。
# 可更改的类型：类似 c++ 的引用传递，如 列表，字典。如 fun（a），则是将 a 真正的传过去，修改后 fun 外部的 a 也会受影响
def changeNum(num):
	num = 100;

def changeList(list):
	list[0] = 'changed'

num = 1
changeNum(num)
print(num)

list = [1,2,3]
changeList(list)
print(list)

# 返回值可多个
def  division ( num1, num2 ):
    # 求商与余数
         a = num1 % num2
         b = (num1-a) / num2
         return b , a

num1 , num2 = division(9,4)
tuple1 = division(9,4)

print (num1,num2)
print (tuple1) # 元组

# 关键字参数， 另外末位参数可以有默认值
def print_user_info( name ,  age  , sex = '男' ):
    # 打印用户信息
    print('昵称：{}'.format(name) , end = ' ')
    print('年龄：{}'.format(age) , end = ' ')
    print('性别：{}'.format(sex))
    return;

# 调用 print_user_info 函数
print_user_info( name = '两点水' ,age = 18 , sex = '女')
print_user_info( name = '两点水' ,sex = '女', age = 18 )


# 不定长参数 Python 提供了一种元组的方式来接受没有直接定义的参数。这种方式在参数前边加星号 * 。如果在函数调用时没有指定参数，它就是一个空元组。
def print_user_info2( name ,  age  , sex = '男' , * hobby):
    # 打印用户信息
    print('昵称：{}'.format(name) , end = ' ')
    print('年龄：{}'.format(age) , end = ' ')
    print('性别：{}'.format(sex) ,end = ' ' )
    print('爱好：{}'.format(hobby))
    return;
print_user_info2( '两点水' ,18 , '女', '打篮球','打羽毛球','跑步')


# 匿名函数 lambda [arg1 [,arg2,.....argn]]:expression
sumFun = lambda num1, num2 : num1 + num2;
print(sumFun(1,2)) 